# github_deployer.py
# GitHub Pages API deployment via GitHub REST API v3

import base64
import hashlib
import json
import os
import time
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests

# Minimal retry wrapper
def _http(method: str, url: str, headers: dict, retries: int = 3, **kwargs) -> requests.Response:
    for attempt in range(retries):
        try:
            resp = requests.request(method, url, headers=headers, timeout=60, **kwargs)
            if resp.status_code in (502, 503, 504):
                time.sleep(2 ** attempt)
                continue
            return resp
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


class GitHubPagesDeployer:
    """Deploy static files to GitHub Pages via the GitHub API."""

    API = "https://api.github.com"

    def __init__(
        self,
        token: str,
        owner: str,
        repo: str,
        branch: str = "gh-pages",
        commit_message: Optional[str] = None,
    ):
        self.token = token
        self.owner = owner
        self.repo = repo
        self.branch = branch
        self.commit_message = commit_message or f"[Auto] Deploy tgnice.pages.dev @ {datetime.now().isoformat()}"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "tgnice-pages-publisher/1.0",
        })

    # ── Repository helpers ───────────────────────────────────────────────────

    def _get(self, path: str, **kw) -> requests.Response:
        return self.session.get(f"{self.API}/{path}", **kw)

    def _put(self, path: str, **kw) -> requests.Response:
        return self.session.put(f"{self.API}/{path}", **kw)

    def _post(self, path: str, **kw) -> requests.Response:
        return self.session.post(f"{self.API}/{path}", **kw)

    def _delete(self, path: str, **kw) -> requests.Response:
        return self.session.delete(f"{self.API}/{path}", **kw)

    # ── Branch operations ────────────────────────────────────────────────────

    def ensure_branch(self) -> bool:
        """Create the target branch if it doesn't exist. Returns True if branch was created."""
        try:
            resp = self._get(f"repos/{self.owner}/{self.repo}/branches/{self.branch}")
            if resp.status_code == 200:
                print(f"  [OK] Branch '{self.branch}' already exists")
                return False
        except requests.HTTPError:
            pass

        # Branch doesn't exist — create it from 'main'
        resp = self._get(f"repos/{self.owner}/{self.repo}/git/ref/heads/main")
        if resp.status_code != 200:
            # Try 'master' if 'main' doesn't exist
            resp = self._get(f"repos/{self.owner}/{self.repo}/git/ref/heads/master")
            if resp.status_code != 200:
                raise RuntimeError(
                    f"Cannot create branch '{self.branch}': "
                    f"could not find 'main' or 'master' branch (status {resp.status_code})"
                )

        ref_data = resp.json()
        main_sha = ref_data["object"]["sha"]
        create_url = f"{self.API}/repos/{self.owner}/{self.repo}/git/refs"
        resp = self._post(create_url, json={
            "ref": f"refs/heads/{self.branch}",
            "sha": main_sha,
        })
        if resp.status_code not in (200, 201):
            raise RuntimeError(f"Failed to create branch '{self.branch}': {resp.text}")
        print(f"  [OK] Branch '{self.branch}' created from main")
        return True

    def get_latest_commit_sha(self) -> Optional[str]:
        """Get the SHA of the latest commit on the target branch."""
        resp = self._get(f"repos/{self.owner}/{self.repo}/branches/{self.branch}")
        if resp.status_code == 200:
            return resp.json()["commit"]["sha"]
        return None

    def get_tree_files(self, branch_sha: str) -> dict:
        """Get all files in the current tree for the given branch SHA."""
        commit_url = f"{self.API}/repos/{self.owner}/{self.repo}/git/commits/{branch_sha}"
        resp = self._get(commit_url)
        if resp.status_code != 200:
            return {}
        commit_data = resp.json()
        tree_url = commit_data["tree"]["url"]
        tree_resp = self._get(tree_url)
        if tree_resp.status_code != 200:
            return {}
        tree_data = tree_resp.json()
        return {item["path"]: item["sha"] for item in tree_data.get("tree", []) if item["type"] == "blob"}

    # ── Git object helpers ───────────────────────────────────────────────────

    @staticmethod
    def _content_to_blob(content: bytes) -> bytes:
        """Git blob content format."""
        header = f"blob {len(content)}\0".encode()
        return header + content

    def create_blob(self, content: bytes) -> str:
        """Create a Git blob and return its SHA."""
        encoded = base64.b64encode(content).decode()
        resp = self._post(
            f"repos/{self.owner}/{self.repo}/git/blobs",
            json={"content": encoded, "encoding": "base64"},
        )
        resp.raise_for_status()
        return resp.json()["sha"]

    # ── Core deploy ──────────────────────────────────────────────────────────

    def deploy(self, build_dir: Path, delete_missing: bool = False) -> dict:
        """
        Upload all files from build_dir to GitHub Pages.

        Args:
            build_dir: Path to the built static files directory.
            delete_missing: If True, delete files on GitHub that are not in build_dir.
        """
        print(f"\n  Preparing deployment to https://{self.owner}.github.io/{self.repo}/")
        print(f"  Source: {build_dir}")

        # Ensure branch exists
        self.ensure_branch()

        # Get latest commit SHA on target branch
        latest_sha = self.get_latest_commit_sha()
        base_tree = None
        if latest_sha:
            commit_url = f"{self.API}/repos/{self.owner}/{self.repo}/git/commits/{latest_sha}"
            resp = self._get(commit_url)
            if resp.status_code == 200:
                base_tree = resp.json()["tree"]["sha"]

        # Collect local files
        local_files: dict[str, bytes] = {}
        for root, _, files in os.walk(build_dir):
            for fname in sorted(files):
                full = Path(root) / fname
                rel = str(full.relative_to(build_dir))
                local_files[rel] = full.read_bytes()

        print(f"  Local files to upload: {len(local_files)}")

        # Create blobs and build new tree entries
        new_tree_entries: list[dict] = []
        for rel_path, content in local_files.items():
            blob_sha = self.create_blob(content)
            new_tree_entries.append({
                "path": rel_path,
                "mode": "100644",
                "type": "blob",
                "sha": blob_sha,
            })

        # Create new tree
        tree_payload: dict = {"tree": new_tree_entries}
        if base_tree:
            tree_payload["base_tree"] = base_tree
        resp = self._post(
            f"repos/{self.owner}/{self.repo}/git/trees",
            json=tree_payload,
        )
        resp.raise_for_status()
        new_tree_sha = resp.json()["sha"]

        # Create commit
        commit_resp = self._post(
            f"repos/{self.owner}/{self.repo}/git/commits",
            json={
                "message": self.commit_message,
                "tree": new_tree_sha,
                "parents": [latest_sha] if latest_sha else [],
            },
        )
        commit_resp.raise_for_status()
        new_commit_sha = commit_resp.json()["sha"]

        # Update branch ref
        update_resp = self._put(
            f"repos/{self.owner}/{self.repo}/git/refs/heads/{self.branch}",
            json={"sha": new_commit_sha},
        )
        update_resp.raise_for_status()

        # Determine URL
        if self.repo.endswith(".github.io"):
            page_url = f"https://{self.owner}.github.io"
        else:
            page_url = f"https://{self.owner}.github.io/{self.repo.replace('.github.io','')}"

        print(f"  [OK] Deployment successful!")
        print(f"  [URL] {page_url}")
        print(f"  [SHA] {new_commit_sha[:7]}")

        return {
            "url": page_url,
            "commit_sha": new_commit_sha,
            "branch": self.branch,
            "files_uploaded": len(local_files),
        }

    # ── Repository info ─────────────────────────────────────────────────────

    def get_repo_info(self) -> dict:
        """Get basic repository information."""
        resp = self._get(f"repos/{self.owner}/{self.repo}")
        resp.raise_for_status()
        return resp.json()

    def is_pages_enabled(self) -> bool:
        """Check if GitHub Pages is enabled for this repository."""
        resp = self._get(f"repos/{self.owner}/{self.repo}/pages")
        return resp.status_code == 200

    def get_pages_info(self) -> dict:
        """Get GitHub Pages configuration."""
        resp = self._get(f"repos/{self.owner}/{self.repo}/pages")
        if resp.status_code == 200:
            return resp.json()
        return {}

    def enable_pages(self) -> dict:
        """Enable GitHub Pages for the repository on the target branch."""
        resp = self._post(
            f"repos/{self.owner}/{self.repo}/pages",
            json={
                "source": {
                    "branch": self.branch,
                    "path": "/",
                },
            },
        )
        if resp.status_code in (200, 201):
            print(f"  [OK] GitHub Pages enabled on branch '{self.branch}'")
            return resp.json()
        elif resp.status_code == 409:
            print(f"  [OK] GitHub Pages already enabled")
            return resp.json()
        else:
            print(f"  [WARN] Could not enable GitHub Pages: {resp.status_code} {resp.text}")
            return {}

    def wait_for_deployment(self, poll_interval: int = 5, max_wait: int = 120) -> dict:
        """Poll until the GitHub Pages site is live."""
        elapsed = 0
        while elapsed < max_wait:
            info = self.get_pages_info()
            status = info.get("status", "unknown")
            print(f"  Pages status: {status} ({elapsed}s elapsed)")
            if status == "built":
                return {"status": "live", "url": info.get("html_url", "")}
            if status == "errored":
                return {"status": "error", "info": info}
            time.sleep(poll_interval)
            elapsed += poll_interval
        return {"status": "timeout", "elapsed": elapsed}
