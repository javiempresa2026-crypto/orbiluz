"""Música original para los TikTok de Orbiluz, sintetizada aquí (sin derechos de terceros).
Cada estilo tiene intro suave, subida («riser») y entrada del ritmo («drop») en el segundo que se elija,
para que el cambio de la música caiga justo cuando aparece el producto.
Estilos: lofi (tranquilo), house (alegre), trap (808 y hi-hats rápidos), sueño (ambiental, sin batería).
Uso: musica.crear("lofi", duracion=15, drop=2.4, salida="m.wav")"""
import math, wave
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve

SR = 44100
rng = np.random.default_rng(11)

# notas MIDI → Hz
def hz(n): return 440.0 * 2 ** ((n - 69) / 12)

ESTILOS = {
    #        bpm  acordes (MIDI)                                                       bajo (raíces)
    "lofi":  (82,  [[57, 60, 64, 67], [53, 57, 60, 64], [48, 52, 55, 59], [55, 59, 62, 64]], [45, 41, 36, 43]),
    "house": (122, [[57, 60, 64, 69], [53, 57, 60, 65], [48, 55, 60, 64], [55, 59, 62, 67]], [45, 41, 48, 43]),
    "trap":  (140, [[56, 59, 63, 66], [52, 56, 59, 63], [49, 53, 56, 61], [51, 55, 58, 63]], [44, 40, 37, 39]),
    "sueño": (70,  [[52, 59, 64, 66], [48, 55, 60, 64], [55, 62, 67, 69], [50, 57, 62, 66]], [40, 36, 43, 38]),
}


def bpm(estilo): return ESTILOS[estilo][0]


# ---------- instrumentos ----------
def env(n, a=0.005, d=0.1, s=0.6, r=0.2, largo=None):
    largo = largo or n / SR
    t = np.arange(n) / SR
    e = np.where(t < a, t / a, np.where(t < a + d, 1 - (1 - s) * (t - a) / d, s))
    e = e * np.clip(1 - (t - largo) / r, 0, 1) if r else e
    return e


def lp(x, f, orden=2):
    return sosfilt(butter(orden, min(f, SR / 2 - 100) / (SR / 2), "low", output="sos"), x)


def hp(x, f, orden=2):
    return sosfilt(butter(orden, f / (SR / 2), "high", output="sos"), x)


def kick(dur=0.45, f0=150, f1=45, golpe=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 28)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7)
    clic = rng.uniform(-1, 1, n) * np.exp(-t * 300) * 0.25
    return np.tanh((x + clic) * 1.6) * golpe


def snare(dur=0.25):
    n = int(dur * SR); t = np.arange(n) / SR
    ruido = hp(lp(rng.uniform(-1, 1, n), 7000), 1200) * np.exp(-t * 18)
    tono = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30) * 0.5
    return (ruido + tono) * 0.7


def clap(dur=0.3):
    n = int(dur * SR); t = np.arange(n) / SR
    e = sum(np.exp(-np.clip(t - o, 0, None) * 60) * (t >= o) for o in (0, 0.011, 0.023)) + np.exp(-t * 14) * 0.6
    return hp(lp(rng.uniform(-1, 1, n), 5000), 900) * e * 0.5


def hat(dur=0.06, abierto=False):
    dur = 0.25 if abierto else dur
    n = int(dur * SR); t = np.arange(n) / SR
    return hp(rng.uniform(-1, 1, n), 7500, 4) * np.exp(-t * (12 if abierto else 70)) * 0.35


def tecla(notas, dur, brillo=2500, trem=True):
    """Piano eléctrico suave: armónicos que se apagan y un ligero trémolo."""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for m in notas:
        f = hz(m) * (1 + rng.uniform(-0.0015, 0.0015))
        for k, a in ((1, 1), (2, 0.35), (3, 0.12), (4, 0.06)):
            x += a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (1.2 + k * 0.9))
    if trem: x *= 1 + 0.12 * np.sin(2 * np.pi * 4.5 * t)
    return lp(x * env(n, 0.01, 0.3, 0.7, 0.25, dur - 0.25), brillo) / len(notas)


def pad(notas, dur):
    """Colchón ancho de sierras desafinadas y filtradas."""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for m in notas:
        for det in (-0.004, 0, 0.004):
            f = hz(m + 12) * (1 + det)
            x += ((t * f) % 1 * 2 - 1) * 0.3
    return lp(x * env(n, 0.6, 0.5, 0.8, 0.6, dur - 0.6), 1600) / len(notas)


def pluck(m, dur=0.3):
    n = int(dur * SR); t = np.arange(n) / SR
    f = hz(m)
    x = ((t * f) % 1 * 2 - 1) + 0.5 * np.sign(np.sin(2 * np.pi * f * 1.005 * t))
    return lp(x * np.exp(-t * 9), 3200) * 0.25


def bajo(m, dur, ocho=False):
    n = int(dur * SR); t = np.arange(n) / SR
    if ocho:  # 808 con caída de tono al principio
        f = hz(m) * (1 + 0.6 * np.exp(-t * 40))
        x = np.tanh(np.sin(2 * np.pi * np.cumsum(f) / SR) * 2.2) * np.exp(-t * 1.6)
    else:
        x = np.sin(2 * np.pi * hz(m) * t) + 0.25 * np.sin(2 * np.pi * hz(m) * 2 * t)
        x *= env(n, 0.01, 0.1, 0.8, 0.08, dur - 0.08)
    return x * 0.55


def riser(dur):
    n = int(dur * SR); t = np.arange(n) / SR
    x = rng.uniform(-1, 1, n)
    out = np.zeros(n); paso = 2048
    for i in range(0, n, paso):  # el filtro se abre durante la subida
        f = 300 + 7000 * (i / n) ** 2
        out[i:i + paso] = lp(x[i:i + paso], f)
    return out * (t / dur) ** 2 * 0.35


def impacto():
    n = int(1.6 * SR); t = np.arange(n) / SR
    sub = np.sin(2 * np.pi * (40 + 60 * np.exp(-t * 10)) * t) * np.exp(-t * 2.2)
    return np.tanh(sub * 1.5) * 0.8 + lp(rng.uniform(-1, 1, n), 2500) * np.exp(-t * 6) * 0.25


def vinilo(n):
    x = lp(rng.uniform(-1, 1, n), 4000) * 0.012
    chasquidos = (rng.random(n) > 0.9997) * rng.uniform(-0.4, 0.4, n)
    return x + lp(chasquidos, 3000)


def reverb(x, largo=1.4, mezcla=0.22):
    n = int(largo * SR); t = np.arange(n) / SR
    ir = rng.uniform(-1, 1, n) * np.exp(-t * 4.5 / largo)
    ir = lp(ir, 5000); ir /= np.sqrt(np.sum(ir ** 2))
    return x * (1 - mezcla) + fftconvolve(x, ir)[: len(x)] * mezcla


def poner(pista, sonido, t, vol=1.0):
    i = int(t * SR)
    if i < 0: sonido, i = sonido[-i:], 0
    if i >= len(pista) or not len(sonido): return
    j = min(len(pista), i + len(sonido))
    pista[i:j] += sonido[: j - i] * vol


# ---------- canción ----------
def crear(estilo, duracion, drop, salida, tempo=None):
    t_def, acordes, raices = ESTILOS[estilo]
    tempo = tempo or t_def
    b = 60 / tempo; compas = 4 * b
    n = int((duracion + 2) * SR)
    armonia, ritmo, graves = np.zeros(n), np.zeros(n), np.zeros(n)
    # los acordes se alinean para que un compás empiece justo en el drop
    inicio = drop - math.ceil(drop / compas) * compas
    c = 0; t = inicio
    while t < duracion + 1:
        notas, raiz = acordes[c % 4], raices[c % 4]
        if t + compas > 0:
            ta = max(t, 0)
            if estilo == "lofi":
                poner(armonia, tecla(notas, compas + 0.3), ta, 0.9)
            elif estilo == "house":
                for k in range(8):  # acordes cortos a contratiempo
                    if k % 2 == 1: poner(armonia, tecla(notas, b * 0.45, 4000, False), t + k * b / 2, 0.8)
                poner(armonia, pad(notas, compas + 0.5), ta, 0.35)
            elif estilo == "trap":
                poner(armonia, pad(notas, compas + 0.5), ta, 0.45)
                for k, m in enumerate([notas[3] + 12, notas[2] + 12, notas[1] + 12, notas[2] + 12] * 2):
                    poner(armonia, pluck(m, 0.35), t + k * b / 2, 0.7)
            else:  # sueño
                poner(armonia, pad(notas, compas + 1.2), ta, 0.8)
                for k, m in enumerate([notas[0] + 24, notas[2] + 24, notas[3] + 24, notas[1] + 24]):
                    poner(armonia, tecla([m], b * 2, 5000, False), t + k * b, 0.35)
            if t >= drop - 0.01:  # a partir del drop entra el bajo y la batería
                if estilo == "trap":
                    poner(graves, bajo(raiz - 12, compas * 0.9, ocho=True), t, 0.9)
                elif estilo == "house":
                    for k in range(4): poner(graves, bajo(raiz - 12, b * 0.4), t + k * b + b / 2, 0.9)
                elif estilo == "lofi":
                    poner(graves, bajo(raiz - 12, b * 1.8), t, 0.8); poner(graves, bajo(raiz - 12, b * 1.5), t + b * 2.5, 0.6)
                else:
                    poner(graves, bajo(raiz - 12, compas), t, 0.5)
                for k in range(16):  # semicorcheas
                    tk = t + k * b / 4; tiempo = k / 4
                    if estilo == "lofi":
                        if k in (0, 7, 10): poner(ritmo, kick(0.4, 110, 45), tk, 0.9)
                        if k in (4, 12): poner(ritmo, snare(), tk + 0.02, 0.55)
                        if k % 2 == 0: poner(ritmo, hat(), tk + (0.03 if k % 4 else 0), 0.45 if k % 4 else 0.6)
                    elif estilo == "house":
                        if k % 4 == 0: poner(ritmo, kick(), tk, 1.0)
                        if k in (4, 12): poner(ritmo, clap(), tk, 0.7)
                        if k % 4 == 2: poner(ritmo, hat(abierto=True), tk, 0.5)
                        elif k % 2 == 1: poner(ritmo, hat(), tk, 0.3)
                    elif estilo == "trap":
                        if k in (0, 10): poner(ritmo, kick(0.5, 160, 50), tk, 1.0)
                        if k == 8: poner(ritmo, clap(), tk, 0.8)
                        if k >= 12 and c % 2 == 1:  # redoble de hi-hats al final de cada 2 compases
                            for r in range(3): poner(ritmo, hat(0.03), tk + r * b / 12, 0.4)
                        elif k % 2 == 0: poner(ritmo, hat(), tk, 0.45)
                    else:
                        if k == 0: poner(ritmo, kick(0.6, 90, 40), tk, 0.6)
        t += compas; c += 1
    # subida e impacto en el drop
    sube = min(2 * b, drop * 0.9)
    if sube > 0.3: poner(ritmo, riser(sube), drop - sube, 0.9)
    poner(ritmo, impacto(), drop, 0.55 if estilo != "sueño" else 0.4)
    # mezcla
    armonia = reverb(armonia, 1.8 if estilo == "sueño" else 1.2, 0.3)
    if estilo == "lofi":
        armonia = lp(armonia, 3500) + vinilo(n)
    intro = np.clip((np.arange(n) / SR) / max(drop, 0.01), 0, 1)
    filtro_intro = np.where(np.arange(n) / SR < drop, 0.8 + 0.2 * intro, 1)
    mezcla = armonia * filtro_intro + ritmo + lp(graves, 400)
    mezcla = mezcla[: int(duracion * SR)]
    cola = int(0.4 * SR); mezcla[-cola:] *= np.linspace(1, 0, cola)
    mezcla = np.tanh(mezcla / (np.max(np.abs(mezcla)) + 1e-9) * 1.3) * 0.89
    estereo = np.stack([mezcla, np.roll(mezcla, int(0.012 * SR)) * 0.96], 1)
    with wave.open(salida, "w") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((estereo * 32000).astype("<i2").tobytes())
    return salida


if __name__ == "__main__":
    import sys
    for e in ESTILOS:
        crear(e, 14, 2.4, f"{sys.argv[1] if len(sys.argv) > 1 else '.'}/prueba-{e}.wav")
