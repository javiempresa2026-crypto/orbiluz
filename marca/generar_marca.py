"""Identidad de Orbiluz: logotipo (SVG con la letra convertida en trazos), icono, paleta y hoja de marca.
La «o» inicial es un planeta con anillo (órbita + luz). Los PNG se generan con Chromium (Playwright).
Uso: python3 orbiluz/marca/generar_marca.py"""
import os, math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

D = os.path.dirname(os.path.abspath(__file__))
OUT = f"{D}/logo"; os.makedirs(OUT, exist_ok=True)

# Paleta
NOCHE, NEBULOSA, AMBAR, LUNA, NIEBLA, CORAL = "#12123A", "#7C6CF6", "#FFB547", "#FFF6E9", "#A7A9C9", "#FF7A59"

def word_paths(text, font_file, size):
    """Trazos SVG de un texto (sin depender de la fuente instalada) + ancho total."""
    f = TTFont(font_file); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
    s = size / upm; x = 0; d = []
    for ch in text:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, 0)))
        d.append(pen.getCommands()); x += gs[g].width * s
    asc = f["OS/2"].sxHeight * s
    return " ".join(d), x, asc

def planet(cx, cy, r, body, ring, knock=None, tilt=-22):
    """Planeta con anillo: mitad trasera del anillo, esfera, mitad delantera (con separación opcional)."""
    rx, ry, w = r * 1.62, r * 0.42, r * 0.2
    back = f'<path d="M {-rx} 0 A {rx} {ry} 0 0 1 {rx} 0" fill="none" stroke="{ring}" stroke-width="{w}" stroke-linecap="round"/>'
    front = f'<path d="M {rx} 0 A {rx} {ry} 0 0 1 {-rx} 0" fill="none" stroke="{ring}" stroke-width="{w}" stroke-linecap="round"/>'
    kn = f'<path d="M {rx*0.93} {ry*0.37} A {rx} {ry} 0 0 1 {-rx*0.93} {ry*0.37}" fill="none" stroke="{knock}" stroke-width="{w*2.1}"/>' if knock else ""
    shine = f'<circle cx="{-r*0.35}" cy="{-r*0.38}" r="{r*0.2}" fill="#fff" opacity=".35"/>'
    return (f'<g transform="translate({cx} {cy}) rotate({tilt})">{back}</g>'
            f'<g transform="translate({cx} {cy})"><circle r="{r}" fill="{body}"/>{shine}</g>'
            f'<g transform="translate({cx} {cy}) rotate({tilt})">{kn}{front}</g>')

def logo_svg(fg, body, ring, bg=None, size=200):
    d, w, xh = word_paths("rbiluz", f"{D}/fuentes/Unbounded-Bold.ttf", size)
    r = xh * 0.56; pad = r * 1.9; gap = r * 0.55
    W = pad + r + gap + w + size * 0.12; H = size * 1.5; base = size * 1.05
    cx, cy = pad, base - xh / 2
    rect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">{rect}'
            f'{planet(cx, cy, r, body, ring, knock=bg)}'
            f'<path transform="translate({cx + r + gap:.1f} {base:.1f})" d="{d}" fill="{fg}"/></svg>')

def icon_svg(bg, body, ring, size=512, round_=True):
    c = size / 2; r = size * 0.24
    rect = f'<rect width="{size}" height="{size}" rx="{size*0.22 if round_ else 0}" fill="{bg}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">{rect}{planet(c, c, r, body, ring, knock=bg)}</svg>'

VARIANTES = {
    "orbiluz-logo-noche": logo_svg(LUNA, AMBAR, NEBULOSA, NOCHE),          # principal, sobre fondo oscuro
    "orbiluz-logo-luna": logo_svg(NOCHE, AMBAR, NEBULOSA, LUNA),           # sobre fondo claro
    "orbiluz-logo-blanco": logo_svg("#FFFFFF", AMBAR, "#FFFFFF"),          # transparente, para fotos oscuras
    "orbiluz-logo-negro": logo_svg(NOCHE, AMBAR, NEBULOSA),                # transparente, para fondos claros
    "orbiluz-icono": icon_svg(NOCHE, AMBAR, NEBULOSA),                     # favicon y avatar
    "orbiluz-avatar": icon_svg(NOCHE, AMBAR, NEBULOSA, round_=False),      # redes (se recorta en círculo)
}

HOJA = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:U;src:url(fuentes/Unbounded-Bold.ttf)}}@font-face{{font-family:UX;src:url(fuentes/Unbounded-ExtraBold.ttf)}}
@font-face{{font-family:S;src:url(fuentes/DMSans-Regular.ttf)}}@font-face{{font-family:SB;src:url(fuentes/DMSans-Bold.ttf)}}
body{{margin:0;width:1600px;background:{LUNA};font-family:S;color:{NOCHE}}}
.hero{{background:radial-gradient(circle at 80% 20%,#2A2370 0,{NOCHE} 60%);padding:90px 100px;color:{LUNA}}}
.hero svg{{width:720px;height:auto}} .hero p{{font-size:30px;opacity:.85;margin:24px 0 0}}
.sec{{padding:60px 100px}} h2{{font-family:U;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:{NEBULOSA};margin:0 0 28px}}
.pal{{display:flex;gap:22px}} .sw{{flex:1;border-radius:26px;overflow:hidden;box-shadow:0 10px 30px #12123a22;background:#fff}}
.sw div{{height:170px}} .sw p{{margin:14px 18px;font-size:20px}} .sw b{{font-family:SB;display:block;font-size:22px}}
.t1{{font-family:UX;font-size:84px;line-height:1.05;margin:0}} .t2{{font-family:SB;font-size:34px;margin:18px 0 6px}} .t3{{font-size:24px;line-height:1.5;max-width:1100px}}
.row{{display:flex;gap:30px;align-items:center}} .box{{border-radius:28px;padding:30px;display:flex;align-items:center;justify-content:center}}
.btn{{display:inline-block;background:{AMBAR};color:{NOCHE};font-family:SB;font-size:26px;padding:20px 40px;border-radius:999px}}
.chip{{display:inline-block;background:{NEBULOSA};color:#fff;font-family:SB;font-size:20px;padding:10px 20px;border-radius:999px;margin-right:10px}}
</style></head><body>
<div class="hero">{VARIANTES['orbiluz-logo-noche'].replace(f'<rect width="100%" height="100%" fill="{NOCHE}"/>','')}<p>Objetos que iluminan y sorprenden · Decoración original para tu casa</p></div>
<div class="sec"><h2>Paleta</h2><div class="pal">
<div class="sw"><div style="background:{NOCHE}"></div><p><b>Noche</b>{NOCHE} · fondos, texto</p></div>
<div class="sw"><div style="background:{AMBAR}"></div><p><b>Ámbar</b>{AMBAR} · botones, precio</p></div>
<div class="sw"><div style="background:{NEBULOSA}"></div><p><b>Nebulosa</b>{NEBULOSA} · acentos</p></div>
<div class="sw"><div style="background:{LUNA}"></div><p><b>Luna</b>{LUNA} · fondo claro</p></div>
<div class="sw"><div style="background:{CORAL}"></div><p><b>Coral</b>{CORAL} · ofertas</p></div>
<div class="sw"><div style="background:{NIEBLA}"></div><p><b>Niebla</b>{NIEBLA} · líneas, texto 2º</p></div></div></div>
<div class="sec"><h2>Tipografía</h2><p class="t1">Unbounded · Titulares</p><p class="t2">DM Sans Bold · Subtítulos y botones</p>
<p class="t3">DM Sans Regular · Textos. Las dos son de Google Fonts (licencia OFL, uso comercial libre) y ya están en el tema de Shopify.</p></div>
<div class="sec"><h2>Versiones del logo</h2><div class="row">
<div class="box" style="background:{NOCHE};width:520px">{VARIANTES['orbiluz-logo-blanco'].replace('<svg ','<svg style="width:420px;height:auto" ')}</div>
<div class="box" style="background:#fff;width:520px">{VARIANTES['orbiluz-logo-negro'].replace('<svg ','<svg style="width:420px;height:auto" ')}</div>
<div class="box" style="background:transparent">{VARIANTES['orbiluz-icono'].replace('<svg ','<svg style="width:180px;height:auto" ')}</div></div></div>
<div class="sec"><h2>Estilo</h2><div class="row"><span class="btn">Añadir al carrito</span><span class="chip">Envío GRATIS +39 €</span><span class="chip" style="background:{CORAL}">-10 % BIENVENIDA</span></div>
<p class="t3">Tono: cercano, curioso y con un punto de humor. Frases cortas, tuteo. Fotos: producto encendido en ambiente nocturno cálido, fondos oscuros con brillo ámbar o morado.</p></div>
</body></html>"""

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    for k, v in VARIANTES.items(): open(f"{OUT}/{k}.svg", "w").write(v)
    open(f"{D}/hoja-de-marca.html", "w").write(HOJA)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")); pg = b.new_page(device_scale_factor=2)
        for k, v in VARIANTES.items():
            pg.set_content(f'<html><body style="margin:0;background:transparent">{v}</body></html>')
            pg.locator("svg").screenshot(path=f"{OUT}/{k}.png", omit_background=True)
        pg = b.new_page(viewport={"width": 1600, "height": 900})
        pg.goto(f"file://{D}/hoja-de-marca.html"); pg.wait_for_timeout(400)
        pg.screenshot(path=f"{D}/hoja-de-marca.png", full_page=True)
        b.close()
    print("ok")
