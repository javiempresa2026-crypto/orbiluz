"""3 anuncios de vídeo para testear en Meta (9:16 para Reels e Historias y 4:5 para el feed).
M1 · Problema → solución con aspecto de Instagram nativo (lámpara + proyector).
M2 · Animación: los 4 productos se encienden uno a uno.
M3 · Amigo invisible: la lámpara como regalo (temporada de Navidad).
Uso: python3 anuncios/meta/video/anuncios_video.py [M1 M2 M3]"""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tiktok"))
from motor import montar, tarjeta_final, ROOT

H = f"{ROOT}/tiktok/historias/material"
M = f"{ROOT}/contenido/material"
E = f"{ROOT}/anuncios/meta/escenas"
F = f"{ROOT}/fotos"
A = f"{ROOT}/anuncios/meta/video/material"
OUT = f"{ROOT}/anuncios/meta/video"
PARPADEO = "eq=eval=frame:brightness='if(lt(mod(t*6\\,1)\\,0.12)\\,-0.22\\,0)'"
CORR = {"orbiluz": "ORBILÚZ", "planera": "planeta.", "mesiña": "mesilla"}


def anuncios(tmp):
    fin_globo = tarjeta_final(f"{tmp}/fin-globo.jpg", fondo=f"{H}/c4-globo-final.png")
    fin_lampara = tarjeta_final(f"{tmp}/fin-lampara.jpg", frase="Elige el suyo", fondo=f"{F}/lampara-saturno-noche.jpg")
    return {
        # M1 · PROBLEMA → SOLUCIÓN, con textos en caja blanca como los de Instagram, sin logo ni barra
        "M1-ig-lo-que-te-quita-el-sueno": dict(
            voz=f"{H}/voz-h1-por-que-no-duermes.wav", musica="lofi", drop=13.1,
            estilo_texto="ig", logo=False, barra=False,
            transiciones=["corte", "corte", "desenfoque", "corte", "fundido", "fundido", "circulo"], segmentos=[
                dict(src=f"{H}/a1-movil-luz-techo.mp4", t0=0, t1=3.8),
                dict(src=f"{H}/c0-cuarto-antes.png", dur=1.8, mov="in", filtro=PARPADEO),
                dict(src=f"{H}/a1-movil-luz-techo.png", dur=2.3, mov="sube"),
                dict(src=f"{E}/escena-3.jpg", dur=3.2, mov="out", filtro="eq=saturation=0.7"),
                dict(src=f"{H}/a2-interruptor.mp4", t0=0.5, t1=3.8),
                dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=1.4, t1=4.3),
                dict(src=f"{H}/a3-cuarto-calido.mp4", t0=0, t1=4.4),
                dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=1.9),
            ],
            textos=[("Lo que te quita el sueño (y no es el móvil)", 0, 2.8, "gancho"),
                    ("Fuerte", 5.2, 5.8, "nota"), ("Fría", 5.8, 6.3, "nota"), ("Desde arriba", 6.3, 7.9, "nota"),
                    ("Para tu cuerpo, sigue siendo de día", 8.0, 11.0, "nota"),
                    ("Desde las 22:00", 12.4, 14.4, "nota"), ("Luz baja y cálida", 14.5, 17.2, "nota"),
                    ("Luz cálida para tu mesilla → orbiluz.com", 21.7, 23.6, "nota")]),

        # M2 · ANIMACIÓN: un plano en el que se encienden los 4 productos, con tarjeta final
        "M2-animacion-se-encienden": dict(
            voz=None, musica="sueño", drop=1.6, compas=False,
            transiciones=["negro", "fundido"], segmentos=[
                dict(src=f"{H}/c0-cuarto-antes.png", dur=1.6, mov="in", filtro=PARPADEO),
                dict(src=f"{H}/d1-se-encienden-corregido.mp4", t0=0, t1=5.0, velocidad=0.8, dur=8.9),
                dict(src=fin_globo, dur=2.2, mov="in"),
            ],
            textos=[("APAGA EL TECHO Y MIRA", 0, 1.6, "gancho"),
                    ("1 · Lámpara", 1.9, 3.2, "nota"), ("2 · Reloj", 3.2, 4.6, "nota"),
                    ("3 · Olas en el techo", 4.6, 6.2, "nota"), ("4 · Globo que flota", 6.2, 7.8, "nota"),
                    ("¿Cuál encenderías primero?", 7.9, 10.4, "nota")]),

        # M3 · AMIGO INVISIBLE: la lámpara como regalo, voz de Marisol, el ritmo entra con «Regala un planeta»
        "M3-amigo-invisible-lampara": dict(
            voz=f"{A}/voz-m3-amigo-invisible.wav", musica="house", drop=5.3,
            transiciones=["corte", "flash", "corte", "corte", "corte", "fundido", "corte", "fundido", "negro"], segmentos=[
                dict(src=f"{H}/b1-regalos-calcetines.mp4", t0=0, t1=4.1),
                dict(src=f"{H}/b1-regalos-calcetines.png", dur=1.2, mov="der"),
                dict(src=f"{M}/viral-regalo-lampara-9x16.mp4", t0=0, t1=3.0),
                dict(src=f"{F}/lampara-luna-noche.jpg", dur=0.6, mov="in"),
                dict(src=f"{F}/lampara-galaxia-noche.jpg", dur=1.0, mov="out"),
                dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=2.4, t1=3.9),
                dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=2.8),
                dict(src=f"{F}/lampara-4-modelos.jpg", dur=2.1, mov="in", ajustar=True),
                dict(src=f"{M}/viral-regalo-lampara-9x16.mp4", t0=2.7, t1=5.0),
                dict(src=fin_lampara, dur=2.0, mov="in"),
            ],
            textos=[("AMIGO INVISIBLE: RESUELTO", 0, 2.7, "gancho")]),
    }


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        todos = anuncios(tmp)
        pedidos = sys.argv[1:]
        for n, v in todos.items():
            if pedidos and not any(n.startswith(p) for p in pedidos): continue
            v = dict(v); segs = v.pop("segmentos")
            montar(n, segs, OUT, correcciones=CORR, formato_4x5=True, **v)
