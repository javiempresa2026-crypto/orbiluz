"""Campaña de imágenes de Black Friday (23-30 de noviembre). Solo imágenes, sin precios: la oferta va en porcentaje.
Tipografía «viral» de los vídeos (mayúsculas, palabra clave en recuadro amarillo) sobre fondos oscurecidos tipo «black»,
con sello «BLACK FRIDAY» arriba y una pegatina con el descuento.
Cada imagen en 4:5 (feed) y 9:16 (Historias y Reels, todo dentro de la zona segura).
Uso: python3 black-friday/imagenes/generar_black_friday.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tiktok"))
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
import textos_ugc as tx

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.dirname(os.path.abspath(__file__))
C = f"{ROOT}/anuncios/meta/cine/material"
U = f"{ROOT}/anuncios/meta/ugc/material"
H = f"{ROOT}/tiktok/historias/material"
NEGRO, AMARILLO, ORO = (0, 0, 0, 255), tx.AMARILLO, (255, 181, 71, 255)

# nombre: (fondo, foco vertical, gancho, etiqueta, pegatina (grande, pequeño) o None, sello superior)
IMAGENES = {
    "BF1-se-ve-a-oscuras": (f"{C}/h4-los-cuatro.png", 0.55, "Este año el Black Friday | se ve *a oscuras*",
                            "Del 23 al 30 de noviembre", None, "Muy pronto"),
    "BF2-oferta": (f"{C}/h4-los-cuatro.png", 0.55, "Llévate 2. | *Paga menos.*",
                   "−15 % en todo · −25 % llevando 2", ("−25 %", "llevando 2"), "Black Friday"),
    "BF3-lampara-regala-un-planeta": (f"{C}/h1-lampara-macro.png", 0.5, "Regala un *planeta* | este Black Friday",
                                      "Combina modelos y ahorra un 25 %", ("−25 %", "llevando 2"), "Black Friday"),
    "BF4-proyector-bajo-el-mar": (f"{C}/h2-proyector-techo.png", 0.62, "Tu techo, | *bajo el mar*",
                                  "Olas en movimiento · 16 colores", ("−15 %", "en todo"), "Black Friday"),
    "BF5-globo-que-flota": (f"{C}/h3-globo-oscuridad.png", 0.5, "El globo que *flota* | ahora con descuento",
                            "Levitación magnética · 14 cm", ("−15 %", "en todo"), "Black Friday"),
    "BF6-regalos-resueltos": (f"{U}/u1-caja-lampara.png", 0.6, "Los regalos de Navidad, | *resueltos*",
                              "Sin códigos · se aplica en el carrito", ("−25 %", "llevando 2"), "Black Friday"),
    "BF7-ultimo-dia": (f"{H}/c4-globo-final.png", 0.55, "*Último día* | de Black Friday",
                       "Termina hoy a las 23:59", ("−25 %", "llevando 2"), "Cyber Monday"),
}


def fondo(ruta, ancho, alto, foco):
    im = Image.open(ruta).convert("RGB")
    r = max(ancho / im.width, alto / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    y = int((im.height - alto) * foco)
    im = im.crop(((im.width - ancho) // 2, y, (im.width - ancho) // 2 + ancho, y + alto))
    # look «black»: menos saturación, más contraste, sombras casi negras y viñeta fuerte
    im = ImageEnhance.Color(im).enhance(0.85); im = ImageEnhance.Contrast(im).enhance(1.12)
    im = ImageEnhance.Brightness(im).enhance(0.82).convert("RGBA")
    capa = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0)); d = ImageDraw.Draw(capa)
    for i in range(alto):
        a = max(0, 1 - i / (alto * 0.45)) * 200 + max(0, (i - alto * 0.68) / (alto * 0.32)) * 170
        d.line([(0, i), (ancho, i)], fill=(3, 3, 8, int(min(225, a))))
    im.alpha_composite(capa)
    vin = Image.new("L", (ancho, alto), 0); ImageDraw.Draw(vin).ellipse((-ancho * 0.25, -alto * 0.1, ancho * 1.25, alto * 1.1), fill=255)
    vin = vin.filter(ImageFilter.GaussianBlur(160))
    negro = Image.new("RGBA", (ancho, alto), (0, 0, 0, 255))
    return Image.composite(im, negro, vin)


def sello(im, texto, y):
    """Sello «BLACK FRIDAY» arriba: texto blanco espaciado entre dos líneas doradas."""
    d = ImageDraw.Draw(im); f = tx.fuente(44, 900)
    t = "  ".join(texto.upper()); w = d.textlength(t, font=f)
    d.text((im.width / 2, y), t, font=f, fill=(255, 255, 255, 255), anchor="mm")
    for s in (-1, 1):
        x0 = im.width / 2 + s * (w / 2 + 30)
        d.line([(x0, y), (x0 + s * 90, y)], fill=ORO, width=4)


def pegatina(im, grande, peque, cx, cy, r=150):
    """Pegatina redonda amarilla con borde negro, ligeramente girada, con el porcentaje."""
    lado = r * 2 + 40
    p = Image.new("RGBA", (lado, lado), (0, 0, 0, 0)); d = ImageDraw.Draw(p)
    d.ellipse((20, 20, lado - 20, lado - 20), fill=AMARILLO, outline=NEGRO, width=9)
    d.ellipse((38, 38, lado - 38, lado - 38), outline=NEGRO, width=3)
    tam = 118
    while d.textlength(grande, font=tx.fuente(tam, 900)) > r * 1.6: tam -= 4
    d.text((lado / 2, lado / 2 - 18), grande, font=tx.fuente(tam, 900), fill=NEGRO, anchor="mm")
    d.text((lado / 2, lado / 2 + tam * 0.55), peque.upper(), font=tx.fuente(34, 850), fill=NEGRO, anchor="mm")
    p = p.rotate(10, resample=Image.BICUBIC, expand=True)
    sombra = Image.new("RGBA", p.size, (0, 0, 0, 0)); sombra.putalpha(p.getchannel("A").point(lambda a: a * 0.6))
    sombra = sombra.filter(ImageFilter.GaussianBlur(14))
    im.alpha_composite(sombra, (int(cx - p.width / 2 + 8), int(cy - p.height / 2 + 14)))
    im.alpha_composite(p, (int(cx - p.width / 2), int(cy - p.height / 2)))


def boton(im, y):
    d = ImageDraw.Draw(im); f = tx.fuente(46, 850)
    texto = "Ver ofertas en orbiluz.com"; w = d.textlength(texto, font=f)
    d.rounded_rectangle(((im.width - w) / 2 - 40, y - 42, (im.width + w) / 2 + 40, y + 42), radius=42, fill=ORO)
    d.text((im.width / 2, y), texto, font=f, fill=(18, 18, 58, 255), anchor="mm")


def main():
    for nombre, (ruta, foco, gancho, nota, peg, sello_txt) in IMAGENES.items():
        # 4:5: sello, gancho arriba, pegatina a la derecha, etiqueta y botón abajo.
        # 9:16: todo entre y=250 y y=1250 (zona segura de Historias y Reels); sin botón, Meta pone el suyo.
        for alto, suf, y_s, y_g, y_p, y_n, y_b in ((1350, "4x5", 80, 300, 820, 1080, 1225),
                                                    (1920, "9x16", 290, 500, 1000, 760, None)):
            im = fondo(ruta, tx.W, alto, foco)
            sello(im, sello_txt, y_s)
            tx.gancho_viral(im, gancho, 99, 1.0, y_centro=y_g)
            if peg: pegatina(im, *peg, cx=tx.W - 210, cy=y_p)
            tx.nota_viral(im, nota, 1.0, y=y_n)
            if y_b: boton(im, y_b)
            im.convert("RGB").save(f"{OUT}/{nombre}-{suf}.jpg", quality=92)
        print(nombre)


if __name__ == "__main__":
    main()
