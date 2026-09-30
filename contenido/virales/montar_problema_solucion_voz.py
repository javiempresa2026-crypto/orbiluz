"""Vídeo viral problema → solución (Reels / Shorts / TikTok), ~18 s, sin voz ni precios.
1) Cuarto con luz de techo (el problema) · 2) se enciende la lámpara (la solución)
3) una mano la coge y la enciende · 4) cierre con la marca.
Versión con locución (voz Ainsley, Higgsfield seed_audio).
Uso: python3 contenido/virales/montar_problema_solucion_voz.py"""
import os, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
from montar_virales import ROOT, CLIPS, OUT, FF, W, H, texto_png, marca_png, FONT, LOGO

ESCENA = f"{ROOT}/anuncios/meta/escenas/escena-3.jpg"   # cuarto con luz de techo
SALIDA = f"{OUT}/v7-problema-luz-del-techo-voz.mp4"
VOZ = f"{CLIPS}/voz-v7-ainsley.wav"

# (texto, inicio, fin) sobre el vídeo final
TEXTOS = [  # subtítulos sincronizados con la locución
    ("¿Tu cuarto de noche parece la sala de espera del médico?", 0.0, 3.5),
    ("No es la decoración… es la luz del techo.", 3.7, 6.6),
    ("Apágala. Y enciende esto.", 6.7, 9.6),
    ("Un solo punto de luz cálida y tu cuarto cambia por completo", 9.7, 14.4),
]

def cierre_png(path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, H], fill=(18, 18, 58, 150))
    lg = Image.open(LOGO).convert("RGBA"); lg = lg.resize((560, round(560 * lg.height / lg.width)), Image.LANCZOS)
    im.alpha_composite(lg, ((W - lg.width) // 2, 820))
    f = ImageFont.truetype(FONT, 58)
    d.text((W / 2, 1010), "Decoración que se enciende", font=f, fill="#FFB547", anchor="ma")
    im.save(path)

def main():
    norm = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1,format=yuv420p"
    with tempfile.TemporaryDirectory() as tmp:
        marca = f"{tmp}/marca.png"; marca_png(marca)
        pngs = []
        for i, (t, a, b) in enumerate(TEXTOS):
            p = f"{tmp}/t{i}.png"; texto_png(t, p); pngs.append((p, a, b))
        cierre = f"{tmp}/cierre.png"; cierre_png(cierre)
        total = 18.0
        ins = ["-i", ESCENA,
               "-i", f"{CLIPS}/viral-lampara-se-enciende-9x16.mp4",
               "-i", f"{CLIPS}/viral-mano-coge-y-enciende-9x16.mp4",
               "-i", f"{CLIPS}/viral-mano-bola-9x16.mp4",
               "-loop", "1", "-framerate", "30", "-t", str(total), "-i", marca,
               "-loop", "1", "-framerate", "30", "-t", str(total), "-i", cierre]
        for p, _, _ in pngs: ins += ["-loop", "1", "-framerate", "30", "-t", str(total), "-i", p]
        ins += ["-i", VOZ]; ia = len(pngs) + 6
        ch = [
            # problema: foto con zoom lento y tono frío
            f"[0:v]scale=-2:2400,crop=1350:2400,zoompan=z='1+0.0009*on':d=195:s={W}x{H}:fps=30,eq=saturation=0.8,{norm}[s0]",
            f"[1:v]trim=0:5,setpts=PTS-STARTPTS,{norm}[s1]",
            f"[2:v]trim=0.8:4.3,setpts=PTS-STARTPTS,{norm}[s2]",
            f"[3:v]trim=0:3.5,setpts=PTS-STARTPTS,{norm}[s3]",
            "[s0][s1][s2][s3]concat=n=4:v=1[base]",
            "[base][4:v]overlay=0:0:enable='lt(t,14.5)'[b0]",
            "[5:v]format=rgba,fade=in:st=14.5:d=0.4:alpha=1[cz]",
            "[b0][cz]overlay=0:0:enable='gte(t,14.5)'[b1]",
        ]
        last = "b1"
        for i, (_, a, b) in enumerate(pngs):
            k = 6 + i
            ch.append(f"[{k}:v]format=rgba,fade=in:st={a}:d=0.2:alpha=1,fade=out:st={b-0.15}:d=0.15:alpha=1[t{i}]")
            ch.append(f"[{last}][t{i}]overlay=0:0:enable='between(t,{a},{b})'[o{i}]"); last = f"o{i}"
        subprocess.run([FF, "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(ch), "-map", f"[{last}]", "-map", f"{ia}:a", "-af", "apad,loudnorm=I=-14:TP=-1.5",
                        "-t", str(total), "-c:v", "libx264", "-preset", "slow", "-crf", "19", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", SALIDA], check=True)
    print(SALIDA)

if __name__ == "__main__":
    main()
