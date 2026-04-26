# templates/templates_base.py
# Premium animated UI — rich, interactive, dynamic feel


def styles_css() -> str:
    return r"""
/* ═══════════════════════════════════════════
   TG工具集 - Premium Animated UI
   ═══════════════════════════════════════════ */

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --primary: #6366F1;
  --primary-dark: #4F46E5;
  --primary-light: #818CF8;
  --accent: #06D6A0;
  --accent2: #FF6B6B;
  --dark: #0B0F1A;
  --gray-900: #111827;
  --gray-800: #1F2937;
  --gray-700: #374151;
  --gray-600: #4B5563;
  --gray-500: #6B7280;
  --gray-400: #9CA3AF;
  --gray-300: #D1D5DB;
  --gray-200: #E5E7EB;
  --gray-100: #F3F4F6;
  --gray-50: #F9FAFB;
  --white: #FFFFFF;
  --font: 'Inter', 'Noto Sans SC', system-ui, -apple-system, sans-serif;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root { color-scheme: dark; }
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--gray-900); }
::-webkit-scrollbar-thumb { background: var(--gray-700); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--gray-600); }

html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: var(--font);
  color: var(--gray-800);
  background: var(--white);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}
a { color: var(--primary); text-decoration: none; }
a:hover { color: var(--primary-dark); }
ul { list-style: none; }

/* ── Focus visible ── */
:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 3px;
  border-radius: 4px;
}

/* ── Selection ── */
::selection { background: rgba(99,102,241,0.2); color: var(--gray-900); }

/* ── Container ── */
.container { max-width: 1150px; margin: 0 auto; padding: 0 1.5rem; }

/* ═══════════════════════════════════════════
   NAVBAR
   ═══════════════════════════════════════════ */
.navbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  background: rgba(11, 15, 26, 0.85);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  transition: background 0.3s, box-shadow 0.3s;
}
.navbar.scrolled {
  background: rgba(11, 15, 26, 0.97);
  box-shadow: 0 4px 30px rgba(0,0,0,0.3);
}
.nav-inner {
  display: flex; align-items: center; justify-content: space-between;
  height: 68px;
}
.nav-logo {
  display: flex; align-items: center; gap: 0.6rem;
  font-weight: 700; font-size: 1.05rem; color: white;
  transition: opacity 0.2s;
}
.nav-logo:hover { opacity: 0.8; color: white; }
.nav-logo-dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 8px var(--accent);
  animation: blink 2s ease-in-out infinite;
}
@keyframes blink {
  0%, 100% { opacity: 1; box-shadow: 0 0 8px var(--accent); }
  50% { opacity: 0.5; box-shadow: 0 0 3px var(--accent); }
}
.nav-links { display: flex; align-items: center; gap: 0.15rem; }
.nav-links a {
  padding: 0.4rem 0.85rem; border-radius: 8px;
  color: rgba(255,255,255,0.65); font-weight: 500; font-size: 0.88rem;
  transition: color 0.2s, background 0.2s;
}
.nav-links a:hover { color: white; background: rgba(255,255,255,0.08); }
.nav-links a.active { color: white; background: rgba(99,102,241,0.2); }
.btn-tg-nav {
  display: flex; align-items: center; gap: 0.35rem;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark)) !important;
  color: white !important; font-weight: 600;
  box-shadow: 0 0 20px rgba(99,102,241,0.3);
  transition: box-shadow 0.2s, transform 0.2s;
}
.btn-tg-nav:hover {
  box-shadow: 0 0 30px rgba(99,102,241,0.5);
  transform: translateY(-1px);
  color: white !important;
}
.nav-toggle { display: none; background: none; border: none; cursor: pointer; padding: 0.5rem; flex-direction: column; gap: 5px; }
.nav-toggle span { width: 22px; height: 2px; background: rgba(255,255,255,0.7); border-radius: 2px; transition: all 0.3s; }
.nav-toggle.active span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.nav-toggle.active span:nth-child(2) { opacity: 0; }
.nav-toggle.active span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }

/* ═══════════════════════════════════════════
   HERO SECTION
   ═══════════════════════════════════════════ */
.hero {
  position: relative; min-height: 100vh;
  display: flex; align-items: center;
  background: var(--dark);
  overflow: hidden;
  padding: 100px 0 80px;
}
.hero-bg {
  position: absolute; inset: 0; z-index: 0;
  background:
    radial-gradient(ellipse 80% 60% at 20% 50%, rgba(99,102,241,0.15) 0%, transparent 70%),
    radial-gradient(ellipse 60% 50% at 80% 20%, rgba(6,214,160,0.1) 0%, transparent 60%),
    radial-gradient(ellipse 50% 40% at 50% 80%, rgba(255,107,107,0.08) 0%, transparent 60%);
}
/* Animated grid overlay */
.hero-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: gridMove 20s linear infinite;
}
@keyframes gridMove {
  0% { background-position: 0 0; }
  100% { background-position: 60px 60px; }
}
/* Floating orbs */
.hero-orb {
  position: absolute; border-radius: 50%;
  filter: blur(80px); z-index: 0;
  animation: orbFloat 8s ease-in-out infinite;
}
.hero-orb-1 { width: 400px; height: 400px; background: rgba(99,102,241,0.2); top: -100px; left: -100px; animation-delay: 0s; }
.hero-orb-2 { width: 300px; height: 300px; background: rgba(6,214,160,0.15); bottom: -50px; right: -50px; animation-delay: -4s; }
.hero-orb-3 { width: 200px; height: 200px; background: rgba(255,107,107,0.1); top: 40%; left: 60%; animation-delay: -2s; }
@keyframes orbFloat {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33% { transform: translate(20px, -30px) scale(1.05); }
  66% { transform: translate(-15px, 20px) scale(0.95); }
}
.hero-content {
  position: relative; z-index: 2; max-width: 720px;
}
.hero-badge {
  display: inline-flex; align-items: center; gap: 0.5rem;
  background: rgba(99,102,241,0.15); border: 1px solid rgba(99,102,241,0.3);
  color: var(--primary-light); padding: 0.35rem 1rem; border-radius: 999px;
  font-size: 0.78rem; font-weight: 600; letter-spacing: 0.04em;
  margin-bottom: 1.5rem;
  animation: fadeInUp 0.8s ease-out both;
}
.hero-badge-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 6px var(--accent);
  animation: blink 2s ease-in-out infinite;
}
.hero h1 {
  font-size: clamp(2.2rem, 5vw, 3.8rem);
  font-weight: 800; color: white;
  line-height: 1.12; margin-bottom: 1.25rem;
  letter-spacing: -0.03em;
  animation: fadeInUp 0.8s 0.1s ease-out both;
}
.hero h1 .gradient-text {
  background: linear-gradient(135deg, var(--primary-light), var(--accent));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.hero p {
  font-size: 1.1rem; color: rgba(255,255,255,0.55);
  max-width: 560px; line-height: 1.8;
  animation: fadeInUp 0.8s 0.2s ease-out both;
}
.hero-actions {
  display: flex; gap: 0.9rem; margin-top: 2rem; flex-wrap: wrap;
  animation: fadeInUp 0.8s 0.3s ease-out both;
}
.btn-primary {
  display: inline-flex; align-items: center; gap: 0.45rem;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white; padding: 0.8rem 2rem; border-radius: 12px;
  font-weight: 700; font-size: 0.95rem;
  border: none; cursor: pointer;
  position: relative; overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px rgba(99,102,241,0.35);
}
.btn-primary::before {
  content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
  transition: left 0.5s;
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(99,102,241,0.5); color: white; }
.btn-primary:hover::before { left: 100%; }
.btn-secondary {
  display: inline-flex; align-items: center; gap: 0.45rem;
  background: rgba(255,255,255,0.07); color: white;
  padding: 0.8rem 2rem; border-radius: 12px;
  font-weight: 600; font-size: 0.95rem;
  border: 1px solid rgba(255,255,255,0.15);
  transition: background 0.2s, border-color 0.2s, transform 0.2s;
}
.btn-secondary:hover { background: rgba(255,255,255,0.12); border-color: rgba(255,255,255,0.3); transform: translateY(-2px); color: white; }

/* Stats bar */
.hero-stats {
  display: flex; gap: 3rem; margin-top: 3.5rem; flex-wrap: wrap;
  animation: fadeInUp 0.8s 0.4s ease-out both;
}
.hero-stat { position: relative; }
.hero-stat::after {
  content: ''; position: absolute; right: -1.5rem; top: 50%; transform: translateY(-50%);
  width: 1px; height: 30px; background: rgba(255,255,255,0.1);
}
.hero-stat:last-child::after { display: none; }
.hero-stat h3 {
  color: white; font-size: 2rem; font-weight: 800;
  display: flex; align-items: baseline; gap: 0.15rem;
}
.hero-stat h3 .unit { font-size: 1rem; font-weight: 600; color: var(--primary-light); }
.hero-stat p { color: rgba(255,255,255,0.4); font-size: 0.78rem; font-weight: 500; margin-top: 0.15rem; }

/* Floating shapes */
.hero-shapes { position: absolute; right: 5%; top: 50%; transform: translateY(-50%); z-index: 1; }
.shape-card {
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px; padding: 1.25rem 1.5rem; margin-bottom: 1rem;
  backdrop-filter: blur(10px);
  animation: shapeFloat 6s ease-in-out infinite;
}
.shape-card:nth-child(2) { animation-delay: -2s; margin-left: 2rem; }
.shape-card:nth-child(3) { animation-delay: -4s; margin-left: 1rem; }
@keyframes shapeFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
.shape-card-inner { display: flex; align-items: center; gap: 0.75rem; }
.shape-icon { width: 36px; height: 36px; border-radius: 9px; display: flex; align-items: center; justify-content: center; }
.shape-icon svg { width: 18px; height: 18px; }
.shape-card h4 { color: white; font-size: 0.85rem; font-weight: 600; }
.shape-card p { color: rgba(255,255,255,0.4); font-size: 0.72rem; }

/* ═══════════════════════════════════════════
   TICKER / MARQUEE
   ═══════════════════════════════════════════ */
.ticker-wrap {
  background: linear-gradient(90deg, var(--primary-dark), var(--primary), var(--accent));
  overflow: hidden; padding: 0.75rem 0;
  position: relative;
}
.ticker-wrap::before, .ticker-wrap::after {
  content: ''; position: absolute; top: 0; bottom: 0; width: 80px; z-index: 2;
}
.ticker-wrap::before { left: 0; background: linear-gradient(90deg, var(--dark), transparent); }
.ticker-wrap::after { right: 0; background: linear-gradient(270deg, var(--dark), transparent); }
.ticker {
  display: flex; animation: ticker 30s linear infinite;
  white-space: nowrap;
}
.ticker span {
  color: rgba(255,255,255,0.9); font-size: 0.8rem; font-weight: 600;
  padding: 0 2rem;
  display: flex; align-items: center; gap: 0.5rem;
}
.ticker span::before { content: '◆'; font-size: 0.5rem; color: rgba(255,255,255,0.5); }
@keyframes ticker { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

/* ═══════════════════════════════════════════
   SECTIONS
   ═══════════════════════════════════════════ */
.section { padding: 5.5rem 0; }
.section-sm { padding: 3rem 0; }
.section-gray { background: var(--gray-50); }
.section-dark { background: var(--dark); color: white; }

.section-header { text-align: center; max-width: 640px; margin: 0 auto 3.5rem; }
.section-label {
  display: inline-flex; align-items: center; gap: 0.4rem;
  background: rgba(99,102,241,0.08); color: var(--primary);
  border: 1px solid rgba(99,102,241,0.2);
  padding: 0.3rem 1rem; border-radius: 999px;
  font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; margin-bottom: 0.75rem;
}
.section-title { font-size: clamp(1.6rem, 3.5vw, 2.4rem); font-weight: 800; color: var(--gray-900); margin-bottom: 0.75rem; letter-spacing: -0.02em; }
.section-desc { color: var(--gray-500); font-size: 1rem; }

/* ═══════════════════════════════════════════
   RESOURCE CARDS
   ═══════════════════════════════════════════ */
.resource-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 1.5rem; }
.resource-card {
  background: white; border-radius: 20px; border: 1px solid var(--gray-200);
  padding: 0; overflow: hidden;
  position: relative;
  transform: translateY(0);
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s;
  cursor: pointer;
  display: flex; flex-direction: column;
}
.resource-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 60px rgba(99,102,241,0.12), 0 8px 20px rgba(0,0,0,0.08);
}
.resource-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
  background: linear-gradient(90deg, var(--primary), var(--accent));
  transform: scaleX(0); transform-origin: left;
  transition: transform 0.3s ease;
}
.resource-card:hover::before { transform: scaleX(1); }

.card-top { display: flex; align-items: flex-start; justify-content: space-between; padding: 1.75rem 1.75rem 0; }
.card-icon-wrap { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.card-badge {
  font-size: 0.7rem; font-weight: 700; padding: 0.22rem 0.65rem; border-radius: 6px;
  animation: badgePulse 3s ease-in-out infinite;
}
.badge-hot { background: #FEF2F2; color: #DC2626; }
.badge-recommend { background: #F0FDF4; color: #16A34A; }
@keyframes badgePulse { 0%,100%{opacity:1} 50%{opacity:0.7} }

.card-body { padding: 0.75rem 1.75rem 1.5rem; flex: 1; }
.resource-card h3 { font-size: 1.1rem; font-weight: 700; color: var(--gray-900); margin-bottom: 0.2rem; }
.card-tagline { font-size: 0.78rem; color: var(--gray-400); margin-bottom: 0.75rem; font-weight: 500; }
.resource-card > p { font-size: 0.875rem; color: var(--gray-600); line-height: 1.7; margin-bottom: 1rem; }

.card-tags { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 1rem; }
.tag { background: var(--gray-100); color: var(--gray-600); padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.72rem; font-weight: 500; transition: background 0.2s, color 0.2s; }
.resource-card:hover .tag { background: rgba(99,102,241,0.08); color: var(--primary); }

.card-footer {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.9rem 1.75rem; border-top: 1px solid var(--gray-100);
  background: var(--gray-50);
}
.card-link {
  font-size: 0.85rem; font-weight: 700; color: var(--primary);
  display: flex; align-items: center; gap: 0.3rem;
  transition: gap 0.2s;
}
.resource-card:hover .card-link { gap: 0.6rem; }
.card-category { font-size: 0.72rem; color: var(--gray-400); font-weight: 500; }

/* Glow border effect on hover */
.resource-card::after {
  content: ''; position: absolute; inset: -1px; border-radius: 21px;
  background: linear-gradient(135deg, var(--primary), var(--accent));
  z-index: -1; opacity: 0;
  transition: opacity 0.3s;
}
.resource-card:hover::after { opacity: 0.15; }

/* ═══════════════════════════════════════════
   TRUST BAR
   ═══════════════════════════════════════════ */
.trust-bar {
  background: white; border-top: 1px solid var(--gray-200); border-bottom: 1px solid var(--gray-200);
  padding: 1.75rem 0;
}
.trust-grid { display: flex; gap: 3rem; flex-wrap: wrap; justify-content: center; }
.trust-item { display: flex; align-items: center; gap: 0.6rem; }
.trust-item svg { color: var(--accent); flex-shrink: 0; }
.trust-item span { font-size: 0.875rem; color: var(--gray-600); font-weight: 500; }

/* ═══════════════════════════════════════════
   CTA SECTION
   ═══════════════════════════════════════════ */
.cta-section {
  background: var(--dark); padding: 6rem 0; text-align: center;
  position: relative; overflow: hidden;
}
.cta-section::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 70% 60% at 50% 100%, rgba(99,102,241,0.2) 0%, transparent 70%);
}
.cta-section h2 { color: white; font-size: clamp(1.8rem, 3.5vw, 2.8rem); font-weight: 800; margin-bottom: 0.75rem; position: relative; }
.cta-section p { color: rgba(255,255,255,0.45); font-size: 1.05rem; margin-bottom: 2rem; position: relative; }
.cta-actions { display: flex; gap: 0.9rem; justify-content: center; flex-wrap: wrap; position: relative; }

/* ═══════════════════════════════════════════
   FEATURE CARDS (section cards)
   ═══════════════════════════════════════════ */
.feature-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.25rem; }
.feature-card {
  background: white; border-radius: 16px; border: 1px solid var(--gray-200);
  padding: 1.75rem; transition: transform 0.25s, box-shadow 0.25s;
}
.feature-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,0,0,0.08); }
.feature-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; }
.feature-card h3 { font-size: 1rem; font-weight: 700; color: var(--gray-900); margin-bottom: 0.4rem; }
.feature-card p { font-size: 0.85rem; color: var(--gray-500); line-height: 1.65; }

/* ═══════════════════════════════════════════
   TOOL DETAIL PAGE
   ═══════════════════════════════════════════ */
.tool-header {
  padding: 100px 0 3rem; background: var(--dark);
  position: relative; overflow: hidden;
}
.tool-header::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 60% 80% at 20% 50%, rgba(99,102,241,0.12) 0%, transparent 70%);
}
.tool-header-inner { display: flex; align-items: flex-start; gap: 1.5rem; position: relative; z-index: 1; }
.tool-icon-lg { width: 64px; height: 64px; border-radius: 18px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.tool-header h1 { font-size: clamp(1.8rem, 4vw, 2.6rem); font-weight: 800; color: white; margin-bottom: 0.3rem; }
.tool-header .subtitle { font-size: 1rem; color: rgba(255,255,255,0.5); margin-bottom: 1rem; }
.tool-header .description { font-size: 0.975rem; color: rgba(255,255,255,0.65); max-width: 660px; line-height: 1.8; }
.breadcrumb { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem; }
.breadcrumb a, .breadcrumb span { font-size: 0.8rem; color: rgba(255,255,255,0.4); }
.breadcrumb a:hover { color: var(--primary-light); }
.tool-badge {
  display: inline-block; font-size: 0.72rem; font-weight: 600;
  padding: 0.25rem 0.75rem; border-radius: 6px; margin-right: 0.5rem;
  background: rgba(99,102,241,0.15); color: var(--primary-light);
  border: 1px solid rgba(99,102,241,0.3);
}

/* Sidebar card */
.sidebar-card {
  background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
  border-radius: 16px; padding: 1.5rem; margin-bottom: 1.25rem;
  backdrop-filter: blur(10px);
}
.sidebar-card h3 { font-size: 0.9rem; font-weight: 700; color: white; margin-bottom: 1rem; }

/* ═══════════════════════════════════════════
   STEPS
   ═══════════════════════════════════════════ */
.step-list { display: flex; flex-direction: column; gap: 0; }
.step-item { display: flex; gap: 1.5rem; padding: 1.5rem 0; border-bottom: 1px solid var(--gray-100); position: relative; }
.step-item:last-child { border-bottom: none; }
.step-num {
  flex-shrink: 0; width: 36px; height: 36px; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white; font-weight: 800; font-size: 0.9rem;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 0 20px rgba(99,102,241,0.3);
}
.step-content h4 { font-size: 1rem; font-weight: 700; color: var(--gray-900); margin-bottom: 0.25rem; }
.step-content p { font-size: 0.875rem; color: var(--gray-500); }

/* ═══════════════════════════════════════════
   FEATURE LIST
   ═══════════════════════════════════════════ */
.features-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; }
.feature-item { display: flex; gap: 0.75rem; }
.feature-check {
  flex-shrink: 0; width: 22px; height: 22px; border-radius: 50%;
  background: rgba(6,214,160,0.1); display: flex; align-items: center; justify-content: center; margin-top: 2px;
}
.feature-item h4 { font-size: 0.9rem; font-weight: 600; color: var(--gray-900); }
.feature-item p { font-size: 0.8rem; color: var(--gray-400); }

/* ═══════════════════════════════════════════
   FAQ
   ═══════════════════════════════════════════ */
.faq-item { border-bottom: 1px solid var(--gray-200); }
.faq-item:last-child { border-bottom: none; }
.faq-q {
  display: flex; align-items: center; justify-content: space-between;
  padding: 1.25rem 0; font-weight: 600; font-size: 0.975rem; color: var(--gray-900);
  cursor: pointer; user-select: none;
  transition: color 0.2s;
}
.faq-q:hover { color: var(--primary); }
.faq-q svg { flex-shrink: 0; color: var(--gray-400); transition: transform 0.3s, color 0.2s; }
.faq-item.open .faq-q svg { transform: rotate(180deg); color: var(--primary); }
.faq-a { display: none; padding: 0 0 1.25rem; color: var(--gray-600); font-size: 0.9rem; line-height: 1.8; }
.faq-item.open .faq-a { display: block; }
.faq-item.open .faq-q { color: var(--primary); }

/* ═══════════════════════════════════════════
   FOOTER
   ═══════════════════════════════════════════ */
.footer { background: var(--dark); color: var(--gray-400); padding: 4rem 0 2rem; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; margin-bottom: 3rem; }
.footer-brand p { font-size: 0.85rem; color: var(--gray-500); line-height: 1.75; margin-top: 0.75rem; max-width: 280px; }
.footer h4 { font-size: 0.78rem; font-weight: 700; color: white; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 1.25rem; }
.footer ul { display: flex; flex-direction: column; gap: 0.6rem; }
.footer a { font-size: 0.85rem; color: var(--gray-500); transition: color 0.2s; }
.footer a:hover { color: white; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.07); padding-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; }
.footer-bottom p { font-size: 0.78rem; color: var(--gray-600); }

/* ═══════════════════════════════════════════
   PAGE HEADER (inner pages)
   ═══════════════════════════════════════════ */
.page-header { padding: 100px 0 3rem; background: var(--dark); position: relative; overflow: hidden; }
.page-header::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 60% 100% at 30% 50%, rgba(99,102,241,0.1) 0%, transparent 70%); }
.page-header h1 { font-size: clamp(1.8rem, 3.5vw, 2.6rem); font-weight: 800; color: white; margin-bottom: 0.5rem; position: relative; }
.page-header p { color: rgba(255,255,255,0.45); font-size: 0.975rem; max-width: 600px; position: relative; }
.breadcrumb { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem; position: relative; }
.breadcrumb a, .breadcrumb span { font-size: 0.8rem; color: rgba(255,255,255,0.4); }
.breadcrumb a:hover { color: var(--primary-light); }

/* ═══════════════════════════════════════════
   CONTACT / FORM
   ═══════════════════════════════════════════ */
.contact-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: 3rem; }
.contact-item { display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 1.5rem; }
.contact-icon { width: 42px; height: 42px; border-radius: 11px; background: rgba(99,102,241,0.08); display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--primary); }
.contact-item h4 { font-size: 0.9rem; font-weight: 700; color: var(--gray-900); margin-bottom: 0.15rem; }
.contact-item p { font-size: 0.85rem; color: var(--gray-500); }
.form-group { margin-bottom: 1.1rem; }
.form-group label { display: block; font-size: 0.875rem; font-weight: 500; margin-bottom: 0.35rem; color: var(--gray-700); }
.form-group input, .form-group textarea, .form-group select {
  width: 100%; padding: 0.7rem 1rem; border: 1.5px solid var(--gray-300);
  border-radius: 10px; font-size: 0.9rem; font-family: var(--font);
  background: white; transition: border-color 0.2s, box-shadow 0.2s;
}
.form-group input:focus, .form-group textarea:focus, .form-group select:focus {
  outline: none; border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99,102,241,0.08);
}
.form-group textarea { min-height: 110px; resize: vertical; }

/* ═══════════════════════════════════════════
   ABOUT / VALUES
   ═══════════════════════════════════════════ */
.about-content { max-width: 720px; margin: 0 auto; }
.about-content p { font-size: 1rem; color: var(--gray-700); line-height: 2; margin-bottom: 1.25rem; }
.values-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1.25rem; margin-top: 2rem; }
.value-card {
  background: var(--gray-50); border-radius: 14px;
  padding: 1.5rem; border: 1px solid var(--gray-200);
  transition: transform 0.2s, box-shadow 0.2s;
}
.value-card:hover { transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.06); }
.value-card h4 { font-size: 0.95rem; font-weight: 700; color: var(--gray-900); margin-bottom: 0.4rem; }
.value-card p { font-size: 0.82rem; color: var(--gray-500); line-height: 1.7; }

/* ═══════════════════════════════════════════
   GUIDE
   ═══════════════════════════════════════════ */
.guide-section { border: 1px solid var(--gray-200); border-radius: 18px; padding: 2rem; margin-bottom: 1.5rem; background: white; transition: box-shadow 0.2s; }
.guide-section:hover { box-shadow: 0 8px 30px rgba(0,0,0,0.05); }
.guide-section h3 { font-size: 1.1rem; font-weight: 700; color: var(--gray-900); margin-bottom: 1rem; padding-bottom: 0.75rem; border-bottom: 1px solid var(--gray-100); }
.guide-section h2 { font-size: 1.1rem; font-weight: 700; color: var(--gray-900); margin-bottom: 1rem; }
.guide-section p, .guide-section li { font-size: 0.9rem; color: var(--gray-700); line-height: 1.85; }
.guide-section ul { display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.75rem; padding-left: 1.25rem; }
.guide-section li { list-style: disc; }

/* ═══════════════════════════════════════════
   ANIMATIONS
   ═══════════════════════════════════════════ */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; } to { opacity: 1; }
}
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
.animate-fade-up { animation: fadeInUp 0.6s ease-out both; }
.animate-fade { animation: fadeIn 0.6s ease-out both; }
.animate-scale { animation: scaleIn 0.5s ease-out both; }

/* Scroll-triggered animations */
.observe-me { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease-out, transform 0.6s ease-out; }
.observe-me.visible { opacity: 1; transform: translateY(0); }

/* ═══════════════════════════════════════════
   RESPONSIVE
   ═══════════════════════════════════════════ */
@media (max-width: 900px) {
  .hero-shapes { display: none; }
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 2rem; }
}
@media (max-width: 768px) {
  body { padding-top: 68px; }
  .nav-toggle { display: flex; }
  .nav-links {
    display: none; flex-direction: column;
    position: fixed; top: 68px; left: 0; right: 0; bottom: 0;
    background: rgba(11,15,26,0.98); backdrop-filter: blur(20px);
    padding: 1rem 1.5rem; gap: 0.25rem;
    border-top: 1px solid rgba(255,255,255,0.08);
  }
  .nav-links.open { display: flex; }
  .nav-links a { padding: 0.75rem 1rem; border-radius: 10px; font-size: 1rem; }
  .hero { padding: 80px 0 60px; min-height: auto; }
  .hero-stats { gap: 1.5rem; flex-wrap: wrap; }
  .hero-stat::after { display: none; }
  .footer-grid { grid-template-columns: 1fr; gap: 2rem; }
  .contact-grid { grid-template-columns: 1fr; }
  .resource-grid { grid-template-columns: 1fr; }
  .tool-header-inner { flex-direction: column; }
  .hero-actions { flex-direction: column; }
  .btn-primary, .btn-secondary { justify-content: center; }
  .footer-bottom { flex-direction: column; gap: 0.5rem; text-align: center; }
  .trust-grid { gap: 1.25rem; }
  .features-list { grid-template-columns: 1fr; }
  .values-grid { grid-template-columns: 1fr; }
}
@media (max-width: 480px) {
  .section { padding: 3.5rem 0; }
  .hero h1 { font-size: 1.9rem; }
  .guide-section { padding: 1.25rem; }
}

/* ═══════════════════════════════════════════
   UTILITIES
   ═══════════════════════════════════════════ */
.text-center { text-align: center; }
.mt-2 { margin-top: 1rem; }
.mb-2 { margin-bottom: 1rem; }

/* Print styles */
@media print {
  .navbar, .footer, .cta-section, .ticker-wrap { display: none; }
  .hero { min-height: auto; padding: 2rem 0; }
  body { color: #000; background: #fff; }
}
"""
