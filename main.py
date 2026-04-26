#!/usr/bin/env python3
# ─────────────────────────────────────────────
#  Static Site Publisher
#  Builds pages and deploys to GitHub Pages or Cloudflare Pages
# ─────────────────────────────────────────────

import os
import sys
import argparse
import subprocess
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from generator import PageGenerator

# Import optional deployment modules
try:
    from github_deployer import GitHubPagesDeployer
    HAS_GITHUB = True
except ImportError:
    HAS_GITHUB = False

try:
    from cf_pages import PagesDeployer as CFPagesDeployer
    HAS_CF_PAGES = True
except ImportError:
    HAS_CF_PAGES = False


def _run_wrl(cmd: list[str], cwd: str = None) -> subprocess.CompletedProcess:
    """Run a wrangler command with proper environment."""
    env = os.environ.copy()
    if hasattr(config, "CF_API_TOKEN"):
        env["CLOUDFLARE_API_TOKEN"] = config.CF_API_TOKEN
    if hasattr(config, "CF_ACCOUNT_ID"):
        env["CLOUDFLARE_ACCOUNT_ID"] = config.CF_ACCOUNT_ID
    return subprocess.run(cmd, cwd=cwd, env=env, check=True)


def deploy_github(dist: Path, commit_msg: str = None) -> bool:
    """Deploy to GitHub Pages via GitHub API."""
    if not HAS_GITHUB:
        print("[ERROR] github_deployer.py not found. Install with: pip install requests")
        return False

    token = getattr(config, "GH_TOKEN", None)
    owner = getattr(config, "GH_OWNER", None)
    repo = getattr(config, "GH_REPO", None)

    if not token or token.startswith("ghp_placeholder"):
        print("[ERROR] GH_TOKEN not configured in config.py")
        return False

    if not owner or not repo:
        print("[ERROR] GH_OWNER and GH_REPO must be configured in config.py")
        return False

    print(f"\n{'=' * 56}")
    print(f"  Deploying to GitHub Pages")
    print(f"  Repository: {owner}/{repo}")
    print(f"{'=' * 56}")

    deployer = GitHubPagesDeployer(
        token=token,
        owner=owner,
        repo=repo,
        branch="gh-pages",
        commit_message=commit_msg or f"[Auto] Deploy tgnice.pages.dev @ {__import__('datetime').datetime.now().isoformat()}",
    )

    # Check repo access
    try:
        repo_info = deployer.get_repo_info()
        print(f"  [OK] Connected to repository: {repo_info.get('full_name', repo)}")
    except Exception as e:
        print(f"[ERROR] Cannot access repository: {e}")
        return False

    # Enable GitHub Pages if not already enabled
    try:
        deployer.enable_pages()
    except Exception as e:
        print(f"  [WARN] Could not enable pages: {e}")

    # Deploy
    try:
        result = deployer.deploy(dist)
        page_url = result.get("url", "")
        if page_url:
            print(f"\n  [SUCCESS] Site deployed!")
            print(f"  [URL] {page_url}")
            # Wait for build
            print(f"  [INFO] Waiting for GitHub Pages to build (may take 1-2 minutes)...")
            status = deployer.wait_for_deployment(poll_interval=10, max_wait=180)
            if status.get("status") == "live":
                print(f"  [OK] Site is live at: {status.get('url', page_url)}")
            else:
                print(f"  [INFO] Build status: {status.get('status', 'unknown')}")
                print(f"  [INFO] Check your repo settings for deployment status")
        return True
    except Exception as e:
        print(f"[ERROR] Deployment failed: {e}")
        return False


def deploy_cloudflare(dist: Path, is_production: bool = False) -> bool:
    """Deploy to Cloudflare Pages via wrangler."""
    if not HAS_CF_PAGES:
        print("[ERROR] cf_pages.py not found.")
        return False

    account_id = getattr(config, "CF_ACCOUNT_ID", None)
    token = getattr(config, "CF_API_TOKEN", None)
    project = getattr(config, "CF_PROJECT_NAME", "tgnice")

    if not account_id or not token:
        print("[ERROR] CF_ACCOUNT_ID and CF_API_TOKEN must be configured in config.py")
        return False

    print(f"\n{'=' * 56}")
    print(f"  Deploying to Cloudflare Pages")
    print(f"  Project: {project}.pages.dev")
    print(f"{'=' * 56}")

    branch = "main" if is_production else "preview"

    # Ensure project exists
    try:
        _run_wrl(
            ["wrangler", "pages", "project", "create", project,
             "--production-branch", "main"],
            cwd=str(dist)
        )
        print(f"  [OK] Project '{project}' ready")
    except subprocess.CalledProcessError:
        print(f"  [OK] Project '{project}' already exists")

    # Deploy
    cmd = ["wrangler", "pages", "deploy", str(dist),
           "--project-name", project, "--branch", branch]
    try:
        result = _run_wrl(cmd, cwd=str(dist))
        print(result.stdout.decode() if result.stdout else "")
        print(f"  [SUCCESS] Deployed to https://{project}.pages.dev")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Deployment failed: {e}")
        return False


def build(publish: bool = False, platform: str = "github",
          cleanup: bool = False, is_production: bool = False):
    print("=" * 56)
    print("  TG工具集 - Static Site Publisher")
    print("=" * 56)

    gen = PageGenerator(output_dir="dist")
    dist = gen.build_all()

    if not publish:
        return

    if platform == "github":
        success = deploy_github(dist)
    elif platform == "cloudflare":
        success = deploy_cloudflare(dist, is_production)
    else:
        print(f"[ERROR] Unknown platform: {platform}")
        print(f"  Available: github, cloudflare")
        return

    if success:
        print("\n  [ALL DONE] ")
    else:
        print("\n  [FAILED] Check errors above")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build TG工具集 static site and deploy to GitHub Pages or Cloudflare Pages"
    )
    parser.add_argument(
        "--publish", action="store_true",
        help="Build and deploy to the configured platform"
    )
    parser.add_argument(
        "--platform", choices=["github", "cloudflare"], default="github",
        help="Deployment platform (default: github)"
    )
    parser.add_argument(
        "--prod", action="store_true",
        help="Deploy to production (for Cloudflare: main branch)"
    )
    parser.add_argument(
        "--cleanup", action="store_true",
        help="Clean up old deployments after build"
    )
    args = parser.parse_args()

    build(
        publish=args.publish,
        platform=args.platform,
        cleanup=args.cleanup,
        is_production=args.prod,
    )
