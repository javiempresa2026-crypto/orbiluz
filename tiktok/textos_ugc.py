"""Textos con aspecto nativo de TikTok / Reels (estilo «ugc»), dibujados con PIL como una capa transparente.
- Gancho: cajas blancas redondeadas por línea con letra negra, como el texto nativo de TikTok.
- Notas: caja amarilla con letra negra.
- Subtítulos: palabras blancas con borde negro; la palabra que suena va sobre un recuadro amarillo que «salta».
Fuente: TikTok Sans (OFL), en marca/fuentes/ugc.
Todo queda dentro de la zona segura: en 9:16 ni arriba (la interfaz tapa unos 270 px) ni abajo (unos 670 px),
y dentro del recorte 4:5 (y = 220 a 1570)."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
FUENTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "marca", "fuentes", "ugc", "TikTokSans[opsz,slnt,wdth,wght].ttf")
AMARILLO = (255, 225, 77, 255)
Y_GANCHO, Y_SUBS, ANCHO_MAX = 300, 1150, 900
_cache = {}


def fuente(tam, peso=800):
    k = (tam, peso)
    if k not in _cache:
        f = ImageFont.truetype(FUENTE, tam)
        valores = {"Optical size": 36, "Width": 100, "Weight": peso, "Slant": 0}
        f.set_variation_by_axes([valores.get(a["name"].decode() if isinstance(a["name"], bytes) else a["name"], a["default"])
                                 for a in f.get_variation_axes()])
        _cache[k] = f
    return _cache[k]


def _lineas(d, texto, f, ancho):
    lineas, actual = [], ""
    for p in texto.split():
        prueba = (actual + " " + p).strip()
        if d.textlength(prueba, font=f) <= ancho or not actual: actual = prueba
        else: lineas.append(actual); actual = p
    if actual: lineas.append(actual)
    return lineas


def caja_texto(im, texto, y, estilo):
    """Cajas por línea. estilo: 'gancho' (blanca, letra negra) o 'nota' (amarilla, letra negra)."""
    d = ImageDraw.Draw(im)
    f = fuente(66 if estilo == "gancho" else 52, 800)
    fondo = (255, 255, 255, 255) if estilo == "gancho" else AMARILLO
    px, py, alto = 26, 13, (86 if estilo == "gancho" else 68)
    for i, l in enumerate(_lineas(d, texto, f, ANCHO_MAX - 2 * px)):
        w = d.textlength(l, font=f); x0 = (W - w) / 2; yy = y + i * alto
        d.rounded_rectangle((x0 - px, yy - py, x0 + w + px, yy + alto - py), radius=18, fill=fondo)
        d.text((W / 2, yy + (alto - 2 * py) / 2), l, font=f, fill=(0, 0, 0, 255), anchor="mm")


def titulo_cine(im, texto, estilo):
    """Estilo «cine»: título grande en blanco, centrado, sin caja y con sombra suave (tipo tráiler).
    gancho: grande, en el centro de la zona segura. nota: más pequeño, en el tercio inferior seguro."""
    from PIL import ImageFilter
    f = fuente(96 if estilo == "gancho" else 52, 850 if estilo == "gancho" else 750)
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(capa)
    lineas = _lineas(d, texto, f, ANCHO_MAX)
    alto = 112 if estilo == "gancho" else 62
    # gancho en el tercio superior (por encima del producto); nota en el tercio inferior, ambos en zona segura
    y0 = (560 if estilo == "gancho" else 1170) - len(lineas) * alto / 2
    if estilo != "gancho":  # las notas llevan un fondo oscuro translúcido para leerse sobre zonas con luz
        for i, l in enumerate(lineas):
            w = d.textlength(l, font=f)
            d.rounded_rectangle(((W - w) / 2 - 26, y0 + i * alto - 12, (W + w) / 2 + 26, y0 + i * alto + alto - 4),
                                radius=22, fill=(8, 8, 26, 150))
    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sombra)
    for i, l in enumerate(lineas):
        ds.text((W / 2, y0 + i * alto), l, font=f, fill=(0, 0, 0, 200), anchor="ma")
    capa.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(14)))
    for i, l in enumerate(lineas):
        d.text((W / 2, y0 + i * alto), l, font=f, fill=(255, 246, 233, 255), anchor="ma")
    im.alpha_composite(capa)


def subtitulo(im, palabras, actual, escala):
    """palabras: lista de str del grupo. actual: índice de la que suena. escala: «salto» de la palabra actual."""
    d = ImageDraw.Draw(im)
    f = fuente(72, 850); esp = d.textlength(" ", font=f) + 26  # hueco para que el recuadro no toque la palabra de al lado
    anchos = [d.textlength(p, font=f) for p in palabras]
    # una o dos líneas
    filas, fila, ancho = [], [], 0
    for i, a in enumerate(anchos):
        if fila and ancho + esp + a > ANCHO_MAX: filas.append(fila); fila, ancho = [], 0
        ancho += (esp if fila else 0) + a; fila.append(i)
    filas.append(fila)
    for r, fila in enumerate(filas):
        total = sum(anchos[i] for i in fila) + esp * (len(fila) - 1)
        x = (W - total) / 2; y = Y_SUBS + r * 100
        for i in fila:
            cx, cy = x + anchos[i] / 2, y + 40
            if i == actual:
                fa = fuente(round(72 * escala), 850); wa = d.textlength(palabras[i], font=fa)
                d.rounded_rectangle((cx - wa / 2 - 16, cy - 46 * escala, cx + wa / 2 + 16, cy + 46 * escala), radius=16, fill=AMARILLO)
                d.text((cx, cy), palabras[i], font=fa, fill=(0, 0, 0, 255), anchor="mm")
            else:
                d.text((cx, cy), palabras[i], font=f, fill=(255, 255, 255, 255), anchor="mm",
                       stroke_width=7, stroke_fill=(0, 0, 0, 255))
            x += anchos[i] + esp


def grupos_de(palabras, correcciones, desfase):
    pal = [(correcciones.get(p.lower().strip(".,¿?¡!"), p), a + desfase, b + desfase) for p, a, b in palabras]
    grupos, g = [], []
    for w in pal:
        g.append(w)
        if len(g) == 3 or w[0][-1:] in ".?!,": grupos.append(g); g = []
    if g: grupos.append(g)
    out = []
    for gi, g in enumerate(grupos):
        fin = grupos[gi + 1][0][1] if gi + 1 < len(grupos) else g[-1][2] + 0.4
        out.append((g[0][1], fin, g))
    return out


def crear(salida, total, palabras, textos, correcciones=None, desfase=0.0, modo="ugc"):
    """Genera un .mov con transparencia (códec png) de `total` segundos con todos los textos."""
    correcciones = correcciones or {}
    grupos = grupos_de(palabras, correcciones, desfase)
    cortes = {0.0, total}
    for t, a, b, e in textos: cortes |= {a, min(b, total)}
    for a, b, g in grupos:
        cortes |= {a, min(b, total)}
        for _, ws, _ in g: cortes |= {ws, ws + 1 / FPS, ws + 2 / FPS}
    cortes = sorted(c for c in cortes if 0 <= c <= total)
    tmp = salida + ".d"; os.makedirs(tmp, exist_ok=True)
    estados, lista = {}, []
    for t0, t1 in zip(cortes, cortes[1:]):
        if t1 - t0 < 1e-4: continue
        t = (t0 + t1) / 2
        clave = []
        for txt, a, b, e in textos:
            if a <= t < b: clave.append((txt, e))
        sub = None
        for a, b, g in grupos:
            if a <= t < b:
                actual = max(i for i, w in enumerate(g) if w[1] <= t) if any(w[1] <= t for w in g) else 0
                dt = t - g[actual][1]
                escala = 1.22 if dt < 1 / FPS else (1.1 if dt < 2 / FPS else 1.0)
                sub = (tuple(w[0] for w in g), actual, escala)
        clave = (tuple(clave), sub)
        if clave not in estados:
            im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            for txt, e in clave[0]:
                if modo == "cine": titulo_cine(im, txt, "gancho" if e == "gancho" else "nota")
                else: caja_texto(im, txt, Y_GANCHO, "gancho" if e == "gancho" else "nota")
            if sub: subtitulo(im, list(sub[0]), sub[1], sub[2])
            ruta = f"{tmp}/e{len(estados)}.png"; im.save(ruta); estados[clave] = ruta
        lista.append((estados[clave], t1 - t0))
    with open(f"{tmp}/lista.txt", "w") as fh:
        for ruta, d in lista: fh.write(f"file '{ruta}'\nduration {d:.4f}\n")
        fh.write(f"file '{lista[-1][0]}'\n")
    import imageio_ffmpeg
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{tmp}/lista.txt",
                    "-vf", f"fps={FPS},format=rgba", "-t", f"{total:.3f}", "-c:v", "png", salida], check=True)
    return salida
