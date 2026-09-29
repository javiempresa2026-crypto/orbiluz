"""Carrusel de Instagram «La luz del techo» (7 diapositivas, 1080x1350).
Renderiza HTML con las fuentes de la marca y guarda JPG en contenido/carruseles/luz-del-techo/.
Uso: python3 contenido/carruseles/generar_carrusel.py"""
import os
from playwright.sync_api import sync_playwright

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = f"{ROOT}/contenido/carruseles/luz-del-techo"
F = f"file://{ROOT}/marca/fuentes"
CHROME = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
LOGO = f"file://{ROOT}/marca/logo/horizontal/orbiluz-horizontal-para-fondo-oscuro-600.png"
STARS = f"file://{ROOT}/tema/assets/orbiluz-fondo-noche.svg"
IMG = {
    "techo": f"file://{ROOT}/anuncios/meta/escenas/escena-3.jpg",
    "mano": f"file://{ROOT}/anuncios/meta/escenas/escena-0.jpg",
    "mesilla": f"file://{ROOT}/anuncios/meta/escenas/escena-1.jpg",
    "modelos": f"file://{ROOT}/fotos/lampara-4-modelos.jpg",
    "apagada": f"file://{OUT}/fondos/noche-apagada.jpg",
    "encendida": f"file://{OUT}/fondos/noche-encendida.jpg",
}

CSS = f"""
@font-face{{font-family:U;src:url({F}/Unbounded-Bold.ttf)}}
@font-face{{font-family:D;src:url({F}/DMSans-Regular.ttf)}}
@font-face{{font-family:D;font-weight:700;src:url({F}/DMSans-Bold.ttf)}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;overflow:hidden;background:#12123A;color:#FFF6E9;font-family:D;position:relative}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.shade-top{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,40,.92) 0%,rgba(10,10,40,.65) 38%,rgba(10,10,40,0) 62%)}}
.shade-bot{{position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,10,40,.95) 0%,rgba(10,10,40,.7) 40%,rgba(10,10,40,0) 65%)}}
.shade-all{{position:absolute;inset:0;background:rgba(10,10,40,.55)}}
.stars{{position:absolute;inset:0;background:url({STARS}) repeat;background-size:520px;opacity:.9}}
.pad{{position:absolute;left:84px;right:84px}}
.top{{top:120px}} .bot{{bottom:150px}}
h1{{font-family:U;font-size:74px;line-height:1.08;letter-spacing:-.01em}}
h2{{font-family:U;font-size:60px;line-height:1.1;letter-spacing:-.01em}}
p{{font-size:36px;line-height:1.38;color:#EDE9FF;margin-top:28px}}
.amb{{color:#FFB547}} .neb{{color:#B7AEFF}}
.logo{{position:absolute;left:84px;top:52px;height:40px}}
.num{{position:absolute;right:84px;top:58px;font:700 26px D;color:#A7A9C9;letter-spacing:.08em}}
.dots{{position:absolute;left:0;right:0;bottom:64px;display:flex;justify-content:center;gap:12px}}
.dots i{{width:12px;height:12px;border-radius:50%;background:rgba(255,246,233,.35)}}
.dots i.on{{background:#FFB547;width:36px;border-radius:6px}}
.swipe{{display:inline-flex;align-items:center;gap:14px;margin-top:40px;font:700 30px D;color:#12123A;background:#FFB547;border-radius:999px;padding:16px 30px}}
.tag{{display:inline-block;font:700 24px D;letter-spacing:.14em;text-transform:uppercase;color:#FFB547;background:rgba(255,181,71,.14);border-radius:999px;padding:10px 20px;margin-bottom:28px}}
.split{{position:absolute;left:0;right:0;height:50%;overflow:hidden}}
.split img{{width:100%;height:100%;object-fit:cover}}
.label{{position:absolute;left:84px;font:700 28px D;padding:10px 22px;border-radius:999px}}
.cta{{display:grid;gap:22px;margin-top:48px}}
.cta div{{display:flex;gap:22px;align-items:center;font-size:34px;line-height:1.3;color:#EDE9FF;background:rgba(18,18,58,.82);border:1px solid rgba(255,246,233,.18);border-radius:28px;padding:26px 30px}}
.cta b{{flex:none;display:grid;place-items:center;width:62px;height:62px;border-radius:50%;background:#FFB547;color:#12123A;font:700 30px U}}
"""

def page(n, body):
    dots = "".join(f'<i class="{"on" if i == n else ""}"></i>' for i in range(1, 8))
    return (f'<html><head><style>{CSS}</style></head><body>{body}'
            f'<img class="logo" src="{LOGO}"><div class="num">{n}/7</div><div class="dots">{dots}</div></body></html>')

SLIDES = [
    # 1 · Gancho
    f'''<img class="bg" src="{IMG["techo"]}"><div class="shade-top"></div>
    <div class="pad top"><h1>Nadie te cuenta por qué tu habitación <span class="amb">nunca se ve como en Pinterest.</span></h1>
    <div class="swipe">Desliza →</div></div>''',
    # 2 · Problema
    f'''<img class="bg" src="{IMG["apagada"]}" style="object-position:50% 60%"><div class="shade-top"></div>
    <div class="pad top"><h2>Compraste los cojines. La manta. La planta que sigue viva de milagro.</h2>
    <p>Y a las once de la noche enciendes la luz del techo… y tu cuarto parece <b class="amb">la sala de espera del dentista.</b></p></div>''',
    # 3 · Nueva mirada
    f'''<img class="bg" src="{IMG["mesilla"]}" style="object-position:50% 70%"><div class="shade-top"></div>
    <div class="pad top"><h1>No te falta decoración.<br><span class="amb">Te sobra luz de techo.</span></h1>
    <p>La luz de arriba lo aplana todo: sin rincones, sin ambiente, sin ese momento de «ahora sí, me quedo aquí».</p></div>''',
    # 4 · Contraste
    f'''<div class="split" style="top:0"><img src="{IMG["techo"]}" style="object-position:50% 35%"></div>
    <div class="split" style="bottom:0"><img src="{IMG["encendida"]}" style="object-position:50% 62%"></div>
    <div class="shade-all" style="background:linear-gradient(180deg,rgba(10,10,40,.8) 0%,rgba(10,10,40,.1) 30%,rgba(10,10,40,.1) 70%,rgba(10,10,40,.85) 100%)"></div>
    <div class="label" style="top:560px;background:#E9EEF5;color:#12123A">Luz de techo</div>
    <div class="label" style="top:700px;background:#FFB547;color:#12123A">Luz baja y cálida</div>
    <div class="pad" style="top:130px"><h2>Una luz es para ver.</h2></div>
    <div class="pad" style="bottom:120px"><h2 class="amb">La otra, para quedarse.</h2></div>''',
    # 5 · Idea central
    f'''<img class="bg" src="{IMG["mano"]}" style="object-position:50% 60%"><div class="shade-top"></div>
    <div class="pad top"><h2>Las habitaciones que te enamoran no tienen más cosas.</h2>
    <p style="font-size:44px;font-family:U;line-height:1.15;color:#FFB547">Tienen un punto de luz<br>que se mira.</p></div>''',
    # 6 · Marca
    f'''<img class="bg" src="{IMG["modelos"]}" style="object-position:50% 40%"><div class="shade-bot"></div>
    <div class="pad bot"><span class="tag">Orbiluz</span><h2>Por eso hicimos <span class="amb">decoración que se enciende.</span></h2>
    <p>Un planeta, una luna o una galaxia en tu mesilla. Apagas la de arriba y la habitación cambia.</p></div>''',
    # 7 · Llamada a la acción
    f'''<img class="bg" src="{IMG["encendida"]}" style="object-position:50% 20%;opacity:.5"><div class="stars" style="opacity:.5"></div>
    <div class="pad top" style="top:150px"><h1>Esta noche, <span class="amb">apaga la de arriba.</span></h1>
    <div class="cta"><div><b>1</b>Guárdalo para cuando cambies tu cuarto</div>
    <div><b>2</b>Mándaselo a quien vive con la luz del techo puesta</div>
    <div><b>3</b>Elige tu planeta en el enlace de la bio</div></div></div>''',
]

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, body in enumerate(SLIDES, 1):
            tmp = f"{OUT}/.tmp.html"; open(tmp, "w").write(page(i, body))
            pg.goto(f"file://{tmp}"); pg.wait_for_timeout(500)
            pg.screenshot(path=f"{OUT}/slide-{i}.jpg", type="jpeg", quality=92); os.remove(tmp)
        b.close()
    print("ok")

if __name__ == "__main__":
    main()
