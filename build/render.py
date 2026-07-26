from playwright.sync_api import sync_playwright
import pathlib
base = pathlib.Path(__file__).parent
out  = base.parent / "assets"
out.mkdir(exist_ok=True)
jobs = [("header.html","header.png",1200,300),("footer.html","footer.png",1200,150)]
with sync_playwright() as p:
    b = p.chromium.launch()
    for src,dst,w,h in jobs:
        pg = b.new_page(viewport={"width":w,"height":h}, device_scale_factor=2)
        pg.goto((base/src).as_uri()); pg.wait_for_timeout(400)
        pg.screenshot(path=str(out/dst))
        print("ok:",dst); pg.close()
    b.close()
