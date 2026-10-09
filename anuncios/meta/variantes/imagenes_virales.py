"""Anuncios de imagen con la tipografía «viral» de los vídeos (gancho en mayúsculas con palabra clave en recuadro amarillo).
Cada uno en 4:5 (feed) y 9:16 (Historias y Reels, todo dentro de la zona segura). Sin precios.
Uso: python3 anuncios/meta/variantes/imagenes_virales.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tiktok"))
from PIL import Image, ImageDraw, ImageEnhance
import textos_ugc as tx

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
OUT = os.path.dirname(os.path.abspath(__file__))
C = f"{ROOT}/anuncios/meta/cine/material"
U = f"{ROOT}/anuncios/meta/ugc/material"
H = f"{ROOT}/tiktok/historias/material"

IMAGENES = {
    "S1-piscina": (f"{C}/h2-proyector-techo.png", 0.62, "Dormir en el fondo | de una *piscina*", "16 colores · con mando"),
    "S2-sin-explicacion": (f"{C}/h3-globo-oscuridad.png", 0.5, "Sin hilos. | Sin trucos. | *Sin explicación.*", "Levitación magnética · 14 cm"),
    "S3-regalo-5cm": (f"{U}/u1-caja-lampara.png", 0.6, "El regalo de *5 cm* | que nadie olvida", "Saturno · Luna · Galaxia · Sistema solar"),
    "S4-cambia-la-luz": (f"{H}/c4-globo-final.png", 0.55, "Deja de comprar cojines. | *Cambia la luz.*", "4 luces · 1 cuarto nuevo"),
}


def fondo(ruta, ancho, alto, foco):
    im = Image.open(ruta).convert("RGB")
    r = max(ancho / im.width, alto / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    y = int((im.height - alto) * foco)
    im = im.crop(((im.width - ancho) // 2, y, (im.width - ancho) // 2 + ancho, y + alto))
    # oscurece arriba y abajo para que el texto destaque
    capa = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0)); d = ImageDraw.Draw(capa)
    for i in range(alto):
        a = max(0, 1 - i / (alto * 0.42)) * 150 + max(0, (i - alto * 0.72) / (alto * 0.28)) * 120
        d.line([(0, i), (ancho, i)], fill=(6, 6, 20, int(min(200, a))))
    out = ImageEnhance.Contrast(im).enhance(1.05).convert("RGBA"); out.alpha_composite(capa)
    return out


def boton(im, y):
    d = ImageDraw.Draw(im); f = tx.fuente(46, 850)
    texto = "Descúbrelo en orbiluz.com"; w = d.textlength(texto, font=f)
    d.rounded_rectangle(((im.width - w) / 2 - 40, y - 42, (im.width + w) / 2 + 40, y + 42), radius=42, fill=(255, 181, 71, 255))
    d.text((im.width / 2, y), texto, font=f, fill=(18, 18, 58, 255), anchor="mm")


def main():
    for nombre, (ruta, foco, gancho, nota) in IMAGENES.items():
        # en 9:16 la etiqueta va bajo el gancho y sin botón (Meta pone el suyo), para no tapar el producto
        for alto, suf, y_g, y_n, y_b in ((1350, "4x5", 330, 1060, 1210), (1920, "9x16", 470, 780, None)):
            im = fondo(ruta, tx.W, alto, foco)
            tx.gancho_viral(im, gancho, 99, 1.0, y_centro=y_g)
            tx.nota_viral(im, nota, 1.0, y=1180 if (alto == 1920 and nombre.startswith("S4")) else y_n)  # en S4 no tapar el reloj
            if y_b: boton(im, y_b)
            im.convert("RGB").save(f"{OUT}/{nombre}-{suf}.jpg", quality=92)
        print(nombre)


if __name__ == "__main__":
    main()
