# generator.py
from datetime import datetime
from pathlib import Path
import os

from config import (RESOURCES, ARTICLES, SITE_NAME, SITE_URL,
                    BOT_TG, ADMIN_TG, TG_CHANNEL, FOOTER_LINKS, ABOUT_CONTENT,
                    SITE_DESCRIPTION)
from templates import (styles_css, render_resource, render_homepage,
                       render_about, render_guide, render_faq, render_article)


class PageGenerator:
    def __init__(self, output_dir="dist"):
        self.out = Path(output_dir)

    def build_all(self):
        self._clean_dist()
        self.out.mkdir(parents=True, exist_ok=True)
        self.assets = self.out / "assets"
        self.assets.mkdir(exist_ok=True)

        print(f"\nBuilding to {self.out.resolve()}")
        self._write_assets()

        year = datetime.now().year
        footer_links = FOOTER_LINKS

        # Homepage
        html = render_homepage(
            RESOURCES, ARTICLES, footer_links,
            SITE_NAME, BOT_TG, ADMIN_TG, TG_CHANNEL,
            SITE_URL, SITE_DESCRIPTION, year
        )
        (self.out / "index.html").write_text(html, encoding="utf-8")
        print("  [OK] index.html")

        # Resource pages
        for r in RESOURCES:
            fname = r["id"] + ".html"
            html = render_resource(
                r, RESOURCES, footer_links,
                SITE_NAME, SITE_URL, BOT_TG, ADMIN_TG, TG_CHANNEL, year
            )
            (self.out / fname).write_text(html, encoding="utf-8")
            print(f"  [OK] {fname}")

        # Static pages
        static = [
            ("about.html", render_about(
                ABOUT_CONTENT, footer_links,
                SITE_NAME, BOT_TG, ADMIN_TG, TG_CHANNEL,
                SITE_URL, year
            )),
            ("guide.html", render_guide(
                RESOURCES, footer_links,
                SITE_NAME, BOT_TG, ADMIN_TG, TG_CHANNEL,
                SITE_URL, year
            )),
            ("faq.html", render_faq(
                footer_links,
                SITE_NAME, BOT_TG, ADMIN_TG, TG_CHANNEL,
                SITE_URL, year
            )),
        ]
        for fname, html in static:
            (self.out / fname).write_text(html, encoding="utf-8")
            print(f"  [OK] {fname}")

        # Articles
        for article in ARTICLES:
            fname = article["slug"] + ".html"
            html = render_article(
                article, ARTICLES, footer_links,
                SITE_NAME, SITE_URL, BOT_TG, ADMIN_TG, TG_CHANNEL, year
            )
            (self.out / fname).write_text(html, encoding="utf-8")
            print(f"  [OK] {fname}")

        # SEO files
        (self.out / "sitemap.xml").write_text(self._sitemap(), encoding="utf-8")
        (self.out / "robots.txt").write_text(self._robots(), encoding="utf-8")
        print("  [OK] sitemap.xml")
        print("  [OK] robots.txt")

        count = len(list(self.out.glob("*.html")))
        print(f"\nDone! {count} pages generated.")
        return self.out

    def _clean_dist(self):
        if self.out.exists():
            for root, dirs, files in os.walk(self.out, topdown=False):
                for name in files:
                    try:
                        (Path(root) / name).unlink()
                    except PermissionError:
                        pass
                for name in dirs:
                    try:
                        (Path(root) / name).rmdir()
                    except OSError:
                        pass
            try:
                self.out.rmdir()
            except OSError:
                pass

    def _write_assets(self):
        (self.out / "styles.css").write_text(styles_css(), encoding="utf-8")
        tmpl_dir = Path(__file__).parent / "templates"
        js_file = tmpl_dir / "templates_main.js"
        if js_file.exists():
            js_content = js_file.read_text(encoding="utf-8")
            (self.assets / "main.js").write_text(js_content, encoding="utf-8")
        favicon = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">'
            '<circle cx="16" cy="16" r="16" fill="#6366F1"/>'
            '<path d="M16 6C10.48 6 6 10.48 6 16s4.48 10 10 10 10-4.48 10-10S21.52 6 16 6zm-1 15h2v2h-2v-2zm0-12h2v10h-2V9z" fill="white"/>'
            "</svg>"
        )
        (self.assets / "favicon.svg").write_text(favicon, encoding="utf-8")

    def _sitemap(self):
        today = datetime.now().strftime("%Y-%m-%d")
        base = SITE_URL
        urls = [
            {"loc": base + "/", "priority": "1.0", "freq": "daily"},
            {"loc": base + "/about.html", "priority": "0.6", "freq": "monthly"},
            {"loc": base + "/guide.html", "priority": "0.7", "freq": "weekly"},
            {"loc": base + "/faq.html", "priority": "0.5", "freq": "monthly"},
        ]
        for r in RESOURCES:
            urls.append({
                "loc": base + "/" + r["id"] + ".html",
                "priority": "0.8",
                "freq": "weekly",
            })
        for a in ARTICLES:
            urls.append({
                "loc": base + "/" + a["slug"] + ".html",
                "priority": "0.7",
                "freq": "monthly",
            })
        items = ""
        for u in urls:
            items += (
                f"  <url>\n"
                f"    <loc>{u['loc']}</loc>\n"
                f"    <lastmod>{today}</lastmod>\n"
                f"    <changefreq>{u['freq']}</changefreq>\n"
                f"    <priority>{u['priority']}</priority>\n"
                f"  </url>\n"
            )
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' +
            items + "</urlset>"
        )

    def _robots(self):
        return f"""User-agent: *
Allow: /
Disallow:

Sitemap: {SITE_URL}/sitemap.xml
Host: {SITE_URL}
"""
