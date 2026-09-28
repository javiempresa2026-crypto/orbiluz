"""Kit completo de logos de Orbiluz: todas las versiones en SVG y PNG a varios tamaños,
iconos, favicon y piezas para redes. Usa las mismas funciones que generar_marca.py.
Uso: python3 marca/generar_kit_logos.py"""
import os, re, io
from generar_marca import logo_svg, icon_svg, planet, word_paths, D, NOCHE, NEBULOSA, AMBAR, LUNA, NIEBLA

K = f"{D}/logo"
STARS = os.path.normpath(os.path.join(D, "..", "tema", "assets", "orbiluz-fondo-noche.svg"))
CHROME = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

def planet_mono(cx, cy, r, col, uid, tilt=-22):
    """Planeta a una tinta: se recorta una franja del cuerpo alrededor del anillo delantero para que se lea la órbita."""
    rx, ry, w = r * 1.62, r * 0.42, r * 0.2
    front = f"M {rx} 0 A {rx} {ry} 0 0 1 {-rx} 0"
    back = f"M {-rx} 0 A {rx} {ry} 0 0 1 {rx} 0"
    cut = f"M {rx*0.93} {ry*0.37} A {rx} {ry} 0 0 1 {-rx*0.93} {ry*0.37}"
    return (f'<defs><mask id="{uid}" maskUnits="userSpaceOnUse" x="{cx-3*r}" y="{cy-3*r}" width="{6*r}" height="{6*r}">'
            f'<rect x="{cx-3*r}" y="{cy-3*r}" width="{6*r}" height="{6*r}" fill="#fff"/>'
            f'<g transform="translate({cx} {cy}) rotate({tilt})"><path d="{cut}" fill="none" stroke="#000" stroke-width="{w*2.1}"/></g></mask></defs>'
            f'<g transform="translate({cx} {cy}) rotate({tilt})"><path d="{back}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/></g>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" mask="url(#{uid})"/>'
            f'<g transform="translate({cx} {cy}) rotate({tilt})"><path d="{front}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/></g>')

def logo_mono(col, size=200):
    d, w, xh = word_paths("rbiluz", f"{D}/fuentes/Unbounded-Bold.ttf", size)
    r = xh * 0.56; pad = r * 1.9; gap = r * 0.55
    W = pad + r + gap + w + size * 0.12; H = size * 1.5; base = size * 1.05
    cx, cy = pad, base - xh / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">'
            f'{planet_mono(cx, cy, r, col, "m" + col.strip("#"))}'
            f'<path transform="translate({cx + r + gap:.1f} {base:.1f})" d="{d}" fill="{col}"/></svg>')

def icon_mono(col, size=512):
    c = size / 2; r = size * 0.24
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">{planet_mono(c, c, r, col, "i" + col.strip("#"))}</svg>'

def icon_transparente(body, ring, size=512):
    c = size / 2; r = size * 0.24
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">{planet(c, c, r, body, ring)}</svg>'

HORIZONTAL = {
    # nombre: (svg, descripción)
    "orbiluz-horizontal-fondo-noche": (logo_svg(LUNA, AMBAR, NEBULOSA, NOCHE), "Principal, con fondo noche"),
    "orbiluz-horizontal-fondo-luna": (logo_svg(NOCHE, AMBAR, NEBULOSA, LUNA), "Principal, con fondo claro"),
    "orbiluz-horizontal-para-fondo-oscuro": (logo_svg(LUNA, AMBAR, NEBULOSA), "Transparente, texto claro (sobre fotos o fondos oscuros)"),
    "orbiluz-horizontal-para-fondo-claro": (logo_svg(NOCHE, AMBAR, NEBULOSA), "Transparente, texto noche (sobre fondos claros)"),
    "orbiluz-horizontal-blanco": (logo_mono("#FFFFFF"), "Monocromo blanco (sellos, vídeo, fotos)"),
    "orbiluz-horizontal-negro": (logo_mono(NOCHE), "Monocromo noche (impresión a una tinta, grabado)"),
}
ICONO = {
    "orbiluz-icono-fondo-noche-redondeado": (icon_svg(NOCHE, AMBAR, NEBULOSA), "App, favicon"),
    "orbiluz-icono-fondo-noche-cuadrado": (icon_svg(NOCHE, AMBAR, NEBULOSA, round_=False), "Perfil de redes (se recorta en círculo)"),
    "orbiluz-icono-fondo-luna": (icon_svg(LUNA, AMBAR, NEBULOSA, round_=False), "Perfil sobre fondo claro"),
    "orbiluz-icono-transparente": (icon_transparente(AMBAR, NEBULOSA), "Planeta a color, sin fondo"),
    "orbiluz-icono-blanco": (icon_mono("#FFFFFF"), "Planeta blanco, sin fondo"),
    "orbiluz-icono-negro": (icon_mono(NOCHE), "Planeta noche, sin fondo"),
}

def sized(svg, width):
    w = float(re.search(r'width="([\d.]+)"', svg).group(1)); h = float(re.search(r'height="([\d.]+)"', svg).group(1))
    hh = round(width * h / w)
    svg = re.sub(r'width="[\d.]+"', f'width="{width}"', svg, count=1)
    return re.sub(r'height="[\d.]+"', f'height="{hh}"', svg, count=1), hh

def render(pg, svg, width, path):
    s, h = sized(svg, width)
    pg.set_viewport_size({"width": width, "height": h})
    pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>')
    pg.locator("svg").screenshot(path=path, omit_background=True)

def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    for sub in ("horizontal", "icono", "favicon", "redes"):
        os.makedirs(f"{K}/{sub}", exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME); pg = b.new_page()
        for name, (svg, _) in HORIZONTAL.items():
            open(f"{K}/horizontal/{name}.svg", "w").write(svg)
            for w in (600, 1200, 2400):
                render(pg, svg, w, f"{K}/horizontal/{name}-{w}.png")
        for name, (svg, _) in ICONO.items():
            open(f"{K}/icono/{name}.svg", "w").write(svg)
            for w in (180, 512, 1024):
                render(pg, svg, w, f"{K}/icono/{name}-{w}.png")
        # favicon
        fav = ICONO["orbiluz-icono-fondo-noche-redondeado"][0]
        for w in (16, 32, 48, 180, 192, 512):
            render(pg, fav, w, f"{K}/favicon/favicon-{w}.png")
        Image.open(f"{K}/favicon/favicon-48.png").save(f"{K}/favicon/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
        os.rename(f"{K}/favicon/favicon-180.png", f"{K}/favicon/apple-touch-icon-180.png")
        # redes
        render(pg, ICONO["orbiluz-icono-fondo-noche-cuadrado"][0], 1080, f"{K}/redes/perfil-1080.png")
        logo = logo_svg(LUNA, AMBAR, NEBULOSA)
        for name, (W, H), tag in (("portada-facebook-1640x624", (1640, 624), "Decoración que se enciende"),
                                  ("imagen-compartir-1200x630", (1200, 630), "Decoración que se enciende"),
                                  ("portada-youtube-2560x1440", (2560, 1440), "Decoración que se enciende")):
            lw = int(W * 0.42)
            s, _ = sized(logo, lw)
            html = (f'<html><head><style>@font-face{{font-family:S;src:url(file://{D}/fuentes/DMSans-Bold.ttf)}}</style></head>'
                    f'<body style="margin:0;width:{W}px;height:{H}px;display:flex;flex-direction:column;align-items:center;justify-content:center;'
                    f'background:radial-gradient(circle at 78% 22%,#2A2370 0,{NOCHE} 58%);font-family:S;color:{NIEBLA}">'
                    f'{s}<div style="margin-top:{int(H*0.03)}px;font-size:{int(W*0.022)}px;letter-spacing:.04em">{tag}</div></body></html>')
            html = html.replace('<body style="', '<body style="background-image:url(file://' + STARS + '),radial-gradient(circle at 78% 22%,#2A2370 0,' + NOCHE + ' 58%);background-size:520px 520px,auto;')
            tmp = f"{D}/.tmp-portada.html"; open(tmp, "w").write(html)
            pg.set_viewport_size({"width": W, "height": H}); pg.goto(f"file://{tmp}"); pg.wait_for_timeout(400); os.remove(tmp)
            pg.screenshot(path=f"{K}/redes/{name}.png")
        b.close()
    print("ok")

if __name__ == "__main__":
    main()
