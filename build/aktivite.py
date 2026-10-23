"""Son 31 günün katkı grafiğini assets/activity.svg (+ dar ekran için activity-mobile.svg) olarak üretir. Dış servis yok.

Veri: GitHub GraphQL `contributionCalendar` (profilde herkese görünen sayılarla aynı).
Token: GITHUB_TOKEN ortam değişkeni; yoksa `gh auth token`.
Yerelde: python3 build/aktivite.py · Action'da: .github/workflows/aktivite.yml
"""
import datetime, json, os, pathlib, subprocess, urllib.request

KULLANICI = "ihsandeniz"
GUN = 31
ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"
# (dosya, genişlik, yükseklik, yazı punto, tarih etiketi aralığı) — dar sürüm telefonda ~308 px'e iner
SURUMLER = [("activity.svg", 1200, 300, 16, 5), ("activity-mobile.svg", 600, 380, 24, 10)]

token = os.environ.get("GITHUB_TOKEN") or subprocess.run(
    ["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
sorgu = ('query($u:String!){user(login:$u){contributionsCollection{contributionCalendar'
         '{weeks{contributionDays{date contributionCount}}}}}}')
istek = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": sorgu, "variables": {"u": KULLANICI}}).encode(),
    headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"})
veri = json.load(urllib.request.urlopen(istek, timeout=30))
gunler = [d for w in veri["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
          for d in w["contributionDays"]][-GUN:]

sayilar = [d["contributionCount"] for d in gunler]
tepe = max(max(sayilar), 1)
toplam = sum(sayilar)
tarih = lambda s: datetime.date.fromisoformat(s).strftime("%b %d").replace(" 0", " ")


def ciz(W, H, P, ADIM):
    SOL, SAG, UST, ALT = round(P * 3.6), round(P * 1.5), round(P * 4.2), round(P * 2.6)
    iw, ih = W - SOL - SAG, H - UST - ALT
    x = lambda i: SOL + iw * i / (len(gunler) - 1)
    y = lambda n: UST + ih * (1 - n / tepe)
    noktalar = [(x(i), y(n)) for i, n in enumerate(sayilar)]
    cizgi = " ".join(f"{a:.1f},{b:.1f}" for a, b in noktalar)
    alan = f"M{SOL},{UST + ih} L" + " L".join(f"{a:.1f},{b:.1f}" for a, b in noktalar) + f" L{SOL + iw},{UST + ih} Z"
    etiketler = "".join(
        f'<text x="{x(i):.1f}" y="{H - P * .8:.0f}" text-anchor="middle">{tarih(gunler[i]["date"])}</text>'
        for i in range(0, len(gunler) - 1, ADIM))
    izgara = "".join(
        f'<line x1="{SOL}" x2="{SOL + iw}" y1="{y(tepe * k / 4):.1f}" y2="{y(tepe * k / 4):.1f}"/>'
        f'<text x="{SOL - P * .6:.0f}" y="{y(tepe * k / 4) + P * .35:.1f}" text-anchor="end">{round(tepe * k / 4)}</text>'
        for k in range(0, 5, 2))
    noktalar_svg = "".join(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="{P * .25:.1f}"/>' for a, b in noktalar)
    dar = W < 900
    baslik = f"LAST {GUN} DAYS" if dar else f"CONTRIBUTION ACTIVITY · LAST {GUN} DAYS"
    ozet = f"{toplam} total" if dar else f"{toplam} total · peak {max(sayilar)}/day"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img"
 aria-label="{toplam} contributions in the last {GUN} days">
<defs><linearGradient id="a" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#22d3ee" stop-opacity=".35"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/>
</linearGradient></defs>
<style>text{{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;fill:#8b98a8;font-size:{P}px}}
.b{{font-size:{P * 1.1:.0f}px;font-weight:600;letter-spacing:.06em}} .g{{fill:#f2cc60}}</style>
<text class="b" x="{SOL}" y="{P * 1.9:.0f}">{baslik}</text>
<text class="b g" x="{W - SAG}" y="{P * 1.9:.0f}" text-anchor="end">{ozet}</text>
<g stroke="#8b98a8" stroke-opacity=".15">{izgara}</g>
<path d="{alan}" fill="url(#a)"/>
<polyline points="{cizgi}" fill="none" stroke="#22d3ee" stroke-width="{P * .17:.1f}" stroke-linejoin="round"/>
<g fill="#f2cc60">{noktalar_svg}</g>
{etiketler}
<text x="{W - SAG}" y="{H - P * .8:.0f}" text-anchor="end">{"" if dar else "updated "}{tarih(gunler[-1]["date"])}</text>
</svg>
'''


for dosya, W, H, P, ADIM in SURUMLER:
    (ASSETS / dosya).write_text(ciz(W, H, P, ADIM))
print(f"{gunler[0]['date']} → {gunler[-1]['date']}, {toplam} katkı, tepe {max(sayilar)} · " + ", ".join(s[0] for s in SURUMLER))
