"""Textos con aspecto nativo de TikTok / Reels, dibujados con PIL como una capa transparente.
Modos: «ugc» (cajas nativas), «cine» (títulos de tráiler) y «viral» (tipografía cinética: el gancho aparece palabra a palabra,
en mayúsculas, con borde grueso y la palabra clave *entre asteriscos* sobre un recuadro amarillo inclinado).
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


# ---------- estilo «viral»: tipografía cinética ----------
NEGRO = (0, 0, 0, 255)
ENTRE_PALABRAS = 0.13  # segundos entre una palabra y la siguiente al aparecer el gancho


def _palabras_marcadas(texto):
    """'Sin hilos. *Sin explicación.*' -> [('SIN', False), ('HILOS.', False), ('SIN', True), ('EXPLICACIÓN.', True)]"""
    out, marcada = [], False
    for p in texto.split():
        if p == "|": out.append(("|", False)); continue  # salto de línea manual
        empieza, termina = p.startswith("*"), p.endswith("*")
        if empieza: marcada = True
        out.append((p.strip("*").upper(), marcada))
        if termina: marcada = False
    return out


def _escala_pop(dt):
    return 1.25 if dt < 1 / FPS else (1.1 if dt < 2 / FPS else (1.03 if dt < 3 / FPS else 1.0))


def _palabra(im, texto, cx, cy, tam, marcada, escala=1.0, giro=-3):
    """Dibuja una palabra centrada en (cx, cy): blanca con borde negro grueso, o sobre recuadro amarillo inclinado."""
    from PIL import ImageFilter
    f = fuente(round(tam * escala), 900)
    d = ImageDraw.Draw(im)
    w = d.textlength(texto, font=f)
    if marcada:
        pad, alto = 22 * escala, tam * escala * 1.18
        ficha = Image.new("RGBA", (int(w + 2 * pad + 8), int(alto + 8)), (0, 0, 0, 0))
        df = ImageDraw.Draw(ficha)
        df.rounded_rectangle((4, 4, ficha.width - 4, ficha.height - 4), radius=int(16 * escala), fill=AMARILLO)
        df.text((ficha.width / 2, ficha.height / 2), texto, font=f, fill=NEGRO, anchor="mm")
        ficha = ficha.rotate(giro, resample=Image.BICUBIC, expand=True)
        im.alpha_composite(ficha, (int(cx - ficha.width / 2), int(cy - ficha.height / 2)))
    else:
        sombra = Image.new("RGBA", (int(w + 120), int(tam * escala * 1.6)), (0, 0, 0, 0))
        ImageDraw.Draw(sombra).text((sombra.width / 2, sombra.height / 2 + 8), texto, font=f, fill=(0, 0, 0, 170), anchor="mm",
                                    stroke_width=12, stroke_fill=(0, 0, 0, 170))
        sombra = sombra.filter(ImageFilter.GaussianBlur(10))
        im.alpha_composite(sombra, (int(cx - sombra.width / 2), int(cy - sombra.height / 2)))
        d.text((cx, cy), texto, font=f, fill=(255, 255, 255, 255), anchor="mm", stroke_width=max(6, round(11 * escala)),
               stroke_fill=NEGRO)


def gancho_viral(im, texto, visibles, escala_ultima, y_centro=560):
    """Gancho en mayúsculas que aparece palabra a palabra. Se maqueta con todas las palabras para que no salten al aparecer."""
    d = ImageDraw.Draw(im)
    pals = _palabras_marcadas(texto)
    saltos = {i for i, (p, _) in enumerate(pals) if p == "|"}
    # relleno del recuadro repartido entre las palabras de cada tramo resaltado (no 44 px por palabra)
    extra, k = [0.0] * len(pals), 0
    while k < len(pals):
        if pals[k][1] and k not in saltos:
            j = k
            while j + 1 < len(pals) and pals[j + 1][1] and j + 1 not in saltos: j += 1
            for q in range(k, j + 1): extra[q] = 56 / (j - k + 1)
            k = j + 1
        else: k += 1
    tam = 120
    while True:
        f = fuente(tam, 900); esp = d.textlength(" ", font=f) + 10
        anchos = [0 if p == "|" else d.textlength(p, font=f) + extra[i] for i, (p, m) in enumerate(pals)]
        # cada línea forzada con «|» tiene que caber entera
        lineas, acc = [], 0
        for i, a in enumerate(anchos):
            if i in saltos: lineas.append(acc); acc = 0
            else: acc += (esp if acc else 0) + a
        lineas.append(acc)
        # ancho real de cada tramo resaltado (palabras seguidas en un mismo recuadro, con relleno y borde)
        tramos, acc_t = [], 0
        for (p_, m), a_ in zip(pals, anchos):
            if m and p_ != "|": acc_t += (esp if acc_t else 0) + a_
            else:
                if acc_t: tramos.append(acc_t + 2 * 24 + 40)
                acc_t = 0
        if acc_t: tramos.append(acc_t + 2 * 24 + 40)
        cabe = (max(lineas) <= 960 if saltos else max(anchos) <= 960) and all(t_ <= 1000 for t_ in tramos)
        if cabe or tam <= 60: break
        tam -= 4
    filas, fila, ancho = [], [], 0
    for i, a in enumerate(anchos):
        if i in saltos: filas.append(fila); fila, ancho = [], 0; continue
        if fila and not saltos and ancho + esp + a > 960: filas.append(fila); fila, ancho = [], 0
        ancho += (esp if fila else 0) + a; fila.append(i)
    filas.append(fila)
    filas = [f_ for f_ in filas if f_]
    alto = tam * 1.3
    y0 = y_centro - (len(filas) - 1) * alto / 2
    orden = {i: k for k, i in enumerate(j for j in range(len(pals)) if j not in saltos)}  # posición de cada palabra real
    for r, fila in enumerate(filas):
        total = sum(anchos[i] for i in fila) + esp * (len(fila) - 1)
        x = (W - total) / 2; cy = y0 + r * alto
        centros = {}
        for i in fila: centros[i] = x + anchos[i] / 2; x += anchos[i] + esp
        # tramos: palabras seguidas resaltadas van juntas en un solo recuadro
        tramos, k = [], 0
        while k < len(fila):
            i = fila[k]
            if pals[i][1]:
                tramo = [i]
                while k + 1 < len(fila) and pals[fila[k + 1]][1]: k += 1; tramo.append(fila[k])
                tramos.append(tramo)
            else:
                tramos.append([i])
            k += 1
        for tramo in tramos:
            vis = [i for i in tramo if orden[i] < visibles]
            if not vis: continue
            nueva = orden[vis[-1]] == visibles - 1
            esc = escala_ultima if nueva else 1.0
            if pals[tramo[0]][1]:
                centro_tramo = ((centros[tramo[0]] - anchos[tramo[0]] / 2) + (centros[tramo[-1]] + anchos[tramo[-1]] / 2)) / 2
                _tramo_resaltado(im, [(pals[i][0], centros[i]) for i in vis], cy, tam, esc, centro=centro_tramo)
            else:
                _palabra(im, pals[tramo[0]][0], centros[tramo[0]], cy, tam, False, esc)


def _tramo_resaltado(im, palabras, cy, tam, escala, centro=None):
    """Una o varias palabras sobre un único recuadro amarillo con borde negro, inclinado y con «golpe» al aparecer.
    palabras: [(texto, centro_x)]; se recolocan con espaciado normal alrededor del centro del tramo."""
    f = fuente(round(tam * escala), 900)
    d0 = ImageDraw.Draw(im)
    anchos = [d0.textlength(t, font=f) for t, _ in palabras]
    esp = d0.textlength(" ", font=f) + 6
    total = sum(anchos) + esp * (len(palabras) - 1)
    pad = 24 * escala
    a = total + 2 * pad; h = tam * 1.2 * escala
    ficha = Image.new("RGBA", (int(a + 16), int(h + 16)), (0, 0, 0, 0)); df = ImageDraw.Draw(ficha)
    df.rounded_rectangle((8, 8, ficha.width - 8, ficha.height - 8), radius=int(18 * escala), fill=AMARILLO,
                         outline=NEGRO, width=max(4, round(6 * escala)))
    x = 8 + pad
    for (texto, _), w in zip(palabras, anchos):
        df.text((x + w / 2, ficha.height / 2), texto, font=f, fill=NEGRO, anchor="mm"); x += w + esp
    if centro is None: centro = sum(c for _, c in palabras) / len(palabras)
    ficha = ficha.rotate(-3, resample=Image.BICUBIC, expand=True)
    im.alpha_composite(ficha, (int(centro - ficha.width / 2), int(cy - ficha.height / 2)))


def nota_viral(im, texto, escala, y=1190):
    """Etiqueta amarilla en mayúsculas, ligeramente inclinada, que entra con un golpe."""
    d = ImageDraw.Draw(im)
    tam = 66
    while d.textlength(texto.upper(), font=fuente(tam, 900)) > 880 and tam > 34: tam -= 2
    _tramo_resaltado(im, [(texto.upper(), W / 2)], y, tam, escala)


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
    for t, a, b, e in textos:
        cortes |= {a, min(b, total)}
        if modo == "viral":  # momentos en que aparece cada palabra y los 3 fotogramas del «golpe»
            n = len([w for w in t.split() if w != "|"]) if e == "gancho" else 1
            for i in range(n):
                ta = a + i * ENTRE_PALABRAS
                cortes |= {ta, ta + 1 / FPS, ta + 2 / FPS, ta + 3 / FPS}
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
            if a <= t < b:
                if modo == "viral":
                    n = len([w for w in txt.split() if w != "|"]) if e == "gancho" else 1
                    visibles = min(n, int((t - a) / ENTRE_PALABRAS) + 1)
                    clave.append((txt, e, visibles, _escala_pop(t - a - (visibles - 1) * ENTRE_PALABRAS)))
                else:
                    clave.append((txt, e))
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
            for txt, e, *anim in clave[0]:
                if modo == "viral":
                    if e == "gancho": gancho_viral(im, txt, anim[0], anim[1])
                    else: nota_viral(im, txt, anim[1])
                elif modo == "cine": titulo_cine(im, txt, "gancho" if e == "gancho" else "nota")
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
