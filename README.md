# TG工具集 - Static Site Publisher

[tgnice.pages.dev](https://tgnice.pages.dev) 资源导航站的静态页面生成与部署工具。

## 功能特性

- 自动生成静态 HTML 页面（首页、资源详情页、指南、FAQ 等）
- 支持 GitHub Pages 部署（通过 GitHub REST API）
- 支持 Cloudflare Pages 部署（通过 Wrangler CLI）
- 响应式设计，支持深色模式、移动端适配
- 高性能 CSS 动画与交互效果
- sitemap.xml 和 robots.txt 自动生成

## 快速开始

```bash
pip install -r requirements.txt

python main.py          # 本地构建预览
python main.py --publish --platform github       # 构建并部署到 GitHub Pages
python main.py --publish --platform cloudflare  # 构建并部署到 Cloudflare Pages
python main.py --publish --platform github --prod  # 生产环境
```

## 配置

通过环境变量设置（**不要把 Token 硬编码在代码里**）：

```bash
# GitHub Pages
export GH_TOKEN="ghp_xxx"          # Personal Access Token（需 repo 权限）
export GH_OWNER="your-github-username"  # GitHub 用户名
export GH_REPO="your-repo-name"        # 仓库名

# Cloudflare Pages（可选）
export CF_ACCOUNT_ID="your_account_id"
export CF_API_TOKEN="cfut_xxx"
export CF_PROJECT_NAME="your-project"
```

或在 Python 中直接设置：

```python
import os
os.environ["GH_TOKEN"] = "ghp_xxx"
```

## 页面结构

| 页面 | 路径 |
|------|------|
| 首页 | `/` |
| TG群关键词监控 | `/tg-monitor.html` |
| 全球手机验证码接收 | `/sms-verification.html` |
| Telegram账号资源 | `/tg-accounts.html` |
| 社交媒体账号 | `/social-accounts.html` |
| 代理IP服务 | `/proxy-services.html` |
| TG Bot开发 | `/tg-api.html` |
| 数据采集工具 | `/data-tools.html` |
| 自动化运营 | `/automation.html` |
| 会员服务 | `/membership.html` |
| 关于我们 | `/about.html` |
| 使用指南 | `/guide.html` |
| 常见问题 | `/faq.html` |
| 运营攻略 | `/guide-telegram-marketing.html` |
| 防封指南 | `/guide-telegram-safety.html` |
| 接码教程 | `/guide-sms-platform.html` |
| 账号选购 | `/guide-tg-accounts.html` |

## 部署到 GitHub Pages

1. 在 [GitHub Settings](https://github.com/settings/tokens) 生成 Personal Access Token（需 `repo` 权限）
2. 在 `config.py` 或环境变量中填入 `GH_TOKEN`、`GH_OWNER`、`GH_REPO`
3. 运行 `python main.py --publish --platform github`
4. GitHub Actions 会自动构建并部署到 `https://<owner>.github.io/<repo>/`

## 部署到 Cloudflare Pages

1. 安装 Wrangler CLI：`npm install -g wrangler`
2. 在 `config.py` 或环境变量中填入 `CF_ACCOUNT_ID` 和 `CF_API_TOKEN`
3. 运行 `python main.py --publish --platform cloudflare --prod`
