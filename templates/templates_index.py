# templates/templates_index.py
# Homepage — animated, dynamic, interactive

from .templates_base import styles_css


def render_homepage(resources: list, articles: list, footer_links: dict,
                    site_name: str, bot_tg: str, admin_tg: str, tg_channel: str,
                    site_url: str, site_desc: str, year: int) -> str:

    # Resource cards
    resource_cards = ""
    for r in resources:
        icon_svg = _get_icon_svg(r.get("icon", "tool"))
        badge_html = ""
        if r.get("highlight"):
            cls = "badge-hot" if r["highlight"] == "热门" else "badge-recommend"
            badge_html = f'<span class="card-badge {cls}">{r["highlight"]}</span>'

        tags_html = "".join(f'<span class="tag">{t}</span>' for t in r.get("features", [])[:3])
        resource_cards += f"""
          <a href="/{r['id']}.html" class="resource-card observe-me">
            <div class="card-top">
              <div class="card-icon-wrap" style="background: linear-gradient(135deg, {r.get('icon_color', '#6366F1')}, {r.get('icon_color_dark', '#4F46E5')});">
                {icon_svg}
              </div>
              {badge_html}
            </div>
            <div class="card-body">
              <h3>{r['name']}</h3>
              <p class="card-tagline">{r['tagline']}</p>
              <p>{r['description'][:100]}...</p>
              <div class="card-tags">{tags_html}</div>
            </div>
            <div class="card-footer">
              <span class="card-link">
                了解更多
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </span>
              <span class="card-category">{r['category']}</span>
            </div>
          </a>"""

    # Feature cards
    feature_cards = _get_feature_cards()

    # Article cards
    article_cards = ""
    for a in articles:
        article_cards += f"""
          <a href="/{a['slug']}.html" class="article-card observe-me">
            <div class="article-meta">
              <span class="tag" style="background:rgba(99,102,241,0.1);color:#6366F1;">{a['category']}</span>
              <span class="article-read-time">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                {a['read_time']}
              </span>
            </div>
            <h3>{a['title']}</h3>
            <p>{a['tagline']}</p>
            <div class="article-arrow">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
              阅读全文
            </div>
          </a>"""

    # Ticker items
    ticker_items = [
        "TG群关键词监控", "全球接码服务", "Telegram账号", "社交媒体账号",
        "7x24 自动运行", "USDT/支付宝/微信", "永久售后支持", "API 接口支持",
        "多平台覆盖", "快速响应",
    ]
    ticker_html = "".join(f'<span>{t}</span>' for t in ticker_items)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{site_name} - 发现实用的 Telegram 工具与资源</title>
  <meta name="description" content="{site_desc}">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{site_name} - 发现实用的 Telegram 工具与资源">
  <meta property="og:description" content="{site_desc}">
  <meta property="og:url" content="{site_url}/">
  <meta property="og:site_name" content="{site_name}">
  <meta property="og:locale" content="zh_CN">
  <meta property="og:image" content="{site_url}/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{site_name} - 发现实用的 Telegram 工具与资源">
  <meta name="twitter:description" content="{site_desc}">

  <link rel="stylesheet" href="/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <meta name="theme-color" content="#6366F1">

  <style>
  /* Article cards */
  .article-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }}
  .article-card {{
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 18px;
    padding: 1.75rem;
    text-decoration: none;
    color: inherit;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
  }}
  .article-card:hover {{
    background: rgba(255,255,255,0.08);
    border-color: rgba(99,102,241,0.4);
    transform: translateY(-4px);
  }}
  .article-meta {{ display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem; }}
  .article-read-time {{ font-size: 0.75rem; color: rgba(255,255,255,0.4); display: flex; align-items: center; gap: 0.25rem; }}
  .article-card h3 {{ font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem; color: white; }}
  .article-card p {{ font-size: 0.85rem; color: rgba(255,255,255,0.6); flex: 1; margin-bottom: 1.25rem; }}
  .article-arrow {{ display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: #6366F1; font-weight: 500; }}
  .article-card:hover .article-arrow {{ gap: 0.75rem; }}
  /* Comparison table */
  .comparison-table-wrap {{ overflow-x: auto; border-radius: 16px; border: 1px solid var(--gray-200); }}
  .comparison-table {{ width: 100%; border-collapse: collapse; background: white; font-size: 0.875rem; }}
  .comparison-table th {{ background: var(--gray-50); padding: 0.875rem 1rem; text-align: left; font-weight: 600; color: var(--gray-700); border-bottom: 2px solid var(--gray-200); white-space: nowrap; }}
  .comparison-table td {{ padding: 0.875rem 1rem; border-bottom: 1px solid var(--gray-100); vertical-align: middle; }}
  .comparison-table tr:last-child td {{ border-bottom: none; }}
  .comparison-table tr:hover td {{ background: var(--gray-50); }}
  .comparison-table td:first-child {{ font-weight: 600; color: var(--primary); }}
  .comparison-table td:last-child {{ text-align: center; }}
  .comparison-table a {{ color: var(--primary); text-decoration: none; font-weight: 500; }}
  .comparison-table a:hover {{ text-decoration: underline; }}
  /* Section dark variant */
  .section-dark {{ background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%); }}
  .section-dark .section-title {{ color: white; }}
  .section-dark .section-desc {{ color: rgba(255,255,255,0.6); }}
  /* Testimonials */
  .testimonial-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; }}
  .testimonial-card {{ background: white; border: 1px solid var(--gray-200); border-radius: 16px; padding: 1.5rem; }}
  .testimonial-stars {{ color: #FBBF24; font-size: 0.9rem; margin-bottom: 0.75rem; letter-spacing: 2px; }}
  .testimonial-text {{ font-size: 0.9rem; color: var(--gray-700); line-height: 1.7; margin-bottom: 1rem; }}
  .testimonial-author {{ font-size: 0.8rem; font-weight: 600; color: var(--gray-500); }}
  /* Trust bar */
  .trust-bar {{ display: flex; gap: 2rem; flex-wrap: wrap; }}
  .trust-item {{ display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: rgba(255,255,255,0.6); }}
  .trust-item svg {{ flex-shrink: 0; }}
  </style>
</head>
<body>
  <nav class="navbar" id="navbar" role="navigation" aria-label="主导航">
    <div class="container nav-inner">
      <a href="/" class="nav-logo" aria-label="{site_name} 首页">
        <svg width="28" height="28" viewBox="0 0 32 32" fill="none" aria-hidden="true">
          <circle cx="16" cy="16" r="16" fill="#6366F1"/>
          <path d="M16 6C10.48 6 6 10.48 6 16s4.48 10 10 10 10-4.48 10-10S21.52 6 16 6zm-1 15h2v2h-2v-2zm0-12h2v10h-2V9z" fill="white"/>
        </svg>
        {site_name}
        <span class="nav-logo-dot" aria-hidden="true"></span>
      </a>
      <button class="nav-toggle" id="navToggle" aria-label="打开菜单" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks" role="menubar">
        <li role="none"><a href="/" class="active" role="menuitem">首页</a></li>
        <li role="none"><a href="/tg-monitor.html" role="menuitem">Telegram工具</a></li>
        <li role="none"><a href="/sms-verification.html" role="menuitem">接码服务</a></li>
        <li role="none"><a href="/tg-accounts.html" role="menuitem">账号资源</a></li>
        <li role="none"><a href="/about.html" role="menuitem">关于</a></li>
        <li role="none"><a href="/guide.html" role="menuitem">使用指南</a></li>
        <li role="none">
          <a href="{bot_tg}" class="btn-tg-nav" role="menuitem" target="_blank" rel="noopener" aria-label="通过 Telegram 机器人使用工具">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
            使用工具
          </a>
        </li>
      </ul>
    </div>
  </nav>

  <main id="main-content">
    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-bg" aria-hidden="true">
        <div class="hero-grid"></div>
        <div class="hero-orb hero-orb-1"></div>
        <div class="hero-orb hero-orb-2"></div>
        <div class="hero-orb hero-orb-3"></div>
      </div>

      <div class="container" style="position:relative;z-index:2;">
        <div style="display:grid;grid-template-columns:1fr auto;gap:3rem;align-items:center;">
          <div class="hero-content">
            <div class="hero-badge" role="note">
              <span class="hero-badge-dot" aria-hidden="true"></span>
              Telegram 实用工具集
            </div>
            <h1 id="hero-title">
              发现实用的 Telegram 工具<br>
              <span class="gradient-text">让社群运营更高效</span>
            </h1>
            <p>收录 TG群关键词监控、全球手机验证码、多平台社交账号等实用工具。透明定价，永久售后，让你的 Telegram 业务事半功倍。</p>
            <div class="trust-bar" style="margin-top:1rem;" aria-label="服务保障">
              <div class="trust-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
                永久售后
              </div>
              <div class="trust-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
                7x24 运行
              </div>
              <div class="trust-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
                USDT/支付宝/微信
              </div>
            </div>
            <div class="hero-actions">
              <a href="{bot_tg}" class="btn-primary" target="_blank" rel="noopener">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                立即使用 @sosojsbot
              </a>
              <a href="/guide.html" class="btn-secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                使用指南
              </a>
            </div>
            <div class="hero-stats" aria-label="数据统计">
              <div class="hero-stat">
                <h3><span data-count="500" data-suffix="+">0</span><span class="unit">+</span></h3>
                <p>服务用户</p>
              </div>
              <div class="hero-stat">
                <h3><span data-count="99" data-suffix=".9%">0</span></h3>
                <p>运行稳定性</p>
              </div>
              <div class="hero-stat">
                <h3><span data-count="24" data-suffix="h">0</span></h3>
                <p>在线支持</p>
              </div>
              <div class="hero-stat">
                <h3><span data-count="9" data-suffix="+">0</span></h3>
                <p>实用工具</p>
              </div>
            </div>
          </div>

          <div class="hero-shapes" aria-hidden="true">
            <div class="shape-card">
              <div class="shape-card-inner">
                <div class="shape-icon" style="background:rgba(99,102,241,0.2);">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#818CF8" stroke-width="2" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                </div>
                <div>
                  <h4>群监控</h4>
                  <p>实时关键词推送</p>
                </div>
              </div>
            </div>
            <div class="shape-card">
              <div class="shape-card-inner">
                <div class="shape-icon" style="background:rgba(6,214,160,0.2);">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                </div>
                <div>
                  <h4>全球接码</h4>
                  <p>200+国家覆盖</p>
                </div>
              </div>
            </div>
            <div class="shape-card">
              <div class="shape-card-inner">
                <div class="shape-icon" style="background:rgba(255,107,107,0.2);">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#FF6B6B" stroke-width="2" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                </div>
                <div>
                  <h4>账号资源</h4>
                  <p>多类型TG账号</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="ticker-wrap" aria-hidden="true">
      <div class="ticker">
        <div style="display:flex;">{ticker_html}{ticker_html}</div>
      </div>
    </div>

    <section class="section" id="tools" aria-labelledby="tools-title">
      <div class="container">
        <div class="section-header">
          <div class="section-label">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            精选资源
          </div>
          <h2 class="section-title" id="tools-title">实用的 Telegram 工具集</h2>
          <p class="section-desc">持续收录优质工具，覆盖社群运营的各个环节</p>
        </div>
        <div class="resource-grid">
          {resource_cards}
        </div>
      </div>
    </section>

    <section class="section section-dark" aria-labelledby="articles-title">
      <div class="container">
        <div class="section-header">
          <div class="section-label">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
            运营攻略
          </div>
          <h2 class="section-title" id="articles-title">Telegram 运营实战指南</h2>
          <p class="section-desc">从账号准备到自动化运营的完整攻略</p>
        </div>
        <div class="article-grid">
          {article_cards}
        </div>
      </div>
    </section>

    <section class="section section-gray" aria-labelledby="features-title">
      <div class="container">
        <div class="section-header">
          <div class="section-label">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
            核心优势
          </div>
          <h2 class="section-title" id="features-title">为什么选择我们</h2>
          <p class="section-desc">稳定、透明、可靠</p>
        </div>
        <div class="feature-grid">
          {feature_cards}
        </div>
      </div>
    </section>

    <section class="section section-gray" aria-labelledby="testimonials-title">
      <div class="container">
        <div class="section-header">
          <div class="section-label">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            用户评价
          </div>
          <h2 class="section-title" id="testimonials-title">用户怎么说</h2>
          <p class="section-desc">真实用户反馈</p>
        </div>
        <div class="testimonial-grid">
          <article class="testimonial-card observe-me">
            <div class="testimonial-stars" aria-label="5星评价">★★★★★</div>
            <p class="testimonial-text">"TG群监控帮我第一时间发现竞品动态，设置好关键词后基本不用管，消息推送很及时。配合接码服务，账号矩阵搭建效率高了很多。"</p>
            <div class="testimonial-author">— 跨境电商运营 李先生</div>
          </article>
          <article class="testimonial-card observe-me">
            <div class="testimonial-stars" aria-label="5星评价">★★★★★</div>
            <p class="testimonial-text">"接码平台用了一年多了，覆盖国家多，成功率高。API 接口对接自动化脚本后，注册效率提升了好几倍。客服响应也很快。"</p>
            <div class="testimonial-author">— 技术开发者 陈先生</div>
          </article>
          <article class="testimonial-card observe-me">
            <div class="testimonial-stars" aria-label="5星评价">★★★★★</div>
            <p class="testimonial-text">"TG账号质量很好，老号很稳，买了十几个都没出过问题。永久售后确实靠谱，中间有几次操作问题都帮我解决了。"</p>
            <div class="testimonial-author">— 社群运营 王女士</div>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="comparison-title">
      <div class="container">
        <div class="section-header">
          <div class="section-label">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            服务对比
          </div>
          <h2 class="section-title" id="comparison-title">工具服务概览</h2>
          <p class="section-desc">一站式满足你的 Telegram 运营需求</p>
        </div>
        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <caption class="sr-only">TG工具集提供的服务列表</caption>
            <thead>
              <tr>
                <th scope="col">服务</th>
                <th scope="col">功能亮点</th>
                <th scope="col">适用场景</th>
                <th scope="col">获取方式</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><a href="/tg-monitor.html">TG群关键词监控</a></td>
                <td>实时关键词推送、多账号监听、自动转发</td>
                <td>社群运营、市场情报、竞品分析</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/sms-verification.html">全球手机验证码</a></td>
                <td>200+国家、50+平台、秒级接收</td>
                <td>批量注册、账号矩阵、跨境业务</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/tg-accounts.html">Telegram账号</a></td>
                <td>新号/老号/靓号/企业号、永久售后</td>
                <td>账号运营、品牌推广、社群营销</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/social-accounts.html">社交媒体账号</a></td>
                <td>WhatsApp/IG/FB/X 多平台覆盖</td>
                <td>跨境电商、社媒营销、多平台矩阵</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/proxy-services.html">代理IP服务</a></td>
                <td>100+国家住宅IP、独享带宽、99.9%在线率</td>
                <td>账号防关联、数据采集、广告验证</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/tg-api.html">TG Bot开发</a></td>
                <td>Python/Node.js、私有化/云端托管</td>
                <td>定制机器人、自动化系统、数据对接</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/data-tools.html">数据采集工具</a></td>
                <td>成员采集、消息导出、数据清洗</td>
                <td>市场分析、竞品调研、用户画像</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/automation.html">自动化运营</a></td>
                <td>多账号管理、自动发帖、批量私信</td>
                <td>账号矩阵、批量运营、社群管理</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
              <tr>
                <td><a href="/membership.html">会员服务</a></td>
                <td>全站8折、优先客服、API升级</td>
                <td>长期用户、多服务重度使用者</td>
                <td><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="cta-section" aria-labelledby="cta-title">
      <div class="container" style="position:relative;z-index:1;">
        <h2 id="cta-title">开始使用 TG工具集</h2>
        <p>通过 Telegram 机器人快速开始，或联系 {admin_tg} 获取帮助</p>
        <div class="cta-actions">
          <a href="{bot_tg}" class="btn-primary" target="_blank" rel="noopener">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
            打开 @sosojsbot
          </a>
          <a href="{tg_channel}" class="btn-secondary" target="_blank" rel="noopener">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            加入 @TGNICETOP
          </a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/" class="nav-logo" style="font-size:1rem;">
            <svg width="26" height="26" viewBox="0 0 32 32" fill="none" aria-hidden="true"><circle cx="16" cy="16" r="16" fill="#6366F1"/><path d="M16 6C10.48 6 6 10.48 6 16s4.48 10 10 10 10-4.48 10-10S21.52 6 16 6zm-1 15h2v2h-2v-2zm0-12h2v10h-2V9z" fill="white"/></svg>
            {site_name}
          </a>
          <p>发现实用的 Telegram 工具与资源，让社群运营更高效</p>
        </div>
        <div>
          <h4>工具</h4>
          <ul>
            <li><a href="/tg-monitor.html">TG群监控</a></li>
            <li><a href="/sms-verification.html">全球接码</a></li>
            <li><a href="/tg-accounts.html">TG账号</a></li>
            <li><a href="/social-accounts.html">社媒账号</a></li>
          </ul>
        </div>
        <div>
          <h4>资源</h4>
          <ul>
            <li><a href="/about.html">关于我们</a></li>
            <li><a href="/guide.html">使用指南</a></li>
            <li><a href="/faq.html">常见问题</a></li>
          </ul>
        </div>
        <div>
          <h4>链接</h4>
          <ul>
            <li><a href="https://tgnice.top" target="_blank" rel="noopener">tgnice.top</a></li>
            <li><a href="{bot_tg}" target="_blank" rel="noopener">@sosojsbot</a></li>
            <li><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; {year} {site_name}. All rights reserved.</p>
        <p>Powered by GitHub Pages</p>
      </div>
    </div>
  </footer>

  <script src="/assets/main.js" defer></script>
</body>
</html>"""


def _get_feature_cards() -> str:
    cards = [
        ("#6366F1", "rgba(99,102,241,0.1)",
         '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#6366F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
         "安全可靠", "全站数据加密，隐私保护，遵守平台规则"),
        ("#06D6A0", "rgba(6,214,160,0.1)",
         '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
         "极速稳定", "7x24 自动运行，全球 CDN 加速，毫秒级响应"),
        ("#FF6B6B", "rgba(255,107,107,0.1)",
         '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF6B6B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
         "全天候客服", "24小时在线，联系 @TGNICETOP 快速响应"),
        ("#FBBF24", "rgba(251,191,36,0.1)",
         '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FBBF24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
         "透明定价", "明码标价，无隐藏费用，USDT/支付宝/微信"),
        ("#8B5CF6", "rgba(139,92,246,0.1)",
         '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
         "管理后台", "简洁易用的 Web 面板，实时查看数据配置"),
        ("#06B2D6", "rgba(6,178,214,0.1)",
         '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#06B2D6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
         "API 接口", "完整 REST API，无缝对接现有系统"),
    ]
    html = ""
    for color, bg, icon, title, desc in cards:
        html += f"""
          <div class="feature-card observe-me">
            <div class="feature-icon" style="background:{bg};">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>"""
    return html


# ── Icon map ─────────────────────────────────
_ICON_SVG_MAP = {
    "monitor": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    "message": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "user": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "globe": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    "star": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    "tool": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    "shield": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "code": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "database": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    "zap": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
}


def _get_icon_svg(icon_name: str) -> str:
    return _ICON_SVG_MAP.get(icon_name, _ICON_SVG_MAP["tool"])


# ── Inner page templates ───────────────────────────────────────────────

def render_about(about_content: dict, footer_links: dict,
                 site_name: str, bot_tg: str, admin_tg: str, tg_channel: str,
                 site_url: str, year: int) -> str:

    values_html = "".join(
        f'<div class="value-card observe-me"><h4>{n}</h4><p>{d}</p></div>'
        for n, d in about_content.get("values", [])
    )
    stats_html = "".join(
        f'<div class="stat-card-dark"><h3>{v}</h3><p>{l}</p></div>'
        for v, l in about_content.get("stats", [])
    )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>关于 - {site_name}</title>
  <meta name="description" content="了解 {site_name}，专注于 Telegram 生态的实用工具与资源导航平台。">
  <meta name="robots" content="index, follow">
  <link rel="stylesheet" href="/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <meta name="theme-color" content="#6366F1">
  <style>
  .stat-card-dark {{ background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); border-radius: 14px; padding: 1.5rem; text-align: center; }}
  .stat-card-dark h3 {{ font-size: 1.75rem; font-weight: 800; color: white; margin-bottom: 0.25rem; }}
  .stat-card-dark p {{ font-size: 0.8rem; color: rgba(255,255,255,0.7); }}
  .sr-only {{ position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }}
  </style>
</head>
<body>
  <nav class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="/" class="nav-logo">{site_name}<span class="nav-logo-dot" aria-hidden="true"></span></a>
      <button class="nav-toggle" id="navToggle" aria-label="菜单"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/">首页</a></li>
        <li><a href="/tg-monitor.html">Telegram工具</a></li>
        <li><a href="/sms-verification.html">接码服务</a></li>
        <li><a href="/tg-accounts.html">账号资源</a></li>
        <li><a href="/about.html" class="active">关于</a></li>
        <li><a href="/guide.html">使用指南</a></li>
        <li><a href="{bot_tg}" class="btn-tg-nav" target="_blank" rel="noopener">使用工具</a></li>
      </ul>
    </div>
  </nav>
  <main id="main-content">
    <section class="page-header">
      <div class="container">
        <nav class="breadcrumb" aria-label="面包屑"><a href="/">首页</a><span>/</span><span>关于</span></nav>
        <h1>关于 {site_name}</h1>
        <p>专注于 Telegram 生态的资源导航平台</p>
      </div>
    </section>
    <section class="section section-sm">
      <div class="container">
        <div class="about-content">
          <p>{about_content['intro']}</p>
          <p style="font-weight:600;color:var(--gray-800);">{about_content['mission']}</p>
          <div style="margin-top:2.5rem;">
            <h2 style="font-size:1.2rem;font-weight:700;color:var(--gray-900);margin-bottom:1.25rem;">我们的理念</h2>
            <div class="values-grid">{values_html}</div>
          </div>
          <div style="margin-top:2.5rem;">
            <h2 style="font-size:1.2rem;font-weight:700;color:var(--gray-900);margin-bottom:1.25rem;">数据一览</h2>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;">{stats_html}</div>
          </div>
        </div>
      </div>
    </section>
    <section class="cta-section">
      <div class="container">
        <h2>有疑问？联系我们</h2>
        <p>直接通过 Telegram 联系 {admin_tg}</p>
        <div class="cta-actions">
          <a href="{bot_tg}" class="btn-primary" target="_blank" rel="noopener">使用工具</a>
          <a href="{tg_channel}" class="btn-secondary" target="_blank" rel="noopener">加入 @TGNICETOP</a>
        </div>
      </div>
    </section>
  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer-bottom" style="border-top:none;padding-top:0;">
        <p>&copy; {year} {site_name}. All rights reserved.</p>
        <p>Powered by GitHub Pages</p>
      </div>
    </div>
  </footer>
  <script src="/assets/main.js" defer></script>
</body>
</html>"""


def render_guide(resources: list, footer_links: dict,
                 site_name: str, bot_tg: str, admin_tg: str, tg_channel: str,
                 site_url: str, year: int) -> str:
    sections = [
        ("第一步：通过 Telegram 联系开通",
         "所有服务均通过 Telegram 机器人 @sosojsbot 提供，无需注册网站账号。首先联系 @TGNICETOP，说明你需要使用的工具类型、使用规模和预算，客服会根据你的需求推荐最合适的方案。整个过程简单高效，通常几分钟内即可完成沟通。",
         ["说明需要使用的工具（群监控、接码、账号等）",
          "告知大致的使用规模（监听几个群、需要多少账号等）",
          "客服会给出透明报价，无任何隐藏费用",
          "确认方案后完成支付即可开通"]),
        ("第二步：完成支付",
         "支持 USDT (TRC20)、支付宝、微信支付三种方式。价格透明，按需计费，无任何隐藏手续费。支付完成后截图发给客服，客服会立即为你开通服务。",
         ["USDT (TRC20)：汇率透明，无额外手续费，推荐使用",
          "支付宝 / 微信：方便快捷，适合国内用户",
          "支持月付、季付、年付多种周期选择",
          "会员用户享受全站 8 折优惠"]),
        ("第三步：开始使用服务",
         "开通后你会收到管理后台登录信息、TG机器人使用指引，以及专属客服对接。登录后台即可开始配置使用。7x24 小时自动运行，无需额外维护。",
         ["TG群监控：配置关键词、添加监听账号、设置推送规则",
          "接码服务：选择平台和国家、获取临时号码、接收验证码",
          "账号资源：获取账号信息后直接使用",
          "遇到任何问题随时联系 @TGNICETOP"]),
        ("第四步：持续使用与售后",
         "所有服务提供永久售后支持。遇到任何问题，直接通过 Telegram 联系 @TGNICETOP 即可获得帮助。服务持续稳定运行，配备自动监控机制。",
         ["TG群监控：7x24 自动运行，关键词实时推送",
          "接码服务：号码有效期约 20 分钟，超时自动释放",
          "TG账号：每个账号建议搭配独立 IP，降低风控风险",
          "自动化运营：后台配置一次，日常自动执行"]),
        ("使用注意事项",
         "请遵守 Telegram 官方使用条款，合理使用各项服务。关键词监控依赖群组开启历史消息查看权限。TG账号请勿频繁切换设备或 IP，以免触发平台风控。",
         ["部分服务需要群组开启「保存历史消息」权限",
          "TG账号操作要自然，避免短时间内大量操作",
          "建议配合住宅代理 IP 使用账号服务",
          "永久售后保障，联系 @TGNICETOP 获取帮助"]),
    ]
    guide_html = ""
    for title, intro, bullets in sections:
        bullets_html = "".join(f"<li>{b}</li>" for b in bullets)
        guide_html += f"""
        <div class="guide-section observe-me">
          <h3>{title}</h3>
          <p>{intro}</p>
          <ul>{bullets_html}</ul>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>使用指南 - {site_name}</title>
  <meta name="description" content="{site_name} 使用指南，了解如何开始使用 TG群监控、接码服务、账号资源等工具。">
  <meta name="robots" content="index, follow">
  <link rel="stylesheet" href="/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <meta name="theme-color" content="#6366F1">
  <style>.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;}}</style>
</head>
<body>
  <nav class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="/" class="nav-logo">{site_name}<span class="nav-logo-dot" aria-hidden="true"></span></a>
      <button class="nav-toggle" id="navToggle" aria-label="菜单"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/">首页</a></li>
        <li><a href="/tg-monitor.html">Telegram工具</a></li>
        <li><a href="/sms-verification.html">接码服务</a></li>
        <li><a href="/tg-accounts.html">账号资源</a></li>
        <li><a href="/about.html">关于</a></li>
        <li><a href="/guide.html" class="active">使用指南</a></li>
        <li><a href="{bot_tg}" class="btn-tg-nav" target="_blank" rel="noopener">使用工具</a></li>
      </ul>
    </div>
  </nav>
  <main id="main-content">
    <section class="page-header">
      <div class="container">
        <nav class="breadcrumb" aria-label="面包屑"><a href="/">首页</a><span>/</span><span>使用指南</span></nav>
        <h1>使用指南</h1>
        <p>四步开始，快速上手</p>
      </div>
    </section>
    <section class="section">
      <div class="container" style="max-width:800px;">
        {guide_html}
      </div>
    </section>
  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer-bottom" style="border-top:none;padding-top:0;">
        <p>&copy; {year} {site_name}. All rights reserved.</p>
        <p>Powered by GitHub Pages</p>
      </div>
    </div>
  </footer>
  <script src="/assets/main.js" defer></script>
</body>
</html>"""


def render_faq(footer_links: dict,
               site_name: str, bot_tg: str, admin_tg: str, tg_channel: str,
               site_url: str, year: int) -> str:
    faqs = [
        ("如何开始使用 TG工具集？",
         "所有服务均通过 Telegram 提供，无需注册网站。首先联系 @TGNICETOP 说明需求，完成支付后客服立即为你开通并提供使用指引。"),
        ("支持哪些支付方式？",
         "支持 USDT (TRC20)、支付宝、微信支付。价格透明，无隐藏手续费。"),
        ("TG群关键词监控支持多少关键词？",
         "每个账号最多支持 50 个关键词同时监听，支持多账号叠加。"),
        ("接码服务支持哪些平台和国家？",
         "支持 Telegram、OpenAI、Twitter/X、Instagram、WhatsApp、Facebook 等 50+ 平台，覆盖 200+ 国家和地区。"),
        ("TG账号是全新的吗？有哪些类型？",
         "提供多种规格：全新账号（5U起）、老号（带活跃群组历史）、靓号（自定义@用户名）、企业认证号。所有账号均经检测，永久售后。"),
        ("代理IP有哪些类型？",
         "提供住宅代理和数据中心代理，覆盖 100+ 国家，支持 HTTP/SOCKS5 协议，独享 IP 不混用。"),
        ("Bot 开发需要多久交付？",
         "标准功能 3-5 个工作日交付，支持 Python / Node.js / Go，可私有化部署或云端托管。"),
        ("数据采集支持哪些格式导出？",
         "支持 Excel、CSV、JSON 三种格式导出，也可通过 API 直接对接，单次最高支持 10 万条数据。"),
        ("自动化运营可以管理多少账号？",
         "单后台支持 100+ 账号同时管理，自动发帖、批量私信、群管、报表全部涵盖。"),
        ("会员有哪些权益？",
         "全站服务 8 折、优先客服通道、批量操作权限、API 日调用量提升 5 倍、推荐奖励。"),
        ("服务稳定性如何保障？",
         "服务部署在高可用架构，7x24 小时自动运行，配备实时监控与故障自动恢复机制。"),
        ("可以先试用吗？",
         "部分服务支持试用。请联系 @TGNICETOP 申请体验，满意后再正式开通。"),
    ]
    faq_html = "".join(
        f'<div class="faq-item"><div class="faq-q">{q}<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="faq-a">{a}</div></div>'
        for q, a in faqs
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>常见问题 - {site_name}</title>
  <meta name="description" content="{site_name} 常见问题解答，关于 TG群监控、接码服务、账号资源的常见问题。">
  <meta name="robots" content="index, follow">
  <link rel="stylesheet" href="/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <meta name="theme-color" content="#6366F1">
  <style>.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;}}</style>
</head>
<body>
  <nav class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="/" class="nav-logo">{site_name}<span class="nav-logo-dot" aria-hidden="true"></span></a>
      <button class="nav-toggle" id="navToggle" aria-label="菜单"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/">首页</a></li>
        <li><a href="/tg-monitor.html">Telegram工具</a></li>
        <li><a href="/sms-verification.html">接码服务</a></li>
        <li><a href="/tg-accounts.html">账号资源</a></li>
        <li><a href="/about.html">关于</a></li>
        <li><a href="/guide.html">使用指南</a></li>
        <li><a href="{bot_tg}" class="btn-tg-nav" target="_blank" rel="noopener">使用工具</a></li>
      </ul>
    </div>
  </nav>
  <main id="main-content">
    <section class="page-header">
      <div class="container">
        <nav class="breadcrumb" aria-label="面包屑"><a href="/">首页</a><span>/</span><span>常见问题</span></nav>
        <h1>常见问题</h1>
        <p>快速找到你关心的问题答案</p>
      </div>
    </section>
    <section class="section">
      <div class="container" style="max-width:720px;">
        <div style="border:1px solid var(--gray-200);border-radius:18px;background:white;padding:1.5rem;">
          {faq_html}
        </div>
        <div style="margin-top:2rem;text-align:center;padding:2rem;background:var(--gray-50);border-radius:16px;border:1px solid var(--gray-200);">
          <h3 style="font-size:1.1rem;font-weight:700;color:var(--gray-900);margin-bottom:0.5rem;">还有其他问题？</h3>
          <p style="font-size:0.9rem;color:var(--gray-600);margin-bottom:1rem;">直接联系我们</p>
          <a href="{tg_channel}" class="btn-primary" target="_blank" rel="noopener" style="display:inline-flex;">联系 @TGNICETOP</a>
        </div>
      </div>
    </section>
  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer-bottom" style="border-top:none;padding-top:0;">
        <p>&copy; {year} {site_name}. All rights reserved.</p>
        <p>Powered by GitHub Pages</p>
      </div>
    </div>
  </footer>
  <script src="/assets/main.js" defer></script>
</body>
</html>"""


def render_article(article: dict, all_articles: list, footer_links: dict,
                    site_name: str, site_url: str, bot_tg: str, admin_tg: str,
                    tg_channel: str, year: int) -> str:
    sections_html = ""
    for section in article.get("sections", []):
        bullets_html = "".join(f"<li>{b}</li>" for b in section.get("bullets", []))
        sections_html += f"""
        <div class="guide-section observe-me">
          <h2>{section['title']}</h2>
          <p>{section['content']}</p>
          <ul>{bullets_html}</ul>
        </div>"""

    related = [a for a in all_articles if a["id"] != article["id"]][:3]
    related_html = ""
    if related:
        related_html = "<div class='related-articles'><h3>相关阅读</h3><div class='related-grid'>"
        for ra in related:
            related_html += f"""
            <a href="/{ra['slug']}.html" class="related-card">
              <span class="tag" style="font-size:0.7rem;">{ra['category']}</span>
              <h4>{ra['title']}</h4>
              <span style="font-size:0.8rem;color:var(--gray-500);">{ra['read_time']}</span>
            </a>"""
        related_html += "</div></div>"

    article_url = f"{site_url}/{article['slug']}.html"
    page_title = f"{article['title']} - {site_name}"
    page_desc = article["description"][:160]

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="{page_desc}">
  <meta name="robots" content="index, follow, max-snippet:-1">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{article['tagline']}">
  <meta property="og:url" content="{article_url}">
  <meta property="og:site_name" content="{site_name}">
  <link rel="stylesheet" href="/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <meta name="theme-color" content="#6366F1">
  <style>
  .related-articles {{ margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--gray-200); }}
  .related-articles h3 {{ font-size: 1.1rem; font-weight: 700; margin-bottom: 1rem; color: var(--gray-900); }}
  .related-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1rem; }}
  .related-card {{ display: flex; flex-direction: column; gap: 0.4rem; padding: 1rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: 12px; text-decoration: none; color: inherit; transition: all 0.2s; }}
  .related-card:hover {{ border-color: var(--primary); background: rgba(99,102,241,0.04); }}
  .related-card h4 {{ font-size: 0.9rem; font-weight: 600; color: var(--gray-900); margin: 0; }}
  .article-header-meta {{ display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }}
  .sr-only {{ position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }}
  </style>
</head>
<body>
  <nav class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="/" class="nav-logo">{site_name}<span class="nav-logo-dot" aria-hidden="true"></span></a>
      <button class="nav-toggle" id="navToggle" aria-label="菜单"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/">首页</a></li>
        <li><a href="/tg-monitor.html">Telegram工具</a></li>
        <li><a href="/sms-verification.html">接码服务</a></li>
        <li><a href="/tg-accounts.html">账号资源</a></li>
        <li><a href="/about.html">关于</a></li>
        <li><a href="{bot_tg}" class="btn-tg-nav" target="_blank" rel="noopener">使用工具</a></li>
      </ul>
    </div>
  </nav>
  <main id="main-content">
    <section class="page-header">
      <div class="container">
        <nav class="breadcrumb" aria-label="面包屑">
          <a href="/">首页</a><span>/</span>
          <a href="/guide.html">使用指南</a><span>/</span>
          <span>{article['category']}</span>
        </nav>
        <div class="article-header-meta">
          <span class="tag" style="background:rgba(99,102,241,0.2);color:white;">{article['category']}</span>
          <span style="font-size:0.85rem;color:rgba(255,255,255,0.6);">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;margin-right:3px;" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            {article['read_time']}
          </span>
        </div>
        <h1>{article['title']}</h1>
        <p>{article['tagline']}</p>
      </div>
    </section>
    <section class="section">
      <div class="container" style="max-width:800px;">
        {sections_html}
        {related_html}
      </div>
    </section>
  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer-bottom" style="border-top:none;padding-top:0;">
        <p>&copy; {year} {site_name}. All rights reserved.</p>
        <p>Powered by GitHub Pages</p>
      </div>
    </div>
  </footer>
  <script src="/assets/main.js" defer></script>
</body>
</html>"""
