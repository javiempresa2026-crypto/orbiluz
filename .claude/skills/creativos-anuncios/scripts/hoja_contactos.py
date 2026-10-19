#!/usr/bin/env python3
"""Hoja de contactos de un vídeo (o de varias imágenes) para revisarlo antes de entregarlo.

Uso:
  python3 hoja_contactos.py video.mp4 [salida.jpg] [--fps 1.4] [--ancho 270]
  python3 hoja_contactos.py img1.jpg img2.jpg ... --salida hoja.jpg

Cada fotograma lleva su segundo en rojo. Usa el ffmpeg de imageio (en este entorno no hay ffmpeg en el PATH).
"""
import argparse, glob, os, subprocess, tempfile
from PIL import Image, ImageDraw
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()


def hoja(rutas, etiquetas, salida, ancho, cols=7):
    ims = [Image.open(r).convert("RGB") for r in rutas]
    ims = [im.resize((ancho, round(im.height * ancho / im.width))) for im in ims]
    h = max(im.height for im in ims)
    filas = (len(ims) + cols - 1) // cols
    o = Image.new("RGB", (cols * ancho, filas * h), "white")
    for i, (im, et) in enumerate(zip(ims, etiquetas)):
        ImageDraw.Draw(im).text((6, 6), et, fill="red")
        o.paste(im, ((i % cols) * ancho, (i // cols) * h))
    o.save(salida, quality=88)
    print(salida)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("entradas", nargs="+")
    a.add_argument("--salida")
    a.add_argument("--fps", type=float, default=1.4)
    a.add_argument("--ancho", type=int, default=270)
    o = a.parse_args()
    ent = o.entradas
    if len(ent) <= 2 and ent[0].lower().endswith((".mp4", ".mov")):
        salida = o.salida or (ent[1] if len(ent) == 2 else os.path.splitext(ent[0])[0] + "-hoja.jpg")
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([FF, "-loglevel", "error", "-y", "-i", ent[0], "-vf", f"fps={o.fps}", f"{tmp}/f_%03d.png"], check=True)
            fs = sorted(glob.glob(f"{tmp}/f_*.png"))
            hoja(fs, [f"{i / o.fps:.1f}s" for i in range(len(fs))], salida, o.ancho)
    else:
        hoja(ent, [os.path.basename(e) for e in ent], o.salida or "hoja.jpg", o.ancho)


if __name__ == "__main__":
    main()
