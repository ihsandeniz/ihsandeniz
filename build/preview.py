"""README'yi GitHub'ın kendi markdown motoruyla render edip ekran görüntüsü alır."""
import subprocess, pathlib
from playwright.sync_api import sync_playwright

md = pathlib.Path("README.md").read_text()
html = subprocess.run(["gh","api","--method","POST","/markdown","-f","mode=gfm","-f","text="+md],
                      capture_output=True, text=True, check=True).stdout
base = pathlib.Path(".").resolve().as_uri() + "/"
CSS = """
body{background:#0d1117;color:#e6edf3;font-family:"Adwaita Sans",sans-serif;font-size:16px;
 line-height:1.6;margin:0;padding:40px 48px;width:1012px;box-sizing:border-box}
a{color:#4493f8;text-decoration:none} img{max-width:100%}
h2{border-bottom:1px solid #3d444d;padding-bottom:.3em;margin:24px 0 16px;font-size:1.5em;font-weight:600}
table{border-collapse:collapse;width:100%;margin:16px 0;display:table}
th,td{border:1px solid #3d444d;padding:6px 13px}
/* GitHub td'ye vertical-align vermez → valign niteliği geçerli olur. Buna DOKUNMA. */
th,td:not([valign]){vertical-align:top}
tr:nth-child(2n){background:#151b23}
code{background:#6e768166;padding:.2em .4em;border-radius:6px;font-family:"JetBrains Mono",monospace;font-size:85%}
sub{color:#9198a1} p{margin:0 0 16px}
blockquote{border-left:.25em solid #3d444d;color:#9198a1;padding:0 1em;margin:0 0 16px}
"""
pathlib.Path("build/preview.html").write_text(
    f'<meta charset="utf-8"><base href="{base}"><style>{CSS}</style>{html}')

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1012,"height":1200})
    pg.goto(pathlib.Path("build/preview.html").resolve().as_uri()); pg.wait_for_timeout(2500)
    pg.screenshot(path="build/preview.png", full_page=True)
    box = pg.evaluate("""() => {
      const td=[...document.querySelectorAll('td')].find(t=>t.querySelector('img[alt*="monogram"]'));
      const i=td.querySelector('img').getBoundingClientRect(), t=td.getBoundingClientRect();
      return {ust:+(i.top-t.top).toFixed(1), alt:+(t.bottom-i.bottom).toFixed(1),
              hiza:getComputedStyle(td).verticalAlign};
    }""")
    print("logo hücresi →", box); b.close()
