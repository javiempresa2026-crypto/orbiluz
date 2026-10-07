"""Motor de montaje de los TikTok de Orbiluz.
Efectos de retención: gancho grande en el primer segundo, transiciones distintas en cada vídeo,
movimientos de cámara variados, música propia con el ritmo entrando al aparecer el producto,
cortes al compás, barra de progreso, subtítulos palabra a palabra (sincronizados con Whisper)
y logo pequeño. Todo en 1080x1920 a 30 fps."""
import os, sys, subprocess, tempfile, json, wave, struct, math, random
import imageio_ffmpeg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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


# ---------- transiciones ----------
# nombre: (transición de ffmpeg xfade, duración, sonido)
TRANSICIONES = {
    "corte":      ("fade", 0.034, "golpe"),       # corte seco con zoom de impacto en el plano que entra
    "flash":      ("fadewhite", 0.3, None),       # destello (solo para el momento del drop)
    "deslizar":   ("slideleft", 0.28, "whoosh"),
    "subir":      ("slideup", 0.28, "whoosh"),
    "barrido":    ("smoothleft", 0.4, "whoosh"),
    "barrido-v":  ("smoothup", 0.4, "whoosh"),
    "zoom":       ("zoomin", 0.35, "whoosh"),
    "desenfoque": ("hblur", 0.35, None),
    "fundido":    ("dissolve", 0.5, None),
    "negro":      ("fadeblack", 0.45, None),
    "circulo":    ("circleopen", 0.45, None),
    "radial":     ("radial", 0.45, None),
    "pixel":      ("pixelize", 0.35, None),
    "cortina":    ("vertopen", 0.4, None),
    "aplastar":   ("squeezeh", 0.3, "whoosh"),
}
MOVIMIENTOS = ["in", "der", "out", "izq", "sube"]


# ---------- segmentos ----------
def duracion_natural(seg):
    if seg.get("dur"): return seg["dur"]
    t1 = min(seg.get("t1", 99), dur(seg["src"]))
    return (t1 - seg.get("t0", 0)) / seg.get("velocidad", 1.0)


def segmento(seg, out, d, cola=0.0, punch=False, mov="in"):
    """Renderiza un plano de d segundos + «cola» (lo que se solapa con la transición siguiente).
    seg: dict(src, t0, t1 | dur, zoom/mov, velocidad, rev, ajustar, filtro)"""
    src = seg["src"]; es_img = src.lower().endswith((".jpg", ".png", ".jpeg"))
    largo = d + cola
    if es_img and seg.get("ajustar"):  # producto entero sobre fondo difuminado de la misma foto
        from PIL import Image, ImageFilter, ImageEnhance
        im = Image.open(src).convert("RGB")
        fondo = im.resize((H, H)).crop(((H - W) // 2, 0, (H - W) // 2 + W, H)).filter(ImageFilter.GaussianBlur(40))
        fondo = ImageEnhance.Brightness(fondo).enhance(0.55)
        fg = im.resize((W, round(W * im.height / im.width)), Image.LANCZOS)
        fondo.paste(fg, (0, (H - fg.height) // 2)); src = f"{out}.jpg"; fondo.save(src, quality=95)
    f = []
    if es_img:
        n = int(round(largo * FPS)); m = seg.get("mov") or {"in": "in", "out": "out"}.get(seg.get("zoom"), mov)
        cx, cy = "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
        z, x, y = {
            "in":   (f"1+0.10*on/{n}", cx, cy),
            "out":  (f"1.10-0.10*on/{n}", cx, cy),
            "der":  ("1.12", f"(iw-iw/zoom)*on/{n}", cy),
            "izq":  ("1.12", f"(iw-iw/zoom)*(1-on/{n})", cy),
            "sube": ("1.12", cx, f"(ih-ih/zoom)*(1-on/{n})"),
        }[m]
        f.append(f"scale=-2:{int(H*1.25)},crop='min(iw,ih*9/16)':ih,zoompan=z='{z}':d={n}:x='{x}':y='{y}':s={W}x{H}:fps={FPS}")
        ins = ["-i", src]
    else:
        t0, v = seg.get("t0", 0), seg.get("velocidad", 1.0)
        ins = ["-ss", str(t0), "-i", src]
        f.append(f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1")
        if seg.get("rev"): f.append("reverse")
        if v != 1.0: f.append(f"setpts={1/v}*PTS")
        f.append(f"fps={FPS},tpad=stop_mode=clone:stop_duration=3")
    if punch:  # zoom de impacto: arranca al 112 % y vuelve al 100 % en 0,25 s
        f.append(f"scale={W*2}:{H*2},zoompan=z='if(lt(in_time,0.25),1.12-0.48*in_time,1)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}")
    if seg.get("filtro"): f.append(seg["filtro"])
    f.append("setsar=1,format=yuv420p")
    run([FF, "-y", "-loglevel", "error", *ins, "-vf", ",".join(f), "-t", f"{largo:.3f}", "-an",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", out])


# ---------- sonido ----------
def _wav(path, samples, sr=48000):
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, s)) * 32000)) for s in samples))


def sfx(tmp):
    """Whoosh suave (ruido filtrado que barre) y golpe grave corto. Sintetizados aquí, sin derechos."""
    sr = 48000; random.seed(7)
    n = int(0.4 * sr); y = 0; out = []
    for i in range(n):
        t = i / n; a = 0.04 + 0.25 * math.sin(math.pi * t)  # filtro más cerrado: suena a aire, no a ruido
        y = y + a * (random.uniform(-1, 1) - y)
        out.append(y * math.sin(math.pi * t) ** 2 * 0.8)
    _wav(f"{tmp}/whoosh.wav", out)
    n = int(0.18 * sr)
    _wav(f"{tmp}/golpe.wav", [math.sin(2 * math.pi * (55 + 70 * math.exp(-i / (0.01 * sr))) * i / sr) * math.exp(-i / (0.04 * sr)) for i in range(n)])


# ---------- subtítulos ----------
def palabras_whisper(voz):
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(voz, language="es", beam_size=5, word_timestamps=True)
    return [(w.word.strip(), w.start, w.end) for s in segs for w in s.words if w.word.strip()]


def ass_tiempo(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def crear_ass(path, palabras, textos, total, desfase=0.0, correcciones=None, estilo="marca"):
    """palabras: [(palabra, ini, fin)] de la voz → subtítulos de 3 palabras con la actual en ámbar y efecto pop.
    textos: [(texto, ini, fin, estilo)] con estilo 'gancho' (grande arriba) o 'nota' (mediano)."""
    correcciones = correcciones or {}
    ig = estilo == "ig"
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
{ESTILOS_ASS[estilo]}

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
                if ig:  # estilo Instagram: frase normal, sin resaltar palabra
                    partes.append(q); continue
                q = q.upper()
                partes.append(f"{{\\c{AMBAR}\\fscx112\\fscy112\\t(0,90,\\fscx100\\fscy100)}}{q}{{\\c&H00FFFFFF\\fscx100\\fscy100}}" if j == i else q)
            ev.append(f"Dialogue: 1,{ass_tiempo(a)},{ass_tiempo(fin)},Sub,,0,0,0,,{' '.join(partes)}")
    for t, a, b, est in textos:
        estilo = "Gancho" if est == "gancho" else "Nota"
        anim = "{\\fad(80,120)\\fscx70\\fscy70\\t(0,160,\\fscx106\\fscy106)\\t(160,260,\\fscx100\\fscy100)}" if est == "gancho" else "{\\fad(120,120)}"
        ev.append(f"Dialogue: 2,{ass_tiempo(a)},{ass_tiempo(min(b, total))},{estilo},,0,0,0,,{anim}{t}")
    open(path, "w", encoding="utf-8").write(cab + "\n".join(ev) + "\n")


# Estilos de texto: «marca» (Unbounded con la palabra en ámbar) o «ig» (caja blanca y letra negra, como los textos nativos de Instagram)
ESTILOS_ASS = {
    "marca": """Style: Sub,Unbounded,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,2,80,80,560,1
Style: Gancho,Unbounded,88,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,3,18,0,8,70,70,300,1
Style: Nota,DM Sans,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,8,80,80,330,1""",
    "ig": """Style: Sub,DM Sans,66,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,16,0,2,110,110,560,1
Style: Gancho,DM Sans,74,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,20,0,8,90,90,300,1
Style: Nota,DM Sans,60,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,14,0,8,100,100,330,1""",
}


def tarjeta_final(path, frase="Decoración que se enciende", web="orbiluz.com", fondo=None):
    """Cierre de anuncio: logo, frase y la web sobre la última escena difuminada y oscurecida."""
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
    if fondo:
        im = Image.open(fondo).convert("RGB")
        r = max(W / im.width, H / im.height); im = im.resize((round(im.width * r), round(im.height * r)))
        im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
        im = ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(28))).enhance(0.35)
    else:
        im = Image.new("RGB", (W, H), (18, 18, 58))
    lg = Image.open(LOGO).convert("RGBA"); lg = lg.resize((640, round(640 * lg.height / lg.width)), Image.LANCZOS)
    im.paste(lg, ((W - lg.width) // 2, 760), lg)
    d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype(f"{FONTS}/DMSans-Bold.ttf", 60); f2 = ImageFont.truetype(f"{FONTS}/Unbounded-Bold.ttf", 54)
    d.text((W / 2, 760 + lg.height + 60), frase, font=f1, fill="#FFF6E9", anchor="ma")
    w = d.textlength(web, font=f2) + 110; y = 760 + lg.height + 190
    d.rounded_rectangle(((W - w) / 2, y, (W + w) / 2, y + 112), radius=56, fill="#FFB547")
    d.text((W / 2, y + 56), web, font=f2, fill="#12123A", anchor="mm")
    im.save(path, quality=95)
    return path


def a_4x5(entrada, salida, y=220):
    """Versión 4:5 (1080x1350) para el feed, recortando la vertical."""
    run([FF, "-y", "-loglevel", "error", "-i", entrada, "-vf", f"crop={W}:1350:0:{y}", "-c:v", "libx264", "-preset", "slow",
         "-crf", "20", "-c:a", "copy", "-movflags", "+faststart", salida])
    return salida


# ---------- montaje ----------
def al_compas(dur_planos, tempo, drop_idx=1):
    """Ajusta los cortes al medio tiempo más cercano de la música, contando desde el corte del drop."""
    cortes = [sum(dur_planos[:i]) for i in range(len(dur_planos) + 1)]
    base = cortes[drop_idx]; paso = 60 / tempo / 2
    nuevos = [c if i <= drop_idx else base + max(1, round((c - base) / paso)) * paso for i, c in enumerate(cortes)]
    for i in range(drop_idx + 1, len(nuevos)):  # nunca dos cortes en el mismo tiempo
        nuevos[i] = max(nuevos[i], nuevos[i - 1] + paso)
    return [b - a for a, b in zip(nuevos, nuevos[1:])], cortes, nuevos


def montar(nombre, segmentos, salida_dir, voz=None, textos=(), correcciones=None, desfase_voz=0.0,
           transiciones=("corte",), musica="lofi", drop=None, tempo=None, compas=None, vol_musica=None, silencio=None,
           estilo_texto="marca", logo=True, barra=True, formato_4x5=False, real=False):
    """transiciones: lista que se repite entre plano y plano (ver TRANSICIONES).
    musica: estilo de musica.py o None. drop: segundo en que entra el ritmo (por defecto, el primer corte).
    compas: True para que los cortes caigan al ritmo (por defecto en los vídeos sin voz).
    silencio: (inicio, fin) en que la música se corta en seco, para un momento dramático.
    estilo_texto: «marca», «ig» o «ugc» (textos nativos de TikTok dibujados con textos_ugc.py).
    real: grano de cámara de móvil y un ligero movimiento de cámara en mano."""
    import numpy as np, musica as mus
    tempo = tempo or (mus.bpm(musica) if musica else 120)
    compas = (voz is None and musica is not None) if compas is None else compas
    with tempfile.TemporaryDirectory() as tmp:
        ds = [duracion_natural(s) for s in segmentos]
        if compas:
            ds, viejos, nuevos = al_compas(ds, tempo)
            textos = [(t, float(np.interp(a, viejos, nuevos)), float(np.interp(b, viejos, nuevos)), e) for t, a, b, e in textos]
        cortes = [sum(ds[:i]) for i in range(len(ds))]; total = sum(ds)
        drop = cortes[1] if drop is None and len(cortes) > 1 else (drop or 0)
        tipos = [transiciones[i % len(transiciones)] for i in range(len(ds) - 1)]
        partes = []
        for i, s in enumerate(segmentos):
            p = f"{tmp}/s{i}.mp4"; cola = TRANSICIONES[tipos[i]][1] if i < len(tipos) else 0
            segmento(s, p, ds[i], cola, punch=(i > 0 and tipos[i - 1] == "corte"), mov=MOVIMIENTOS[i % len(MOVIMIENTOS)])
            partes.append(p)
        palabras = palabras_whisper(voz) if voz else []
        ass = f"{tmp}/s.ass"
        if estilo_texto != "ugc": crear_ass(ass, palabras, textos, total, desfase_voz, correcciones, estilo_texto)
        sfx(tmp)
        from PIL import Image
        lg = Image.open(LOGO).convert("RGBA"); lg = lg.resize((200, round(200 * lg.height / lg.width)))
        lg.putalpha(lg.getchannel("A").point(lambda v: int(v * 0.75))); lg.save(f"{tmp}/logo.png")
        ins = []
        for p in partes: ins += ["-i", p]
        n = len(partes)
        ins += ["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.3f}", "-i", f"{tmp}/logo.png"]
        ugc = estilo_texto == "ugc"
        if ugc:
            import textos_ugc
            ins += ["-i", textos_ugc.crear(f"{tmp}/textos.mov", total, palabras, textos, correcciones, desfase_voz)]
        # vídeo: cadena de transiciones + logo + barra de progreso + subtítulos
        fc, ult = [], "0:v"
        for i, tp in enumerate(tipos):
            efecto, td, _ = TRANSICIONES[tp]
            fc.append(f"[{ult}][{i+1}:v]xfade=transition={efecto}:duration={td}:offset={cortes[i+1]:.3f}[x{i+1}]"); ult = f"x{i+1}"
        fc.append(f"[{ult}][{n}:v]overlay=(W-w)/2:150[v1]" if logo else f"[{ult}]null[v1]")
        fc.append(f"[v1]drawbox=x=0:y=0:w='iw*t/{total:.3f}':h=12:color=0xFFB547@0.95:t=fill[v2]" if barra else "[v1]null[v2]")
        if real:  # cámara en mano (desplazamiento suave de pocos píxeles) y grano de móvil
            fc.append("[v2]scale=1112:1978,crop=1080:1920:x='16+8*sin(t*1.9)+4*sin(t*4.3)':y='29+10*sin(t*1.4)+5*sin(t*3.7)',"
                      "noise=alls=7:allf=t+u,eq=contrast=1.03:saturation=0.96[v3]")
        else:
            fc.append("[v2]null[v3]")
        fc.append(f"[v3][{n+1}:v]overlay=0:0:format=auto,format=yuv420p[v]" if ugc else f"[v3]ass={ass}:fontsdir={FONTS}[v]")
        # audio: voz + música (que baja sola cuando habla la voz) + efectos suaves
        k = n + (2 if ugc else 1); mezcla = []
        if musica:
            mw = f"{tmp}/musica.wav"; mus.crear(musica, total + 0.5, drop, mw, tempo=tempo)
            ins += ["-i", mw]; vm = vol_musica or (0.30 if voz else 0.85)
            corte = f",volume='if(between(t,{silencio[0]},{silencio[1]}),0.03,1)':eval=frame" if silencio else ""
            fc.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={vm}{corte}[mus]"); k += 1
        if voz:
            ins += ["-i", voz]; ms = int(desfase_voz * 1000)
            fc.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms},asplit=2[voz][vsc]"); k += 1
            mezcla.append("[voz]")
            if musica:
                fc.append("[mus][vsc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[mus2]"); mezcla.append("[mus2]")
            else:
                fc.append("[vsc]anullsink")
        elif musica:
            mezcla.append("[mus]")
        vol_sfx = {"whoosh": 0.10 if voz else 0.16, "golpe": 0.22 if voz else 0.3}
        for i, tp in enumerate(tipos):
            sonido = TRANSICIONES[tp][2]
            if not sonido: continue
            ins += ["-i", f"{tmp}/{sonido}.wav"]; ms = int(max(0, cortes[i + 1] - (0.2 if sonido == "whoosh" else 0)) * 1000)
            fc.append(f"[{k}:a]aresample=48000,adelay={ms}|{ms},volume={vol_sfx[sonido]}[e{k}]"); mezcla.append(f"[e{k}]"); k += 1
        mapa = ["-map", "[v]"]
        if mezcla:
            fc.append(f"{''.join(mezcla)}amix=inputs={len(mezcla)}:normalize=0,apad,atrim=0:{total:.3f},"
                      f"alimiter=limit=0.9,aformat=sample_rates=48000:channel_layouts=stereo[a]")
            mapa += ["-map", "[a]", "-c:a", "aac", "-b:a", "192k"]
        out = f"{salida_dir}/{nombre}.mp4"
        run([FF, "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fc), *mapa,
             "-t", f"{total:.3f}", "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out])
        if formato_4x5: a_4x5(out, f"{salida_dir}/{nombre}-4x5.mp4")
        print(f"{nombre}: {total:.1f} s · {musica or 'sin música'} · {', '.join(dict.fromkeys(tipos))}")
        return out
