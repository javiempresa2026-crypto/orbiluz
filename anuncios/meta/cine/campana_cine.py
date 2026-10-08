"""Campaña «Cinemática»: planos de producto tipo anuncio de marca (macro, cámara lenta, luz dramática) con títulos de tráiler.
4 vídeos (9:16 y 4:5): lámpara, proyector, globo y los 4 juntos. Sin voz: el texto cuenta la idea y la música marca el ritmo.
Uso: python3 anuncios/meta/cine/campana_cine.py [CI1 CI2 CI3 CI4]"""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tiktok"))
from motor import montar, tarjeta_final, ROOT

C = f"{ROOT}/anuncios/meta/cine/material"
M = f"{ROOT}/contenido/material"
T = f"{ROOT}/tiktok/material"
F = f"{ROOT}/fotos"
OUT = f"{ROOT}/anuncios/meta/cine"
CINE = dict(estilo_texto="cine", logo=False, barra=False, voz=None, compas=False)


def videos(tmp):
    fin = lambda nombre, frase, fondo: tarjeta_final(f"{tmp}/{nombre}.jpg", frase=frase, fondo=fondo)
    return {
        "CI1-grabado-dentro-del-cristal": dict(**CINE, musica="lofi", drop=6.3, transiciones=["fundido", "negro"], segmentos=[
            dict(src=f"{C}/c1-lampara.mp4", t0=0, t1=5.0, velocidad=0.8),
            dict(src=f"{F}/lampara-4-modelos.jpg", dur=2.0, mov="in", ajustar=True),
            dict(src=fin("fin1", "Un planeta en tu mesilla", f"{C}/h1-lampara-macro.png"), dur=2.2, mov="in"),
        ], textos=[("Esto está grabado", 0.3, 2.2, "gancho"), ("dentro del cristal.", 2.2, 4.4, "gancho"),
                   ("Bola de 5 cm · grabado láser 3D", 4.5, 6.2, "nota"),
                   ("Saturno · Luna · Galaxia · Sistema solar", 6.4, 8.3, "nota")]),

        "CI2-tu-techo-puede-hacer-esto": dict(**CINE, musica="sueño", drop=1.8, transiciones=["fundido", "corte", "negro"], segmentos=[
            # el clip de Kling del proyector (c2) no se usa: añadió humo saliendo del cubo y el producto no echa vapor
            dict(src=f"{C}/h2-proyector-techo.png", dur=2.6, mov="sube"),
            dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=3.4),
            dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=2.2),
            dict(src=fin("fin2", "Tu cuarto, bajo el mar", f"{C}/h2-proyector-techo.png"), dur=2.2, mov="in"),
        ], textos=[("Tu techo", 0.3, 1.8, "gancho"), ("puede hacer esto.", 1.8, 4.4, "gancho"),
                   ("Olas en movimiento · 16 colores", 4.6, 6.2, "nota"), ("Con mando y por USB", 6.3, 8.4, "nota")]),

        "CI3-flota-gira-brilla": dict(**CINE, musica="trap", drop=2.9, transiciones=["fundido", "negro"], segmentos=[
            dict(src=f"{C}/c3-globo.mp4", t0=0, t1=5.0, velocidad=0.8),
            dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=1.0, t1=3.2),
            dict(src=fin("fin3", "El mundo, flotando en tu escritorio", f"{C}/h3-globo-oscuridad.png"), dur=2.2, mov="in"),
        ], textos=[("Flota.", 0.4, 1.6, "gancho"), ("Gira.", 1.6, 2.8, "gancho"), ("Brilla.", 2.8, 4.6, "gancho"),
                   ("Levitación magnética · sin hilos", 4.8, 6.4, "nota"), ("Globo de 14 cm · mapa en inglés", 6.5, 8.4, "nota")]),

        "CI4-cuatro-luces": dict(**CINE, musica="house", drop=2.6, transiciones=["corte", "corte", "corte", "fundido", "negro"], segmentos=[
            dict(src=f"{C}/h4-los-cuatro.png", dur=2.6, mov="in"),
            dict(src=f"{C}/c1-lampara.mp4", t0=1.5, t1=2.9),
            dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=1.0, t1=2.4),
            dict(src=f"{C}/c3-globo.mp4", t0=2.0, t1=3.4),
            dict(src=f"{C}/h4-los-cuatro.png", dur=2.2, mov="out"),
            dict(src=fin("fin4", "Decoración que se enciende", f"{C}/h4-los-cuatro.png"), dur=2.2, mov="in"),
        ], textos=[("4 luces que cambian", 0.3, 1.5, "gancho"), ("un cuarto de noche.", 1.5, 2.6, "gancho"),
                   ("Lámpara planeta", 2.6, 4.0, "nota"), ("Proyector de olas", 4.0, 5.4, "nota"),
                   ("Globo que levita", 5.4, 6.8, "nota"), ("Y reloj 3D", 6.8, 9.0, "nota")]),
    }


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        pedidos = sys.argv[1:]
        for n, v in videos(tmp).items():
            if pedidos and not any(n.startswith(p) for p in pedidos): continue
            v = dict(v); segs = v.pop("segmentos")
            montar(n, segs, OUT, formato_4x5=True, **v)
