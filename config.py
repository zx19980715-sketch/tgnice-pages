# config.py — tgnice.top resource hub

import os

# ── GitHub Pages ────────────────────────────
# Personal Access Token (from https://github.com/settings/tokens)
GH_TOKEN = os.getenv("GH_TOKEN", "")  # Set via environment variable — do NOT hardcode
GH_OWNER = os.getenv("GH_OWNER", "zx19980715-sketch")
GH_REPO = os.getenv("GH_REPO", "tgnice-pages")

# ── Site ─────────────────────────────────
SITE_NAME = "TG工具集"
SITE_TAGLINE = "发现实用的 Telegram 工具与资源"
SITE_URL = "https://tgnice.pages.dev"
SITE_CANONICAL = "https://tgnice.pages.dev"
SITE_DOMAIN = "tgnice.pages.dev"
SITE_LANGUAGE = "zh-CN"

# ── Branding ───────────────────────────────
ADMIN_TG = "@TGNICETOP"
BOT_TG = "https://t.me/sosojsbot"
MAIN_SITE = "https://tgnice.top"
TG_CHANNEL = "https://t.me/TGNICETOP"
TG_SHOP = "https://tgnice.top/tg-shop"

# ── Site Description ─────────────────────
SITE_DESCRIPTION = (
    "TG工具集收录TG群关键词监控、全球手机验证码、多平台社交账号、代理IP、Bot开发、"
    "数据采集、自动化运营等实用Telegram工具。透明定价，永久售后，配合@sosojsbot使用。"
)

# Social
SITE_AUTHOR = "TGNICETOP"
SITE_TWITTER = "@TGNICETOP"

# ── Resources ──────────────────────────────
RESOURCES = [
    {
        "id": "tg-monitor",
        "name": "TG群关键词监控",
        "tagline": "实时追踪群组动态",
        "description": "当 Telegram 群组中出现指定关键词时，自动推送通知。支持多账号监听、自定义过滤规则、消息转发与自动私信功能。适合需要追踪行业讨论、竞品动态、社群运营或市场情报的用户。配合 @sosojsbot 机器人使用，配置简单，运行稳定。",
        "category": "Telegram工具",
        "icon": "monitor",
        "icon_color": "#6366F1",
        "icon_color_dark": "#4F46E5",
        "highlight": "推荐",
        "features": [
            "关键词实时捕获，毫秒级推送",
            "多账号同时监听，互不干扰",
            "消息自动转发到指定群组",
            "支持自动私信目标用户",
            "后台 Web 管理面板",
            "7x24 自动运行",
        ],
        "specs": [
            ("监听上限", "50 个关键词/账号"),
            ("响应速度", "实时推送 < 1秒"),
            ("支持语言", "中文 / 英文 / 多语言"),
            ("操作系统", "Telegram 全平台"),
            ("运行时间", "7x24 自动运行"),
            ("数据保留", "30 天历史记录"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 开通账号",
            "登录管理后台添加监听规则",
            "配置关键词和目标群组",
            "实时收到推送通知",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["sms-verification", "tg-accounts", "data-tools"],
    },
    {
        "id": "sms-verification",
        "name": "全球手机验证码接收",
        "tagline": "200+国家号码，秒级接收",
        "description": "在线接收全球主流平台的注册验证码，覆盖 200+ 国家和地区。支持 Telegram、OpenAI、Twitter/X、Instagram、WhatsApp、Facebook、Amazon 等 50+ 热门平台。REST API 接口可对接自动化脚本，适合批量注册、账号矩阵运营等场景。",
        "category": "接码服务",
        "icon": "message",
        "icon_color": "#06D6A0",
        "icon_color_dark": "#059669",
        "highlight": "热门",
        "features": [
            "200+ 国家与地区号码",
            "50+ 主流平台支持",
            "秒级接收验证码",
            "REST API 接口对接",
            "Web + TG 机器人双端",
            "成功率 > 95%",
        ],
        "specs": [
            ("号码国家", "200+ 国家地区"),
            ("支持平台", "50+ 热门平台"),
            ("接收速度", "秒级到达"),
            ("API 接口", "REST API 完整文档"),
            ("号码有效期", "约 20 分钟"),
            ("成功率", "> 95%"),
        ],
        "how_to_use": [
            "充值余额到接码平台",
            "选择目标平台和国家",
            "获取临时号码并使用",
            "验证码自动展示",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-accounts", "tg-monitor", "social-accounts"],
    },
    {
        "id": "tg-accounts",
        "name": "Telegram账号资源",
        "tagline": "多类型TG账号，即买即用",
        "description": "提供多种类型的 Telegram 账号，包括全新账号、老号、靓号、企业认证号等。所有账号均经过严格检测，开通后可直接用于运营、推广或自动化脚本。提供永久售后支持，账号稳定，不易风控。",
        "category": "账号资源",
        "icon": "user",
        "icon_color": "#FF6B6B",
        "icon_color_dark": "#DC2626",
        "highlight": "",
        "features": [
            "全新账号 5 USDT 起",
            "老号带活跃群组历史",
            "靓号支持自定义选择",
            "企业认证账号服务",
            "批量采购享受折扣",
            "永久售后支持",
        ],
        "specs": [
            ("账号类型", "新号 / 老号 / 靓号 / 企业号"),
            ("账号来源", "官方渠道，正规注册"),
            ("检测流程", "三步质检，确保稳定"),
            ("交付方式", "Telegram 直接移交"),
            ("售后政策", "永久售后保障"),
            ("批量折扣", "10 个起享受批发价"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 说明需求",
            "选择合适的账号类型",
            "完成支付后快速交付",
            "永久售后支持",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-monitor", "social-accounts", "membership"],
    },
    {
        "id": "social-accounts",
        "name": "社交媒体账号",
        "tagline": "多平台账号一站式解决",
        "description": "聚合 WhatsApp、Instagram、Facebook、Twitter/X 等主流社交平台的账号资源。支持个人号、企业号、粉丝号等多种规格，满足跨境电商、社媒营销、账号矩阵等不同业务需求。",
        "category": "账号资源",
        "icon": "globe",
        "icon_color": "#FBBF24",
        "icon_color_dark": "#D97706",
        "highlight": "",
        "features": [
            "WhatsApp 多规格账号",
            "Instagram 粉丝号 / 耐用药号",
            "Facebook 个人号 / 主页",
            "Twitter/X 账号",
            "多平台企业认证号",
            "售后有保障",
        ],
        "specs": [
            ("支持平台", "WhatsApp / IG / FB / X"),
            ("账号规格", "新号 / 老号 / 耐用药号"),
            ("交付方式", "Telegram 直接移交"),
            ("企业号", "支持认证企业账号"),
            ("批量折扣", "多平台打包优惠"),
            ("售后期限", "永久售后"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 了解库存",
            "选择平台和账号规格",
            "支付后快速交付账号",
            "遇到问题永久售后",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-accounts", "sms-verification", "proxy-services"],
    },
    {
        "id": "membership",
        "name": "会员服务",
        "tagline": "全站通用，省钱省心",
        "description": "开通 TG工具集会员后，全站所有服务享受专属折扣，优先获得客服响应，解锁批量操作权限和 API 调用次数限制提升。适合长期使用多种服务的用户。",
        "category": "会员",
        "icon": "star",
        "icon_color": "#8B5CF6",
        "icon_color_dark": "#7C3AED",
        "highlight": "",
        "features": [
            "全站服务 8 折优惠",
            "专属客服通道，优先响应",
            "批量操作权限解锁",
            "API 日调用量提升",
            "专属推荐码奖励",
            "多时长灵活选择",
        ],
        "specs": [
            ("折扣力度", "全站服务 8 折"),
            ("会员期限", "月 / 季 / 年多种"),
            ("客服响应", "优先通道 < 30 分钟"),
            ("API 限制", "日调用量提升 5 倍"),
            ("推荐奖励", "每推荐1人奖励1个月"),
            ("适用服务", "全站所有工具"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 申请开通",
            "选择会员时长（月/季/年）",
            "USDT 或 CNY 支付",
            "即刻开通享受权益",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-monitor", "sms-verification", "tg-accounts"],
    },
    {
        "id": "proxy-services",
        "name": "代理IP服务",
        "tagline": "全球住宅IP，纯净独享",
        "description": "提供覆盖 100+ 国家的住宅代理 IP 和数据中心代理，适用于账号注册、数据采集、市场调研、广告验证等场景。IP 纯净，独享带宽，稳定好用。配合 TG 账号和接码服务使用效果更佳。",
        "category": "网络服务",
        "icon": "shield",
        "icon_color": "#0EA5E9",
        "icon_color_dark": "#0284C7",
        "highlight": "",
        "features": [
            "100+ 国家住宅代理",
            "独享 IP，不与其他用户混用",
            "99.9% 在线率",
            "支持 HTTP / SOCKS5 协议",
            "按流量或按 IP 计费",
            "API 接口管理",
        ],
        "specs": [
            ("IP 类型", "住宅代理 / 数据中心代理"),
            ("覆盖国家", "100+ 国家"),
            ("IP 池规模", "千万级 IP 池"),
            ("协议支持", "HTTP / HTTPS / SOCKS5"),
            ("在线率", "99.9%"),
            ("计费方式", "按流量 / 按 IP"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 了解套餐",
            "选择国家和代理类型",
            "获取 IP 和端口信息",
            "API 或后台管理 IP",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-accounts", "social-accounts", "sms-verification"],
    },
    {
        "id": "tg-api",
        "name": "TG Bot API 开发",
        "tagline": "快速搭建 Telegram 机器人",
        "description": "提供 Telegram Bot API 对接开发服务，包括关键词监控机器人、自动回复机器人、群管机器人、数据统计机器人等。支持 Python、Node.js 等主流语言，可私有化部署或使用我们的云端服务。",
        "category": "技术开发",
        "icon": "code",
        "icon_color": "#14B8A6",
        "icon_color_dark": "#0D9488",
        "highlight": "",
        "features": [
            "关键词监控 Bot 开发",
            "自动回复机器人定制",
            "群管机器人（踢人/禁言/欢迎）",
            "数据统计与报表",
            "支持 Python / Node.js",
            "私有化部署或云端托管",
        ],
        "specs": [
            ("开发语言", "Python / Node.js / Go"),
            ("Bot 类型", "监控 / 自动回复 / 群管 / 统计"),
            ("部署方式", "私有化 / 云端托管"),
            ("交付形式", "源码 / Docker 镜像 / API"),
            ("售后服务", "7x24 运维支持"),
            ("定制周期", "标准功能 3-5 个工作日"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 说明需求",
            "技术评估并出具方案",
            "确认后开始开发",
            "交付后运维支持",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-monitor", "data-tools", "membership"],
    },
    {
        "id": "data-tools",
        "name": "数据采集工具",
        "tagline": "TG群组数据，一键导出",
        "description": "批量采集 Telegram 群组和频道的成员信息、消息数据、互动统计。支持导出为 Excel、CSV、JSON 格式。可用于市场分析、竞品调研、用户画像构建等场景。",
        "category": "数据服务",
        "icon": "database",
        "icon_color": "#EC4899",
        "icon_color_dark": "#DB2777",
        "highlight": "",
        "features": [
            "TG 群组成员批量采集",
            "消息历史记录导出",
            "互动数据统计分析",
            "导出 Excel / CSV / JSON",
            "定时自动采集任务",
            "数据清洗与去重",
        ],
        "specs": [
            ("采集范围", "群成员 / 消息 / 互动统计"),
            ("导出格式", "Excel / CSV / JSON / API"),
            ("数据量级", "单次最高支持 10 万条"),
            ("采集速度", "可配置速率，防封禁"),
            ("数据字段", "用户名 / ID / 加入时间等"),
            ("使用场景", "市场分析 / 竞品调研 / CRM"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 申请权限",
            "配置采集目标和数据字段",
            "启动采集任务",
            "下载或对接 API 获取数据",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-monitor", "tg-api", "proxy-services"],
    },
    {
        "id": "automation",
        "name": "自动化运营套件",
        "tagline": "TG账号矩阵自动化管理",
        "description": "一站式管理多个 Telegram 账号的运营工作流。自动发帖、定时任务、批量私信、群组管理、数据汇总，全部在一个后台完成。支持自定义脚本，适配各种运营场景。",
        "category": "Telegram工具",
        "icon": "zap",
        "icon_color": "#F59E0B",
        "icon_color_dark": "#D97706",
        "highlight": "",
        "features": [
            "多账号统一管理后台",
            "自动定时发帖与消息群发",
            "批量私信与自动回复",
            "群组自动管理（踢广告、欢迎语）",
            "运营数据汇总报表",
            "自定义脚本支持",
        ],
        "specs": [
            ("管理规模", "支持 100+ 账号同时管理"),
            ("任务类型", "发帖 / 私信 / 群管 / 数据"),
            ("定时精度", "精确到分钟"),
            ("数据报表", "日报 / 周报 / 月报"),
            ("API 接口", "支持 Webhook 对接"),
            ("使用场景", "账号矩阵运营 / 社群营销"),
        ],
        "how_to_use": [
            "联系 @TGNICETOP 了解方案",
            "根据运营需求定制配置",
            "部署后登录后台开始使用",
            "持续优化和运维支持",
        ],
        "bot_link": "https://t.me/sosojsbot",
        "related": ["tg-monitor", "tg-api", "membership"],
    },
]

# ── Navigation ─────────────────────────────
NAV_LINKS = [
    {"label": "首页", "url": "/"},
    {"label": "TG工具", "url": "/tg-monitor.html"},
    {"label": "接码服务", "url": "/sms-verification.html"},
    {"label": "账号资源", "url": "/tg-accounts.html"},
    {"label": "使用指南", "url": "/guide.html"},
    {"label": "关于", "url": "/about.html"},
]

# ── Footer ─────────────────────────────────
FOOTER_LINKS = {
    "tools": [
        {"label": "TG群关键词监控", "url": "/tg-monitor.html"},
        {"label": "全球接码服务", "url": "/sms-verification.html"},
        {"label": "Telegram账号", "url": "/tg-accounts.html"},
        {"label": "社交媒体账号", "url": "/social-accounts.html"},
        {"label": "代理IP服务", "url": "/proxy-services.html"},
        {"label": "TG Bot开发", "url": "/tg-api.html"},
        {"label": "数据采集", "url": "/data-tools.html"},
        {"label": "自动化运营", "url": "/automation.html"},
    ],
    "resources": [
        {"label": "会员服务", "url": "/membership.html"},
        {"label": "使用指南", "url": "/guide.html"},
        {"label": "TG运营攻略", "url": "/guide-telegram-marketing.html"},
        {"label": "TG防封指南", "url": "/guide-telegram-safety.html"},
        {"label": "常见问题", "url": "/faq.html"},
    ],
    "connect": [
        {"label": "主站 tgnice.top", "url": "https://tgnice.top"},
        {"label": "@sosojsbot", "url": "https://t.me/sosojsbot"},
        {"label": "@TGNICETOP", "url": "https://t.me/TGNICETOP"},
    ],
}

# ── About ──────────────────────────────────
ABOUT_CONTENT = {
    "title": "关于 TG工具集",
    "intro": "TG工具集（tgnice.top）是一个专注于 Telegram 生态的资源导航与技术服务平台。平台聚合了 TG 群关键词监控、全球手机验证码、社交账号、代理 IP、Bot 开发、数据采集、自动化运营等实用工具，帮助用户在 Telegram 平台上更高效地开展业务、运营社群、进行市场调研。",
    "mission": "让 Telegram 工具的使用变得更简单、透明、可靠。",
    "description": "tgnice.top 收录了经过验证的 Telegram 实用工具与资源。所有服务均提供稳定运行保障、透明定价和永久售后支持。平台不追求功能数量，而是确保每个工具都经过长期验证，真正能用、好用。",
    "founded": "2023",
    "values": [
        ("稳定可靠", "所有服务均经过长期验证，确保 7x24 小时稳定可用，配备自动监控与恢复机制"),
        ("明码标价", "价格透明，无隐藏费用，支持 USDT (TRC20)、支付宝、微信支付等多种方式"),
        ("快速响应", "遇到任何问题随时联系 @TGNICETOP，客服在线，响应速度快"),
        ("持续更新", "平台持续收录新工具，根据用户需求不断优化现有服务"),
    ],
    "stats": [
        ("500+", "服务用户"),
        ("9+", "实用工具"),
        ("200+", "覆盖国家"),
        ("99.9%", "运行稳定性"),
    ],
}

# ── Blog / Guide Articles ────────────────────
ARTICLES = [
    {
        "id": "telegram-marketing",
        "slug": "guide-telegram-marketing",
        "title": "Telegram 社群运营完整攻略",
        "tagline": "从账号准备到自动化运营的实战指南",
        "description": "本文详细介绍如何从零开始搭建 Telegram 社群运营体系，涵盖账号准备、群组设置、内容运营、自动化工具使用等核心环节。适合社群运营者、市场营销人员和跨境电商从业者参考。",
        "category": "运营攻略",
        "read_time": "8 分钟",
        "sections": [
            {
                "title": "一、账号准备：打好运营基础",
                "content": "运营 Telegram 社群的第一步是确保账号本身稳定可靠。使用全新账号直接大规模操作容易触发平台风控。建议优先准备好稳定的老号或企业认证号，再开始正式运营。配合 TG 账号资源服务，可以快速获取符合运营需求的账号。",
                "bullets": [
                    "优先使用老号而非新注册账号，抗风控能力更强",
                    "企业认证号在搜索排名和信任度上更有优势",
                    "每个运营账号建议搭配独立 IP，避免关联封号",
                    "账号到手后先正常使用 3-7 天再进行大规模操作",
                ],
            },
            {
                "title": "二、群组设置：提升用户体验",
                "content": "一个设置合理的 Telegram 群组能显著提升用户体验和留存率。除了基本的群名、简介、头像之外，还需配置好权限（发言权限、邀请权限）、机器人管理、自动欢迎语、关键词过滤等。",
                "bullets": [
                    "设置清晰的群规则，减少垃圾信息和违规内容",
                    "使用群管机器人自动处理广告和违规用户",
                    "开启历史消息权限，方便新成员查看历史内容",
                    "配置关键词回复和自动欢迎语提升活跃度",
                ],
            },
            {
                "title": "三、关键词监控：把握行业动态",
                "content": "Telegram 群关键词监控是社群运营的核心能力之一。通过监控行业关键词，可以第一时间发现潜在用户、竞品动态和市场机会。TG群关键词监控工具支持多账号同时监听、关键词实时推送、自动转发等高级功能。",
                "bullets": [
                    "监控行业关键词，第一时间发现目标用户",
                    "监控竞品群动态，了解竞争对手动作",
                    "设置过滤规则，减少无关信息的干扰",
                    "关键词推送支持 Telegram 私信和邮件两种方式",
                ],
            },
            {
                "title": "四、自动化运营：提升效率",
                "content": "当群组规模扩大后，人工管理会变得困难。使用自动化运营工具可以大幅提升效率，包括自动欢迎、自动踢广告、定时发帖、批量私信等功能。自动化运营套件支持多账号统一管理，一个后台搞定所有运营任务。",
                "bullets": [
                    "自动化欢迎语和关键词回复提升用户体验",
                    "自动踢广告和敏感词过滤保持群组质量",
                    "定时群发消息保持用户活跃度",
                    "运营数据报表帮助持续优化策略",
                ],
            },
        ],
    },
    {
        "id": "telegram-safety",
        "slug": "guide-telegram-safety",
        "title": "Telegram 账号防封完全指南",
        "tagline": "避免账号被封的实战技巧",
        "description": "Telegram 对异常操作的风控越来越严格，账号一旦被封损失巨大。本文整理了从账号使用、IP 管理到自动化操作的完整防封指南，帮助长期稳定运营。",
        "category": "安全指南",
        "read_time": "6 分钟",
        "sections": [
            {
                "title": "一、IP 管理是防封的第一步",
                "content": "IP 是 Telegram 风控的核心维度之一。同一 IP 登录多个账号、使用数据中心 IP、大量账号同时操作同一 IP 段，都会触发风控。推荐使用住宅代理 IP，每个账号绑定独立 IP。",
                "bullets": [
                    "每个重要账号建议使用独立住宅代理 IP",
                    "避免使用数据中心 IP（容易被识别和封禁）",
                    "不要在多个账号之间频繁切换同一 IP",
                    "更换 IP 时逐步过渡，不要突然大范围更换",
                ],
            },
            {
                "title": "二、账号行为要自然",
                "content": "Telegram 的风控系统会分析账号行为模式。突然添加大量群组、频繁私信陌生人、短时间内发送大量相同内容，都会触发风控。建议账号操作要模拟真人行为，有节奏地渐进操作。",
                "bullets": [
                    "新账号前 3-7 天正常浏览和使用",
                    "添加群组和联系人要分批次、有节奏",
                    "私信陌生人要控制频率，避免被举报",
                    "发布内容要多样化，避免重复内容轰炸",
                ],
            },
            {
                "title": "三、敏感操作要注意",
                "content": "某些操作在 Telegram 上属于高风险行为，包括拉人进群过于频繁、创建大量群组、加入被举报过的群组、使用第三方不安全的机器人等。了解这些限制并规避，可以大幅降低封号风险。",
                "bullets": [
                    "拉人进群控制节奏，避免单次拉大量",
                    "避免加入被 Telegram 标记的群组",
                    "谨慎使用第三方机器人，优先选择官方 Bot API",
                    "定期检查账号状态，发现异常及时处理",
                ],
            },
        ],
    },
    {
        "id": "sms-platform-guide",
        "slug": "guide-sms-platform",
        "title": "全球接码平台使用完全教程",
        "tagline": "如何用接码服务高效完成账号注册",
        "description": "详细讲解全球接码服务的使用方法，从充值、选号、接码到 API 对接，覆盖 Telegram 注册、OpenAI 账号、Twitter 等热门平台的操作流程。",
        "category": "使用教程",
        "read_time": "5 分钟",
        "sections": [
            {
                "title": "一、准备工作",
                "content": "开始使用接码服务前，需要准备好充值余额和目标平台信息。平台支持 USDT、支付宝、微信三种充值方式，到账速度快。",
                "bullets": [
                    "联系 @TGNICETOP 获取充值指引",
                    "充值后确认余额到账再开始选号",
                    "确认目标平台支持的国家和价格",
                ],
            },
            {
                "title": "二、选择号码",
                "content": "不同国家和平台的价格和成功率不同。建议选择成功率较高的国家（如俄罗斯、印尼、英国等）的号码。热门平台如 Telegram、OpenAI、Twitter 建议选择对应区域号码。",
                "bullets": [
                    "Telegram 推荐：俄罗斯、英国、印尼号码",
                    "OpenAI 推荐：美国、英国号码",
                    "Twitter/X 推荐：印度、巴西号码",
                    "避开高风险国家的敏感号码",
                ],
            },
            {
                "title": "三、API 对接（进阶）",
                "content": "对于需要批量注册的场景，可以使用 REST API 接口对接接码服务。平台提供完整的 API 文档，支持获取号码、获取验证码、释放号码等操作。",
                "bullets": [
                    "联系 @TGNICETOP 获取 API 密钥",
                    "API 支持 Python、Node.js、Go 等语言",
                    "建议设置超时机制，避免号码过期损失",
                    "批量操作时控制请求频率",
                ],
            },
        ],
    },
    {
        "id": "tg-accounts-types",
        "slug": "guide-tg-accounts",
        "title": "Telegram 账号类型详解与选购指南",
        "tagline": "新号、老号、靓号、企业号有什么区别？",
        "description": "市面上 TG 账号分为全新账号、老号、靓号、企业认证号等多种类型，价格和适用场景各不相同。本文详细对比各类型账号的优缺点，帮助你选择最适合的账号。",
        "category": "选购指南",
        "read_time": "7 分钟",
        "sections": [
            {
                "title": "一、全新账号",
                "content": "全新注册的 Telegram 账号，价格最低，适合预算有限但对账号质量要求不高的场景。但全新账号抗风控能力较弱，不建议直接用于重要业务。",
                "bullets": [
                    "价格低，5 USDT 起",
                    "注册时间短，即买即用",
                    "抗风控能力较弱",
                    "适合测试场景或短期使用",
                ],
            },
            {
                "title": "二、老号（带历史）",
                "content": "注册时间较长、有正常使用历史的账号。拥有真实用户的活跃度数据，抗风控能力显著强于新号。适合需要长期稳定运营的用户。",
                "bullets": [
                    "有加入群组和聊天历史",
                    "抗风控能力较强",
                    "适合长期运营和营销使用",
                    "价格适中，性价比高",
                ],
            },
            {
                "title": "三、靓号",
                "content": "用户名（@username）具有一定规律或特殊含义的账号，如含关键词、吉利数字、连号等。靓号在展示和品牌推广上更有优势，适合用于对外展示的官方账号。",
                "bullets": [
                    "@username 有特定规律或含义",
                    "品牌展示效果更好",
                    "价格根据靓号稀缺程度浮动",
                    "适合官方客服号、品牌展示号",
                ],
            },
            {
                "title": "四、企业认证号",
                "content": "通过 Telegram 官方企业认证的账号，拥有官方认证徽章，在搜索排名和用户信任度上都有显著优势。适合需要建立品牌信任的官方账号。",
                "bullets": [
                    "官方认证徽章，信任度高",
                    "搜索排名更有优势",
                    "支持企业信息展示",
                    "价格较高，适合核心账号",
                ],
            },
        ],
    },
]
