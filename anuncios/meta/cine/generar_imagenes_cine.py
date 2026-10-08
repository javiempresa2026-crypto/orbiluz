"""Anuncios de imagen de la campaña «Cinemática»: foto a sangre, titular grande y botón, en 4:5 (feed) y 9:16 (Historias y Reels).
En 9:16 el texto queda dentro de la zona segura (sin 250 px arriba ni 380 px abajo). Sin precios.
Uso: python3 anuncios/meta/cine/generar_imagenes_cine.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "contenido", "carruseles"))
from playwright.sync_api import sync_playwright
from generar_carrusel import CHROME, ROOT

OUT = os.path.dirname(os.path.abspath(__file__))
FU = f"file://{ROOT}/marca/fuentes"
TT = f"file://{ROOT}/marca/fuentes/ugc/TikTokSans%5Bopsz,slnt,wdth,wght%5D.ttf"
LOGO = f"file://{ROOT}/marca/logo/horizontal/orbiluz-horizontal-para-fondo-oscuro-600.png"
M = f"file://{OUT}/material"

ANUNCIOS = {
    "I1-grabado-dentro": (f"{M}/h1-lampara-macro.png", "50% 45%",
        'Grabado <span class="amb">dentro</span> del cristal.', "Bola de 5 cm con Saturno, la Luna, una galaxia o el sistema solar. Luz cálida por USB."),
    "I2-tu-techo": (f"{M}/h2-proyector-techo.png", "50% 74%",
        'Tu techo <span class="amb">puede hacer esto.</span>', "Olas que se mueven · 16 colores · mando a distancia"),
    "I3-flota-gira-brilla": (f"{M}/h3-globo-oscuridad.png", "50% 40%",
        'Flota. Gira. <span class="amb">Brilla.</span>', "Globo de 14 cm con levitación magnética. Sin hilos ni soportes."),
    "I4-cambia-la-luz": (f"{M}/h4-los-cuatro.png", "60% 50%",
        'Deja de comprar cojines. <span class="amb">Cambia la luz.</span>', "Lámpara planeta · Proyector de olas · Globo que levita · Reloj 3D"),
}

CSS = f"""
@font-face{{font-family:U;src:url({FU}/Unbounded-Bold.ttf)}}
@font-face{{font-family:T;src:url({TT})}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;overflow:hidden;background:#0B0B22;color:#FFF6E9;position:relative;font-family:T;font-variation-settings:'wght' 500}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.top{{position:absolute;left:0;right:0;top:0;height:62%;background:linear-gradient(180deg,rgba(8,8,26,.92) 0%,rgba(8,8,26,.55) 45%,rgba(8,8,26,0) 100%)}}
.bot{{position:absolute;left:0;right:0;bottom:0;height:40%;background:linear-gradient(0deg,rgba(8,8,26,.92) 0%,rgba(8,8,26,0) 100%)}}
.txt{{position:absolute;left:72px;right:72px}}
h1{{font-family:U;font-size:78px;line-height:1.05;letter-spacing:-.015em;text-shadow:0 4px 30px rgba(0,0,0,.5)}}
p{{font-size:34px;line-height:1.35;color:#EDE9FF;margin-top:22px;font-variation-settings:'wght' 600}}
.amb{{color:#FFB547}}
.cta{{position:absolute;left:0;right:0;text-align:center}}
.pill{{display:inline-block;font:36px T;font-variation-settings:'wght' 800;color:#12123A;background:#FFB547;border-radius:999px;padding:20px 46px}}
.small{{display:block;text-align:inherit;font-size:26px;color:#C9C7E6;margin-top:16px}}
.logo{{height:40px;margin-bottom:26px}}
"""

def html(img, pos, titulo, sub, alto, cta_abajo=False):
    top, bottom = (70, 70) if alto == 1350 else (260, 390)
    boton = ('<span class="pill">Descúbrelo en orbiluz.com</span>'
             '<span class="small">Envío con seguimiento · 14 días para devolver</span>')
    # en 9:16 el botón va bajo el texto, para que no tape el producto en la parte de abajo
    cta_arriba = f'<div style="margin-top:34px">{boton}</div>'
    return (f'<html><head><style>{CSS} body{{height:{alto}px}}</style></head><body>'
            f'<img class="bg" src="{img}" style="object-position:{pos}"><div class="top"></div><div class="bot"></div>'
            f'<div class="txt" style="top:{top}px"><img class="logo" src="{LOGO}"><h1>{titulo}</h1><p>{sub}</p>'
            + (cta_arriba if alto == 1920 and not cta_abajo else '') + '</div>'
            + ('' if alto == 1920 and not cta_abajo else f'<div class="cta" style="bottom:{bottom}px">{boton}</div>') + '</body></html>')

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        for nombre, (img, pos, titulo, sub) in ANUNCIOS.items():
            for alto, suf in ((1350, "4x5"), (1920, "9x16")):
                pg = b.new_page(viewport={"width": 1080, "height": alto})
                tmp = f"{OUT}/.tmp.html"; open(tmp, "w").write(html(img, pos, titulo, sub, alto, cta_abajo=nombre.startswith("I3")))
                pg.goto(f"file://{tmp}"); pg.wait_for_timeout(800)
                pg.screenshot(path=f"{OUT}/{nombre}-{suf}.jpg", type="jpeg", quality=92); os.remove(tmp); pg.close()
            print(nombre)
        b.close()

if __name__ == "__main__":
    main()
