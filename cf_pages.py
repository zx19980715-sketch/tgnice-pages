# ─────────────────────────────────────────────
#  Cloudflare Pages API 封装
# ─────────────────────────────────────────────

import hashlib
import json
import os
import zipfile
from pathlib import Path
from typing import Optional

import requests

import requests
class PagesDeployer:
    """Cloudflare Pages 部署器"""

    def __init__(self, account_id: str, api_token: str, project_name: str):
        self.account_id = account_id
        self.api_token = api_token
        self.project_name = project_name
        self.base_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
        }

    # ── 项目操作 ────────────────────────────

    def get_project(self) -> dict:
        resp = requests.get(self.base_url, headers=self.headers, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def list_deployments(self, page: int = 1, per_page: int = 20) -> dict:
        resp = requests.get(
            f"{self.base_url}/deployments",
            headers=self.headers,
            params={"page": page, "per_page": per_page},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def get_deployment(self, deployment_id: str) -> dict:
        resp = requests.get(
            f"{self.base_url}/deployments/{deployment_id}", headers=self.headers, timeout=30
        )
        resp.raise_for_status()
        return resp.json()

    def delete_deployment(self, deployment_id: str) -> dict:
        resp = requests.delete(
            f"{self.base_url}/deployments/{deployment_id}", headers=self.headers, timeout=30
        )
        resp.raise_for_status()
        return resp.json()

    # ── 核心部署 ────────────────────────────

    def _compute_manifest(self, build_dir: Path) -> dict:
        """计算文件 manifest（content-type mapping）"""
        manifest = {}
        for root, _, files in os.walk(build_dir):
            for fname in files:
                full_path = Path(root) / fname
                rel = full_path.relative_to(build_dir)
                with open(full_path, "rb") as f:
                    content = f.read()
                digest = hashlib.sha1(content).hexdigest()
                manifest[str(rel)] = digest
        return manifest

    def _zip_directory(self, build_dir: Path) -> bytes:
        """将目录打包为 zip（无压缩，减少 CPU 开销）"""
        buf = __import__("io").BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as zf:
            for root, _, files in os.walk(build_dir):
                for fname in sorted(files):
                    full = Path(root) / fname
                    arcname = str(full.relative_to(build_dir))
                    zf.write(full, arcname)
        return buf.getvalue()

    def deploy(
        self,
        build_dir: Path,
        branch: str = "main",
        commit_message: str = "Auto deploy via API",
        commit_hash: Optional[str] = None,
        commit_dirty: bool = False,
    ) -> dict:
        """
        通过 Cloudflare Pages Direct Upload API 部署。

        参数:
            build_dir:  静态文件目录（包含 index.html 等）
            branch:     分支名（main = 生产环境）
            commit_message: 提交信息
        """
        manifest = self._compute_manifest(build_dir)
        zip_data = self._zip_directory(build_dir)

        commit_hash = commit_hash or hashlib.sha1(
            (commit_message + str(build_dir)).encode()
        ).hexdigest()[:12]

        endpoint = f"{self.base_url}/deployments"

        files = {
            "branch": (None, branch),
            "commit_hash": (None, commit_hash),
            "commit_dirty": (None, str(commit_dirty).lower()),
            "commit_message": (None, commit_message),
            "manifest": (None, json.dumps(manifest)),
            "pages_build_output_dir": (None, ""),
        }
        # zip 包作为单个字段上传，字段名必须是 zip
        files["zip"] = ("build.zip", zip_data, "application/zip")

        resp = requests.post(endpoint, headers={"Authorization": f"Bearer {self.api_token}"}, files=files, timeout=120)
        resp.raise_for_status()
        result = resp.json()

        if result.get("success"):
            info = result["result"]
            print(f"  [OK]   部署成功!")
            print(f"  [URL]  {info.get('url', 'N/A')}")
            if info.get("aliases"):
                print(f"  [ALIAS] {info['aliases']}")
        else:
            print(f"  [FAIL] 部署失败: {result}")

        return result

    def deploy_adhoc(
        self,
        build_dir: Path,
        product_id: str,
        is_production: bool = False,
    ) -> dict:
        """快捷部署方法，带产品标记"""
        branch = "main" if is_production else product_id
        return self.deploy(
            build_dir=build_dir,
            branch=branch,
            commit_message=f"[Auto] Deploy product page: {product_id}",
            commit_hash=hashlib.sha1(product_id.encode()).hexdigest()[:12],
            commit_dirty=False,
        )

    def wait_for_deployment(self, deployment_id: str, poll_interval: int = 5, max_wait: int = 300) -> dict:
        """轮询等待部署完成"""
        import time

        elapsed = 0
        while elapsed < max_wait:
            result = self.get_deployment(deployment_id)
            stage = result.get("result", {}).get("latest_stage", {})
            status = stage.get("status", "unknown")
            name = stage.get("name", "")

            print(f"  部署状态: {name} -> {status}")
            if status in ("success", "failure", "canceled"):
                return result
            time.sleep(poll_interval)
            elapsed += poll_interval

        return {"status": "timeout", "deployment_id": deployment_id}

    def cleanup_old_deployments(self, keep_latest: int = 5, branch_filter: Optional[str] = None):
        """清理旧部署，只保留最新的 N 个"""
        page = 1
        all_deps = []
        while True:
            resp = self.list_deployments(page=page, per_page=100)
            deps = resp.get("result", [])
            if branch_filter:
                deps = [d for d in deps if d.get("deployment_trigger", {}).get("metadata", {}).get("branch") == branch_filter]
            all_deps.extend(deps)
            if len(deps) < 100:
                break
            page += 1

        # 按时间倒序
        all_deps.sort(key=lambda d: d.get("created_on", ""), reverse=True)

        for dep in all_deps[keep_latest:]:
            dep_id = dep["id"]
            branch = dep.get("deployment_trigger", {}).get("metadata", {}).get("branch", "?")
            try:
                self.delete_deployment(dep_id)
                print(f"  [CLEAN] 删除旧部署 {dep_id[:8]} (branch={branch})")
            except Exception as e:
                print(f"  [SKIP]  无法删除 {dep_id[:8]}: {e}")
