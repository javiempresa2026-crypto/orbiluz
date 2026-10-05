"""Motor de montaje de los TikTok de Orbiluz.
Efectos de retención: gancho grande en el primer segundo, zoom de impacto y destello en cada corte,
barra de progreso, subtítulos palabra a palabra (sincronizados con Whisper), whoosh en los cortes
y logo pequeño. Todo en 1080x1920 a 30 fps."""
import os, subprocess, tempfile, json, wave, struct, math, random
import imageio_ffmpeg

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 30
FONTS = f"{ROOT}/marca/fuentes"
LOGO = f"{ROOT}/marca/logo/horizontal/orbiluz-horizontal-blanco-600.png"
AMBAR, NOCHE = "&H0047B5FF", "&H003A1212"  # colores ASS (BGR)


def run(cmd):
    subprocess.run(cmd, check=True)


def dur(path):
    out = subprocess.run([FF, "-i", path], capture_output=True, text=True).stderr
    h, m, s = out.split("Duration: ")[1].split(",")[0].split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


# ---------- segmentos ----------
def segmento(seg, out, tmp):
    """seg: dict(src, t0, t1 | dur, zoom='in'|'out'|None, velocidad, punch=True, flash=True, rev=False)"""
    src = seg["src"]; d = seg.get("dur"); es_img = src.lower().endswith((".jpg", ".png", ".jpeg"))
    if es_img and seg.get("ajustar"):  # producto entero sobre fondo difuminado de la misma foto
        from PIL import Image, ImageFilter, ImageEnhance
        im = Image.open(src).convert("RGB")
        fondo = im.resize((H, H)).crop(((H - W) // 2, 0, (H - W) // 2 + W, H)).filter(ImageFilter.GaussianBlur(40))
        fondo = ImageEnhance.Brightness(fondo).enhance(0.55)
        fg = im.resize((W, round(W * im.height / im.width)), Image.LANCZOS)
        fondo.paste(fg, (0, (H - fg.height) // 2)); src = f"{out}.jpg"; fondo.save(src, quality=95)
    base = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1"
    f = []
    if es_img:
        n = int(d * FPS)
        z = "1+0.10*on/{n}".format(n=n) if seg.get("zoom", "in") == "in" else "1.10-0.10*on/{n}".format(n=n)
        f.append(f"scale=-2:{int(H*1.25)},crop='min(iw,ih*9/16)':ih,zoompan=z='{z}':d={n}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}")
        ins = ["-i", src]
    else:
        t0, t1 = seg.get("t0", 0), seg.get("t1", 99)
        v = seg.get("velocidad", 1.0)
        ins = ["-ss", str(t0), "-to", str(t1), "-i", src]
        f.append(base)
        if seg.get("rev"): f.append("reverse")
        if v != 1.0: f.append(f"setpts={1/v}*PTS")
        f.append(f"fps={FPS}")
    if seg.get("punch", True):  # zoom de impacto: arranca al 112 % y vuelve al 100 % en 0,25 s
        f.append(f"scale={W*2}:{H*2},zoompan=z='if(lt(in_time,0.25),1.12-0.48*in_time,1)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}")
    if seg.get("flash", True):
        f.append("fade=t=in:st=0:d=0.12:color=white")
    if seg.get("filtro"): f.append(seg["filtro"])
    f.append("setsar=1,format=yuv420p")
    extra = ["-t", str(d)] if d else []
    run([FF, "-y", "-loglevel", "error", *ins, "-vf", ",".join(f), *extra, "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", out])
    return dur(out)


# ---------- sonido ----------
def _wav(path, samples, sr=48000):
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, s)) * 32000)) for s in samples))


def sfx(tmp):
    """Genera un whoosh (ruido filtrado que barre) y un pop suave. Sonidos sintetizados aquí, sin derechos."""
    sr = 48000; random.seed(7)
    n = int(0.35 * sr); y = 0; out = []
    for i in range(n):
        t = i / n; a = 0.15 + 0.85 * t  # el filtro se abre
        y = y + a * 0.35 * (random.uniform(-1, 1) - y)
        env = math.sin(math.pi * t) ** 1.5
        out.append(y * env * 0.9)
    _wav(f"{tmp}/whoosh.wav", out)
    n = int(0.12 * sr)
    _wav(f"{tmp}/pop.wav", [math.sin(2 * math.pi * (900 - 500 * i / n) * i / sr) * math.exp(-i / (0.025 * sr)) * 0.7 for i in range(n)])


# ---------- subtítulos ----------
def palabras_whisper(voz):
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(voz, language="es", beam_size=5, word_timestamps=True)
    return [(w.word.strip(), w.start, w.end) for s in segs for w in s.words if w.word.strip()]


def ass_tiempo(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def crear_ass(path, palabras, textos, total, desfase=0.0, correcciones=None):
    """palabras: [(palabra, ini, fin)] de la voz → subtítulos de 3 palabras con la actual en ámbar y efecto pop.
    textos: [(texto, ini, fin, estilo)] con estilo 'gancho' (grande arriba) o 'nota' (mediano)."""
    correcciones = correcciones or {}
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Unbounded,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,2,80,80,560,1
Style: Gancho,Unbounded,88,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,3,18,0,8,70,70,300,1
Style: Nota,DM Sans,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,8,80,80,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    pal = [(correcciones.get(p.lower().strip(".,¿?¡!"), p), a + desfase, b + desfase) for p, a, b in palabras]
    grupos, g = [], []
    for w in pal:
        g.append(w)
        if len(g) == 3 or w[0][-1:] in ".?!,": grupos.append(g); g = []
    if g: grupos.append(g)
    for gi, g in enumerate(grupos):
        fin_grupo = grupos[gi + 1][0][1] if gi + 1 < len(grupos) else g[-1][2] + 0.4
        for i, (p, a, b) in enumerate(g):
            fin = g[i + 1][1] if i + 1 < len(g) else fin_grupo
            partes = []
            for j, (q, _, _) in enumerate(g):
                q = q.upper()
                partes.append(f"{{\\c{AMBAR}\\fscx112\\fscy112\\t(0,90,\\fscx100\\fscy100)}}{q}{{\\c&H00FFFFFF\\fscx100\\fscy100}}" if j == i else q)
            ev.append(f"Dialogue: 1,{ass_tiempo(a)},{ass_tiempo(fin)},Sub,,0,0,0,,{' '.join(partes)}")
    for t, a, b, est in textos:
        estilo = "Gancho" if est == "gancho" else "Nota"
        anim = "{\\fad(80,120)\\fscx70\\fscy70\\t(0,160,\\fscx106\\fscy106)\\t(160,260,\\fscx100\\fscy100)}" if est == "gancho" else "{\\fad(120,120)}"
        ev.append(f"Dialogue: 2,{ass_tiempo(a)},{ass_tiempo(min(b, total))},{estilo},,0,0,0,,{anim}{t}")
    open(path, "w", encoding="utf-8").write(cab + "\n".join(ev) + "\n")


# ---------- montaje ----------
def montar(nombre, segmentos, salida_dir, voz=None, textos=(), whoosh=True, correcciones=None, desfase_voz=0.0, cierre=True):
    with tempfile.TemporaryDirectory() as tmp:
        partes, cortes, t = [], [], 0.0
        for i, s in enumerate(segmentos):
            p = f"{tmp}/s{i}.mp4"; d = segmento(s, p, tmp); partes.append(p); cortes.append(t); t += d
        total = t
        lst = f"{tmp}/l.txt"; open(lst, "w").write("".join(f"file '{p}'\n" for p in partes))
        base = f"{tmp}/base.mp4"
        run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])
        palabras = palabras_whisper(voz) if voz else []
        ass = f"{tmp}/s.ass"; crear_ass(ass, palabras, textos, total, desfase_voz, correcciones)
        sfx(tmp)
        # vídeo: logo + barra de progreso + subtítulos
        vf = (f"[0:v][1:v]overlay=(W-w)/2:150[v1];"
              f"[v1]drawbox=x=0:y=0:w='iw*t/{total:.3f}':h=12:color=0xFFB547@0.95:t=fill[v2];"
              f"[v2]ass={ass}:fontsdir={FONTS}[v]")
        ins = ["-i", base, "-loop", "1", "-framerate", str(FPS), "-t", f"{total:.3f}", "-i", f"{tmp}/logo.png"]
        from PIL import Image
        lg = Image.open(LOGO).convert("RGBA"); lg = lg.resize((200, round(200 * lg.height / lg.width)))
        a = lg.getchannel("A").point(lambda v: int(v * 0.75)); lg.putalpha(a); lg.save(f"{tmp}/logo.png")
        # audio: voz + whoosh en cada corte (menos el primero)
        a_ins, mezcla, k = [], [], 2
        if voz:
            a_ins += ["-i", voz]; mezcla.append(f"[{k}:a]adelay={int(desfase_voz*1000)}|{int(desfase_voz*1000)},volume=1.0[a{k}]"); k += 1
        if whoosh:
            for c in cortes[1:]:
                a_ins += ["-i", f"{tmp}/whoosh.wav"]; ms = int(max(0, c - 0.15) * 1000)
                mezcla.append(f"[{k}:a]adelay={ms}|{ms},volume={0.35 if voz else 0.6}[a{k}]"); k += 1
            a_ins += ["-i", f"{tmp}/pop.wav"]; mezcla.append(f"[{k}:a]adelay=150|150,volume=0.5[a{k}]"); k += 1
        filtros = [vf]
        mapa = ["-map", "[v]"]
        if mezcla:
            etiquetas = "".join(f"[a{i}]" for i in range(2, k))
            filtros += mezcla + [f"{etiquetas}amix=inputs={k-2}:normalize=0,apad,atrim=0:{total:.3f},aformat=sample_rates=48000:channel_layouts=stereo[a]"]
            mapa += ["-map", "[a]", "-c:a", "aac", "-b:a", "192k"]
        out = f"{salida_dir}/{nombre}.mp4"
        run([FF, "-y", "-loglevel", "error", *ins, *a_ins, "-filter_complex", ";".join(filtros), *mapa,
             "-t", f"{total:.3f}", "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out])
        print(f"{nombre}: {total:.1f} s")
        return out
