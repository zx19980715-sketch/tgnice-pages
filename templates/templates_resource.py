# templates/templates_resource.py
# Resource detail page — dark header, rich content, sidebar, interactive


_ICON_SVG_MAP = {
    "monitor": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    "message": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "user": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "globe": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    "star": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    "tool": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    "shield": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "code": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "database": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    "zap": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
}

_ICON_COLORS = {
    "monitor": ("#6366F1", "#4F46E5"),
    "message": ("#06D6A0", "#059669"),
    "user": ("#FF6B6B", "#DC2626"),
    "globe": ("#FBBF24", "#D97706"),
    "star": ("#8B5CF6", "#7C3AED"),
    "tool": ("#06B2D6", "#0891B2"),
    "shield": ("#0EA5E9", "#0284C7"),
    "code": ("#14B8A6", "#0D9488"),
    "database": ("#EC4899", "#DB2777"),
    "zap": ("#F59E0B", "#D97706"),
}


def render_resource(resource, all_resources, footer_links,
                   site_name, site_url, bot_tg, admin_tg, tg_channel, year):
    icon_name = resource.get("icon", "tool")
    icon_svg = _ICON_SVG_MAP.get(icon_name, _ICON_SVG_MAP["tool"])
    icon_color = _ICON_COLORS.get(icon_name, ("#6366F1", "#4F46E5"))

    # Related resources
    related = [r for r in all_resources if r["id"] in resource.get("related", [])]
    related_html = ""
    for r in related:
        r_icon = _ICON_SVG_MAP.get(r.get("icon", "tool"))
        related_html += (
            '<a href="/' + r["id"] + '.html" class="related-card">'
            '<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem;">'
            '<div style="width:32px;height:32px;border-radius:8px;background:rgba(99,102,241,0.1);display:flex;align-items:center;justify-content:center;flex-shrink:0;">' + r_icon + '</div>'
            '<h4>' + r["name"] + '</h4></div>'
            '<p>' + r["tagline"] + '</p></a>'
        )

    # Steps
    steps_html = ""
    for i, step in enumerate(resource.get("how_to_use", []), 1):
        steps_html += (
            '<div class="step-item">'
            '<div class="step-num">' + str(i) + '</div>'
            '<div class="step-content"><h4>第 ' + str(i) + ' 步</h4><p>' + step + '</p></div>'
            '</div>'
        )

    # Features
    features_html = ""
    for feat in resource.get("features", []):
        features_html += (
            '<div class="feature-item">'
            '<div class="feature-check"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></div>'
            '<div><h4>' + feat + '</h4></div>'
            '</div>'
        )

    # Specs table
    specs_html = ""
    if resource.get("specs"):
        rows = ""
        for label, value in resource.get("specs", []):
            rows += ("<tr><td style='font-weight:600;color:var(--gray-600);"
                     "padding:0.6rem 1rem;font-size:0.875rem;background:var(--gray-50);"
                     "border-bottom:1px solid var(--gray-100);'>" + label +
                     "</td><td style='padding:0.6rem 1rem;font-size:0.875rem;"
                     "border-bottom:1px solid var(--gray-100);'>" + value + "</td></tr>")
        specs_html = (
            '<div style="margin-bottom:2.5rem;">'
            '<h2 style="font-size:1.25rem;font-weight:700;color:var(--gray-900);'
            'margin-bottom:1.25rem;padding-bottom:0.75rem;border-bottom:1px solid var(--gray-200);">'
            '服务参数</h2>'
            '<table style="width:100%;border-collapse:collapse;background:white;'
            'border:1px solid var(--gray-200);border-radius:12px;overflow:hidden;">'
            '<tbody>' + rows + '</tbody></table></div>'
        )

    highlight_tag = ""
    if resource.get("highlight"):
        highlight_tag = ('<span class="tool-badge" style="background:rgba(255,107,107,0.15);'
                        'color:#FF6B6B;border-color:rgba(255,107,107,0.3);">'
                        + resource["highlight"] + '</span>')

    related_section = ""
    if related:
        related_section = (
            '<div class="sidebar-card" style="background:rgba(255,255,255,0.03);margin-top:1rem;">'
            '<h3>相关资源</h3>'
            '<div style="display:flex;flex-direction:column;gap:0.75rem;margin-top:0.75rem;">'
            + related_html + '</div></div>'
        )

    tg_icon_svg = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" '
                    'aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 '
                    '12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.'
                    '321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.'
                    '36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.'
                    '124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.'
                    '014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.'
                    '49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.'
                    '325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.'
                    '635z"/></svg>')

    # SEO
    page_url = f"{site_url}/{resource['id']}.html"
    page_title = f"{resource['name']} - {site_name}"
    page_desc = resource["description"][:160]

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="{page_desc}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
  <meta name="google-site-verification" content="GhbpcdX0oAktg3z_tgn4-zP7m-cY2dUjOIfheK8xSHw">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{page_desc}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:site_name" content="{site_name}">
  <meta property="og:locale" content="zh_CN">

  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{page_title}">
  <meta name="twitter:description" content="{page_desc}">

  <link rel="stylesheet" href="/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <meta name="theme-color" content="{icon_color[0]}">

  <style>
  .sr-only {{ position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }}
  </style>
</head>
<body>
  <nav class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="/" class="nav-logo">
        <svg width="28" height="28" viewBox="0 0 32 32" fill="none" aria-hidden="true">
          <circle cx="16" cy="16" r="16" fill="#6366F1"/>
          <path d="M16 6C10.48 6 6 10.48 6 16s4.48 10 10 10 10-4.48 10-10S21.52 6 16 6zm-1 15h2v2h-2v-2zm0-12h2v10h-2V9z" fill="white"/>
        </svg>
        {site_name}
        <span class="nav-logo-dot" aria-hidden="true"></span>
      </a>
      <button class="nav-toggle" id="navToggle" aria-label="菜单"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/">首页</a></li>
        <li><a href="/tg-monitor.html">Telegram工具</a></li>
        <li><a href="/sms-verification.html">接码服务</a></li>
        <li><a href="/tg-accounts.html">账号资源</a></li>
        <li><a href="/about.html">关于</a></li>
        <li><a href="/guide.html">使用指南</a></li>
        <li><a href="{bot_tg}" class="btn-tg-nav" target="_blank" rel="noopener">{tg_icon_svg}使用工具</a></li>
      </ul>
    </div>
  </nav>

  <main id="main-content">
    <section class="tool-header">
      <div class="container" style="position:relative;z-index:1;">
        <nav class="breadcrumb" aria-label="面包屑">
          <a href="/">首页</a><span>/</span>
          <span>{resource["category"]}</span>
        </nav>
        <div class="tool-header-inner">
          <div style="width:72px;height:72px;border-radius:20px;background:linear-gradient(135deg,{icon_color[0]},{icon_color[1]});display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 12px 40px {icon_color[0]}40;">
            {icon_svg}
          </div>
          <div>
            <div style="display:flex;gap:0.5rem;align-items:center;margin-bottom:0.75rem;flex-wrap:wrap;">
              <span class="tool-badge">{resource["category"]}</span>
              {highlight_tag}
            </div>
            <h1>{resource["name"]}</h1>
            <p class="subtitle">{resource["tagline"]}</p>
            <p class="description">{resource["description"]}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr 300px;gap:3rem;align-items:start;">
          <div>
            <div style="margin-bottom:2.5rem;">
              <h2 style="font-size:1.25rem;font-weight:700;color:var(--gray-900);margin-bottom:1.25rem;padding-bottom:0.75rem;border-bottom:1px solid var(--gray-200);">功能特点</h2>
              <div class="features-list">{features_html}</div>
            </div>
            {specs_html}
            <div style="margin-bottom:2.5rem;">
              <h2 style="font-size:1.25rem;font-weight:700;color:var(--gray-900);margin-bottom:1.25rem;padding-bottom:0.75rem;border-bottom:1px solid var(--gray-200);">使用步骤</h2>
              <div class="step-list">{steps_html}</div>
            </div>
            <div>
              <h2 style="font-size:1.25rem;font-weight:700;color:var(--gray-900);margin-bottom:1.25rem;padding-bottom:0.75rem;border-bottom:1px solid var(--gray-200);">常见问题</h2>
              <div>
                <div class="faq-item"><div class="faq-q">这个服务支持哪些功能？<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="faq-a">{resource.get("description", "请联系 @TGNICETOP 获取详细功能说明。")}</div></div>
                <div class="faq-item"><div class="faq-q">如何开始使用？<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="faq-a">联系 @TGNICETOP 说明需求，完成支付后即可开通。开通后客服会发送详细使用指引。</div></div>
                <div class="faq-item"><div class="faq-q">支持哪些支付方式？<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="faq-a">支持 USDT (TRC20)、支付宝、微信支付。价格透明，无额外手续费。</div></div>
                <div class="faq-item"><div class="faq-q">可以试用吗？<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="faq-a">部分服务支持试用，联系 @TGNICETOP 申请体验。</div></div>
                <div class="faq-item"><div class="faq-q">服务稳定吗？<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="faq-a">服务部署在高可用架构上，7x24 小时自动运行，配备实时监控与故障自动恢复机制。</div></div>
                <div class="faq-item"><div class="faq-q">有售后保障吗？<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="faq-a">所有服务提供永久售后支持。遇到任何问题，直接联系 @TGNICETOP 即可获得帮助。</div></div>
              </div>
            </div>
          </div>
          <div style="position:sticky;top:90px;">
            <div class="sidebar-card">
              <h3>快速开始</h3>
              <div style="display:flex;flex-direction:column;gap:0.6rem;">
                <a href="{bot_tg}" class="btn-primary" style="justify-content:center;" target="_blank" rel="noopener">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                  立即使用 @sosojsbot
                </a>
                <a href="{tg_channel}" class="btn-secondary" style="justify-content:center;border-color:rgba(255,255,255,0.15);" target="_blank" rel="noopener">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                  联系 @TGNICETOP
                </a>
              </div>
              <div style="margin-top:1rem;padding-top:1rem;border-top:1px solid rgba(255,255,255,0.08);display:flex;flex-direction:column;gap:0.5rem;">
                <div style="display:flex;align-items:center;gap:0.5rem;font-size:0.8rem;color:rgba(255,255,255,0.5);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>7x24 自动运行</div>
                <div style="display:flex;align-items:center;gap:0.5rem;font-size:0.8rem;color:rgba(255,255,255,0.5);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>永久售后支持</div>
                <div style="display:flex;align-items:center;gap:0.5rem;font-size:0.8rem;color:rgba(255,255,255,0.5);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#06D6A0" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>USDT / 支付宝 / 微信</div>
              </div>
            </div>
            {related_section}
          </div>
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="container" style="position:relative;z-index:1;">
        <h2>开始使用 {resource["name"]}</h2>
        <p>通过 Telegram 机器人快速开通，或联系 @TGNICETOP 获取更多帮助</p>
        <div class="cta-actions">
          <a href="{bot_tg}" class="btn-primary" target="_blank" rel="noopener">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
            打开 @sosojsbot
          </a>
          <a href="{tg_channel}" class="btn-secondary" target="_blank" rel="noopener">加入 @TGNICETOP</a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/" class="nav-logo" style="font-size:1rem;color:white;">
            <svg width="26" height="26" viewBox="0 0 32 32" fill="none" aria-hidden="true"><circle cx="16" cy="16" r="16" fill="#6366F1"/><path d="M16 6C10.48 6 6 10.48 6 16s4.48 10 10 10 10-4.48 10-10S21.52 6 16 6zm-1 15h2v2h-2v-2zm0-12h2v10h-2V9z" fill="white"/></svg>
            {site_name}
          </a>
          <p>发现实用的 Telegram 工具与资源，让社群运营更高效</p>
        </div>
        <div><h4>工具</h4><ul>
          <li><a href="/tg-monitor.html">TG群关键词监控</a></li>
          <li><a href="/sms-verification.html">全球接码</a></li>
          <li><a href="/tg-accounts.html">TG账号</a></li>
          <li><a href="/social-accounts.html">社媒账号</a></li>
          <li><a href="/proxy-services.html">代理IP服务</a></li>
          <li><a href="/tg-api.html">Bot开发</a></li>
          <li><a href="/data-tools.html">数据采集</a></li>
          <li><a href="/automation.html">自动化运营</a></li>
        </ul></div>
        <div><h4>资源</h4><ul>
          <li><a href="/about.html">关于我们</a></li>
          <li><a href="/guide.html">使用指南</a></li>
          <li><a href="/guide-telegram-marketing.html">运营攻略</a></li>
          <li><a href="/faq.html">常见问题</a></li>
          <li><a href="/membership.html">会员服务</a></li>
        </ul></div>
        <div><h4>链接</h4><ul>
          <li><a href="https://tgnice.top" target="_blank" rel="noopener">tgnice.top</a></li>
          <li><a href="{bot_tg}" target="_blank" rel="noopener">@sosojsbot</a></li>
          <li><a href="{tg_channel}" target="_blank" rel="noopener">@TGNICETOP</a></li>
        </ul></div>
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
