"""Anuncios de imagen para Meta: problema explicado, comparativas, ventajas reales y antes/después.
Cada uno en 4:5 (1080x1350, feed) y 9:16 (1080x1920, Historias y Reels; el contenido queda dentro de la zona segura).
Todas las ventajas salen de la ficha real del producto. Sin precios.
Uso: python3 anuncios/meta/estaticos/generar_estaticos.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "contenido", "carruseles"))
from playwright.sync_api import sync_playwright
from generar_carrusel import CHROME, ROOT

OUT = os.path.dirname(os.path.abspath(__file__))
FU = f"file://{ROOT}/marca/fuentes"
LOGO = f"file://{ROOT}/marca/logo/horizontal/orbiluz-horizontal-para-fondo-oscuro-600.png"

def f(p): return f"file://{ROOT}/{p}"

IMG = {
    "antes": f("tiktok/historias/material/c0-cuarto-antes.png"),
    "lampara_cuarto": f("tiktok/historias/material/c1-lampara.png"),
    "final": f("tiktok/historias/material/c4-globo-final.png"),
    "calido": f("tiktok/historias/material/a3-cuarto-calido.png"),
    "regalos": f("tiktok/historias/material/b1-regalos-calcetines.png"),
    "saturno": f("fotos/lampara-saturno-noche.jpg"),
    "modelos": f("fotos/lampara-4-modelos.jpg"),
    "proyector": f("fotos/proyector-ondas-noche.jpg"),
    "proyector_cuarto": f("tiktok/historias/material/c3-proyector.png"),
}

CSS = f"""
@font-face{{font-family:U;src:url({FU}/Unbounded-Bold.ttf)}}
@font-face{{font-family:D;src:url({FU}/DMSans-Regular.ttf)}}
@font-face{{font-family:D;font-weight:700;src:url({FU}/DMSans-Bold.ttf)}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;overflow:hidden;background:#12123A;color:#FFF6E9;font-family:D;position:relative}}
.wrap{{position:absolute;left:0;right:0;display:flex;flex-direction:column}}
h1{{font-family:U;font-size:64px;line-height:1.08;letter-spacing:-.01em}}
h2{{font-family:U;font-size:44px;line-height:1.1}}
p{{font-size:34px;line-height:1.35;color:#EDE9FF}}
.amb{{color:#FFB547}}
.logo{{height:44px}}
.pill{{display:inline-block;font:700 30px D;color:#12123A;background:#FFB547;border-radius:999px;padding:16px 32px}}
.foto{{width:100%;object-fit:cover;display:block}}
.tag{{display:inline-block;font:700 24px D;letter-spacing:.12em;text-transform:uppercase;padding:10px 18px;border-radius:999px}}
.mal{{background:#E9EEF5;color:#12123A}} .bien{{background:#FFB547;color:#12123A}}
table{{width:100%;border-collapse:separate;border-spacing:0 12px;font-size:32px}}
td{{padding:18px 20px;background:rgba(255,255,255,.06)}}
td:first-child{{border-radius:18px 0 0 18px;color:#EDE9FF}}
td:last-child{{border-radius:0 18px 18px 0}}
td.c{{text-align:center;width:180px;font:700 40px D}}
.no{{color:#8C90B8}} .si{{color:#FFB547}}
.call{{position:absolute;background:rgba(18,18,58,.88);border:2px solid #FFB547;border-radius:22px;padding:16px 22px;font:700 30px D;max-width:440px}}
.call small{{display:block;font:400 26px D;color:#EDE9FF;margin-top:4px}}
"""

def cabecera(): return f'<img class="logo" src="{LOGO}">'

ANUNCIOS = {
    # E1 · PROBLEMA EXPLICADO → SOLUCIÓN
    "E1-sala-de-espera": lambda: f'''
      <div style="padding:0 64px 28px">{cabecera()}<h1 style="margin-top:26px">¿Por qué tu cuarto parece <span class="amb">una sala de espera?</span></h1></div>
      <div style="position:relative;height:560px">
        <img class="foto" src="{IMG["antes"]}" style="height:560px;object-position:50% 35%">
        <div class="call" style="left:40px;top:40px">1 · Luz desde arriba<small>Aplana todo, sin sombras</small></div>
        <div class="call" style="right:40px;top:215px">2 · Blanca y fría<small>Como la de una oficina</small></div>
        <div class="call" style="left:40px;bottom:40px">3 · Un solo punto de luz<small>Ningún rincón acogedor</small></div>
      </div>
      <div style="display:flex;gap:30px;align-items:center;padding:30px 64px 0">
        <img src="{IMG["lampara_cuarto"]}" style="width:250px;height:250px;object-fit:cover;object-position:20% 62%;border-radius:28px;border:3px solid #FFB547">
        <div><h2>La solución: <span class="amb">luz baja y cálida</span> en la mesilla.</h2>
        <div class="pill" style="margin-top:22px">Descúbrelo en orbiluz.com</div></div>
      </div>''',

    # E2 · COMPARATIVA: LUZ DEL TECHO vs LÁMPARA PLANETA
    "E2-techo-vs-lampara": lambda: f'''
      <div style="padding:0 64px">{cabecera()}<h1 style="margin-top:26px">De noche, <span class="amb">¿cuál enciendes?</span></h1></div>
      <div style="display:flex;gap:20px;padding:30px 64px 10px">
        <div style="flex:1"><img src="{IMG["antes"]}" style="width:100%;height:400px;object-fit:cover;object-position:50% 30%;border-radius:26px"><div class="tag mal" style="margin-top:14px">Luz del techo</div></div>
        <div style="flex:1"><img src="{IMG["saturno"]}" style="width:100%;height:400px;object-fit:cover;border-radius:26px;border:3px solid #FFB547"><div class="tag bien" style="margin-top:14px">Lámpara planeta</div></div>
      </div>
      <div style="padding:0 64px"><table>
        <tr><td></td><td class="c" style="font:700 24px D;background:none">Techo</td><td class="c" style="font:700 24px D;background:none;color:#FFB547">Planeta</td></tr>
        <tr><td>Luz cálida y suave</td><td class="c no">✕</td><td class="c si">✓</td></tr>
        <tr><td>A la altura de la mesilla</td><td class="c no">✕</td><td class="c si">✓</td></tr>
        <tr><td>Decora, también apagada</td><td class="c no">✕</td><td class="c si">✓</td></tr>
        <tr><td>Por USB, con 0,5 W</td><td class="c no">—</td><td class="c si">✓</td></tr>
      </table>
      <p style="font-size:26px;color:#A7A9C9;margin-top:6px">Bola de cristal de 5 cm con grabado láser 3D y base de madera.</p></div>''',

    # E3 · COMPARATIVA: EL REGALO DE SIEMPRE vs EL QUE SE RECUERDA
    "E3-regalo-de-siempre": lambda: f'''
      <div style="padding:0 64px">{cabecera()}<h1 style="margin-top:26px">Amigo invisible: <span class="amb">deja de fallar.</span></h1></div>
      <div style="display:flex;gap:20px;padding:30px 64px 10px">
        <div style="flex:1"><img src="{IMG["regalos"]}" style="width:100%;height:400px;object-fit:cover;object-position:40% 30%;border-radius:26px"><div class="tag mal" style="margin-top:14px">El de siempre</div></div>
        <div style="flex:1"><img src="{IMG["modelos"]}" style="width:100%;height:400px;object-fit:cover;object-position:50% 45%;border-radius:26px;border:3px solid #FFB547"><div class="tag bien" style="margin-top:14px">Un planeta</div></div>
      </div>
      <div style="padding:0 64px"><table>
        <tr><td></td><td class="c" style="font:700 24px D;background:none">Calcetines</td><td class="c" style="font:700 24px D;background:none;color:#FFB547">Planeta</td></tr>
        <tr><td>Se queda a la vista</td><td class="c no">✕</td><td class="c si">✓</td></tr>
        <tr><td>Se enciende cada noche</td><td class="c no">✕</td><td class="c si">✓</td></tr>
        <tr><td>Uno para cada persona (4 modelos)</td><td class="c no">✕</td><td class="c si">✓</td></tr>
        <tr><td>Acaba en un cajón</td><td class="c si">✓</td><td class="c no">✕</td></tr>
      </table></div>''',

    # E4 · VENTAJAS REALES DEL PROYECTOR (formato «razones»)
    "E4-proyector-ventajas": lambda: f'''
      <div style="padding:0 64px">{cabecera()}<h1 style="margin-top:26px">Tu techo, <span class="amb">bajo el mar.</span></h1>
      <p style="margin-top:14px">Apaga la luz: el agua se mueve sola por el techo y las paredes.</p></div>
      <div style="position:relative;height:760px;margin-top:30px">
        <img class="foto" src="{IMG["proyector_cuarto"]}" style="height:760px;object-position:50% 40%">
        <div class="call" style="left:40px;top:40px">🌊 Ondas en movimiento<small>Un disco interior gira bajo el cristal</small></div>
        <div class="call" style="right:40px;top:230px">🎨 16 colores<small>Y brillo regulable con mando</small></div>
        <div class="call" style="left:40px;top:430px">👆 Botón táctil<small>Para no buscar el mando</small></div>
        <div class="call" style="right:40px;bottom:40px">🔌 Por USB<small>Vale el cargador del móvil</small></div>
      </div>''',

    # E5 · ANTES / DESPUÉS DEL MISMO CUARTO
    "E5-antes-despues": lambda: f'''
      <div style="padding:0 64px">{cabecera()}<h1 style="margin-top:26px">Mismo cuarto. <span class="amb">4 cosas.</span></h1></div>
      <div style="display:flex;gap:16px;padding:30px 40px 0">
        <div style="flex:1;position:relative"><img src="{IMG["antes"]}" style="width:100%;height:860px;object-fit:cover;object-position:55% 50%;border-radius:26px">
          <div class="tag mal" style="position:absolute;left:18px;top:18px">Antes</div></div>
        <div style="flex:1;position:relative"><img src="{IMG["final"]}" style="width:100%;height:860px;object-fit:cover;object-position:55% 50%;border-radius:26px;border:3px solid #FFB547">
          <div class="tag bien" style="position:absolute;left:18px;top:18px">Después</div></div>
      </div>
      <p style="padding:22px 64px 0;font-size:30px">Lámpara planeta · Reloj 3D · Proyector de olas · Globo que levita</p>''',
}

def html(cuerpo, alto):
    # 4:5: contenido centrado. 9:16: contenido dentro de la zona segura (sin 250 px arriba ni 340 px abajo)
    top = 60 if alto == 1350 else 220
    pie = ("" if alto == 1350 or "pill" in cuerpo else
           '<div style="position:absolute;left:0;right:0;bottom:270px;text-align:center">'
           '<div class="pill" style="font-size:36px;padding:20px 44px">orbiluz.com</div>'
           '<p style="font-size:28px;color:#A7A9C9;margin-top:18px">Envío con seguimiento · 14 días para devolver</p></div>')
    return (f'<html><head><style>{CSS} body{{height:{alto}px}}</style></head><body>'
            f'<div class="wrap" style="top:{top}px">{cuerpo}</div>{pie}</body></html>')

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        for nombre, fn in ANUNCIOS.items():
            for alto, suf in ((1350, "4x5"), (1920, "9x16")):
                pg = b.new_page(viewport={"width": 1080, "height": alto})
                tmp = f"{OUT}/.tmp.html"; open(tmp, "w").write(html(fn(), alto))
                pg.goto(f"file://{tmp}"); pg.wait_for_timeout(700)
                pg.screenshot(path=f"{OUT}/{nombre}-{suf}.jpg", type="jpeg", quality=92); os.remove(tmp); pg.close()
            print(nombre)
        b.close()

if __name__ == "__main__":
    main()
