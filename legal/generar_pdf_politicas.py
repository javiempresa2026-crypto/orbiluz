"""Genera legal/politicas-orbiluz.pdf a partir de politicas-para-pegar.html (+ política de cookies).
Uso: python3 legal/generar_pdf_politicas.py"""
import os, re, datetime
from playwright.sync_api import sync_playwright

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
SRC = open(f"{ROOT}/politicas-para-pegar.html", encoding="utf-8").read()
F = f"file://{ROOT}/marca/fuentes"
LOGO = f"file://{ROOT}/marca/logo/horizontal/orbiluz-horizontal-para-fondo-claro-1200.png"
CHROME = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

bloques = dict(re.findall(r'<div class="b" id="(\w+)">(.*?)</div></section>', SRC, re.S))
COOKIES = """<h2>Política de cookies</h2><p>Esta web usa cookies propias y de terceros. Una cookie es un pequeño archivo que se guarda en tu navegador.</p>
<h3>Qué cookies usamos</h3><ul><li><strong>Técnicas (necesarias)</strong>: hacen que la tienda funcione: carrito, pago, idioma y seguridad. Las instala Shopify y no necesitan tu consentimiento.</li>
<li><strong>Analíticas</strong>: nos ayudan a entender cómo se usa la web (páginas vistas, origen de las visitas). Solo se activan si las aceptas.</li>
<li><strong>Publicitarias</strong>: permiten medir y mostrar anuncios de nuestros productos en redes sociales. Solo se activan si las aceptas.</li></ul>
<h3>Cómo gestionarlas</h3><p>Al entrar por primera vez puedes aceptar o rechazar las cookies no necesarias en el aviso de cookies. También puedes borrarlas o bloquearlas desde la configuración de tu navegador.</p>
<h3>Más información</h3><p>Consulta la política de privacidad o escríbenos a orbiluzsupport@gmail.com.</p>"""
orden = [("pl", "Aviso legal"), ("pt", "Condiciones generales de venta"), ("pr", "Política de devoluciones y desistimiento"),
         ("ps", "Política de envíos"), ("pp", "Política de privacidad"), ("ck", "Política de cookies"), ("pc", "Información de contacto")]
bloques["ck"] = COOKIES
def completar(h):
    return re.sub(r'href="/', 'href="https://orbiluz.myshopify.com/', h)

hoy = datetime.date.today().strftime("%d/%m/%Y")
indice = "".join(f'<li><a href="#{k}">{t}</a></li>' for k, t in orden)
cuerpo = "".join(f'<section id="{k}">{completar(bloques[k])}</section>' for k, _ in orden)
html = f"""<html lang="es"><head><meta charset="utf-8"><style>
@font-face{{font-family:U;src:url({F}/Unbounded-Bold.ttf)}}
@font-face{{font-family:D;src:url({F}/DMSans-Regular.ttf)}}
@font-face{{font-family:D;font-weight:700;src:url({F}/DMSans-Bold.ttf)}}
@page{{size:A4;margin:22mm 20mm 20mm}}
body{{font-family:D;color:#12123A;font-size:10.5pt;line-height:1.55}}
.cover{{height:245mm;display:flex;flex-direction:column;justify-content:center;page-break-after:always}}
.cover img{{width:95mm}} .cover h1{{font-family:U;font-size:26pt;margin:14mm 0 4mm}}
.cover p{{color:#555;font-size:11pt;margin:2mm 0}} .cover ol{{margin-top:10mm;font-size:12pt;line-height:2}}
.cover a{{color:#12123A;text-decoration:none}}
.nota{{margin-top:10mm;background:#FFF6E9;border-left:4px solid #FFB547;padding:4mm 5mm;font-size:10pt}}
section{{page-break-before:always}}
h2{{font-family:U;font-size:17pt;margin:0 0 6mm;padding-bottom:3mm;border-bottom:3px solid #FFB547}}
h3{{font-size:12pt;margin:6mm 0 2mm;color:#2A2370}}
a{{color:#2A2370}} li{{margin:1mm 0}} mark{{background:#FFE9A8;padding:0 2px}}
</style></head><body>
<div class="cover"><img src="{LOGO}"><h1>Textos legales</h1>
<p>Tienda online Orbiluz · orbiluz.myshopify.com</p><p>Versión del {hoy}</p><ol>{indice}</ol></div>
{cuerpo}</body></html>"""
tmp = f"{ROOT}/legal/.tmp.html"; open(tmp, "w", encoding="utf-8").write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME); pg = b.new_page()
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(600)
    pg.pdf(path=f"{ROOT}/legal/politicas-orbiluz.pdf", format="A4", print_background=True, display_header_footer=True,
           header_template="<span></span>",
           footer_template='<div style="font-family:Arial;font-size:8px;color:#888;width:100%;text-align:center">Orbiluz · Textos legales · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
           margin={"top": "22mm", "bottom": "20mm", "left": "20mm", "right": "20mm"})
    b.close()
os.remove(tmp); print("ok")
