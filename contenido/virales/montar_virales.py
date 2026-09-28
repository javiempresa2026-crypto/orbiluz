"""Monta los vídeos virales verticales (TikTok / Reels) de Orbiluz.
Sin voz, sin precios y sin características: solo el producto, un texto nativo que crea la necesidad
y una marca de agua pequeña. La música se añade dentro de la app (sonidos en tendencia).
Uso: python3 contenido/virales/montar_virales.py"""
import os, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
CLIPS = f"{ROOT}/contenido/material"
OUT = f"{ROOT}/contenido/virales"
FONT = f"{ROOT}/marca/fuentes/DMSans-Bold.ttf"
LOGO = f"{ROOT}/marca/logo/horizontal/orbiluz-horizontal-blanco-600.png"
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1080, 1920

# Cada vídeo: clip base, cómo alargarlo y los textos (texto, inicio, fin) en segundos.
#   "pingpong": ida y vuelta, bucle perfecto con cámara estática
#   "hold": congela el último fotograma N segundos
#   "lento": velocidad reducida (factor sobre la duración)
VIDEOS = {
    "v1-pov-luz-del-techo": dict(clip="viral-lampara-se-enciende-9x16.mp4", modo=("hold", 3.5), textos=[
        ("POV: por fin quitaste la luz del techo", 0.0, 3.0),
        ("y tu cuarto cambió por completo", 3.0, 99)]),
    "v2-regalo-que-sorprende": dict(clip="viral-mano-bola-9x16.mp4", modo=("pingpong",), textos=[
        ("Cuando encuentras el regalo que de verdad sorprende", 0.0, 99)]),
    "v3-no-regalo-otra-taza": dict(clip="viral-regalo-lampara-9x16.mp4", modo=("pingpong",), textos=[
        ("Este año no regalo otra taza", 0.0, 3.2),
        ("regalo esto", 3.2, 99)]),
    "v4-nadie-sabe-como-funciona": dict(clip="viral-globo-despacho-9x16.mp4", modo=("lento", 1.7), textos=[
        ("Nadie en mi casa sabe cómo funciona esto", 0.0, 4.5),
        ("y nadie deja de mirarlo", 4.5, 99)]),
    # Reutilizan material ya generado (0 créditos)
    "v5-mi-cuarto-a-las-23": dict(clip="lampara-saturno-mesilla-9x16.mp4", modo=("pingpong",), textos=[
        ("Mi parte favorita del día: apagar la luz grande", 0.0, 99)]),
    "v6-lo-pongo-y-todos-preguntan": dict(clip="globo-flotando-escritorio-9x16.mp4", modo=("lento", 1.7), textos=[
        ("Lo puse en el escritorio y ahora todos preguntan", 0.0, 4.5),
        ("¿y esto cómo flota?", 4.5, 99)]),
}

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]

def texto_png(text, path):
    """Texto estilo TikTok: blanco con contorno negro, centrado en el tercio superior (fuera de la zona de la interfaz)."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    size = 70
    while True:
        f = ImageFont.truetype(FONT, size); lines = wrap(d, text, f, 900)
        if len(lines) <= 3 or size <= 50: break
        size -= 4
    lh = int(size * 1.22); y = 330
    for ln in lines:
        d.text((W / 2, y), ln, font=f, fill="#FFFFFF", anchor="ma", stroke_width=7, stroke_fill="#000000")
        y += lh
    im.save(path)

def marca_png(path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lg = Image.open(LOGO).convert("RGBA"); lg = lg.resize((210, round(210 * lg.height / lg.width)), Image.LANCZOS)
    a = lg.getchannel("A").point(lambda v: int(v * 0.7)); lg.putalpha(a)
    im.alpha_composite(lg, ((W - lg.width) // 2, 230)); im.save(path)

def duracion(path):
    out = subprocess.run([FF, "-i", path], capture_output=True, text=True).stderr
    h, m, s = out.split("Duration: ")[1].split(",")[0].split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)

def montar(nombre, cfg, tmp):
    src = f"{CLIPS}/{cfg['clip']}"; d = duracion(src); modo = cfg["modo"]
    base = f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1"
    if modo[0] == "pingpong":
        vf = f"{base},split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1[v0]"; total = d * 2
    elif modo[0] == "hold":
        vf = f"{base},tpad=stop_mode=clone:stop_duration={modo[1]}[v0]"; total = d + modo[1]
    else:
        vf = f"[0:v]setpts={modo[1]}*PTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1[v0]"; total = d * modo[1]
    ins, chain, last = ["-i", src], [vf], "v0"
    marca = f"{tmp}/marca.png"; marca_png(marca)
    ins += ["-loop", "1", "-framerate", "30", "-t", f"{total:.2f}", "-i", marca]
    chain.append(f"[{last}][1:v]overlay=0:0[m]"); last = "m"
    for i, (txt, t0, t1) in enumerate(cfg["textos"]):
        p = f"{tmp}/{nombre}-{i}.png"; texto_png(txt, p); k = i + 2; t1 = min(t1, total)
        ins += ["-loop", "1", "-framerate", "30", "-t", f"{total:.2f}", "-i", p]
        chain.append(f"[{k}:v]format=rgba,fade=in:st={t0}:d=0.2:alpha=1,fade=out:st={max(t1 - 0.15, t0)}:d=0.15:alpha=1[t{i}]")
        chain.append(f"[{last}][t{i}]overlay=0:0:enable='between(t,{t0},{t1})'[o{i}]"); last = f"o{i}"
    out = f"{OUT}/{nombre}.mp4"
    subprocess.run([FF, "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(chain), "-map", f"[{last}]",
                    "-t", f"{total:.2f}", "-c:v", "libx264", "-preset", "slow", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-movflags", "+faststart", "-an", out], check=True)
    print(f"{nombre}: {total:.1f} s")

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        for n, c in VIDEOS.items():
            if os.path.exists(f"{CLIPS}/{c['clip']}"): montar(n, c, tmp)
            else: print(f"{n}: falta el clip {c['clip']}")
