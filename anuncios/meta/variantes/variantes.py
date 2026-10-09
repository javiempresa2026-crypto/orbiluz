"""Variantes de anuncio con los ganchos nuevos: tipografía cinética «viral» (el gancho aparece palabra a palabra,
en mayúsculas, con la palabra clave *entre asteriscos* sobre un recuadro amarillo), planos cinemáticos con resplandor,
cámara lenta y grano de película. Sin voz: las voces disponibles no sonaban lo bastante naturales.
Cada variante en 9:16 (Reels e Historias) y 4:5 (feed).
Uso: python3 anuncios/meta/variantes/variantes.py [V1 V2 ...]"""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tiktok"))
from motor import montar, tarjeta_final, ROOT

C = f"{ROOT}/anuncios/meta/cine/material"
U = f"{ROOT}/anuncios/meta/ugc/material"
H = f"{ROOT}/tiktok/historias/material"
M = f"{ROOT}/contenido/material"
T = f"{ROOT}/tiktok/material"
F = f"{ROOT}/fotos"
OUT = f"{ROOT}/anuncios/meta/variantes"
VIRAL = dict(estilo_texto="viral", real="grano", logo=False, barra=False, voz=None, compas=False)
PARPADEO = "eq=eval=frame:brightness='if(lt(mod(t*6\\,1)\\,0.12)\\,-0.22\\,0)'"


def variantes(tmp):
    fin = lambda n, frase, fondo: tarjeta_final(f"{tmp}/{n}.jpg", frase=frase, fondo=fondo)
    return {
        # ---------- LÁMPARA ----------
        "V1-lampara-regalo-5cm": dict(**VIRAL, musica="house", drop=2.6, transiciones=["corte", "corte", "flash", "corte", "negro"], segmentos=[
            dict(src=f"{U}/u1-unboxing.mp4", t0=0, t1=2.6),
            dict(src=f"{C}/c1-lampara.mp4", t0=0.5, t1=3.0, velocidad=0.6, brillo=0.3),
            dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=2.4, t1=4.0),
            dict(src=f"{F}/lampara-4-modelos.jpg", dur=1.8, mov="in", ajustar=True, brillo=0.25),
            dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=1.8),
            dict(src=fin("f1", "Un planeta en tu mesilla", f"{C}/h1-lampara-macro.png"), dur=2.0, mov="in"),
        ], textos=[("El regalo de *5 cm* | que nadie olvida", 0.15, 3.0, "gancho"),
                   ("Grabado láser dentro del cristal", 3.2, 6.6, "nota"),
                   ("Saturno · Luna · Galaxia · Sistema solar", 6.8, 10.2, "nota")]),

        "V2-lampara-sobra-luz-de-techo": dict(**VIRAL, musica="lofi", drop=4.4, transiciones=["corte", "negro", "flash", "fundido", "negro"], segmentos=[
            dict(src=f"{H}/c0-cuarto-antes.png", dur=2.4, mov="in", filtro=PARPADEO),
            dict(src=f"{H}/a2-interruptor.mp4", t0=1.4, t1=3.4),
            dict(src=f"{C}/c1-lampara.mp4", t0=0, t1=2.4, velocidad=0.6, brillo=0.3),
            dict(src=f"{H}/c1-lampara.png", dur=2.0, mov="in", brillo=0.2),
            dict(src=f"{H}/a3-cuarto-calido.mp4", t0=0, t1=2.2),
            dict(src=fin("f2", "Luz cálida para tu mesilla", f"{C}/h1-lampara-macro.png"), dur=2.0, mov="in"),
        ], textos=[("No te falta decoración. | Te sobra *luz de techo.*", 0.15, 4.4, "gancho"),
                   ("Apágala", 2.5, 4.4, "nota"),
                   ("Y enciende un planeta", 4.5, 8.3, "nota"),
                   ("Bola de 5 cm · luz cálida", 8.4, 11.6, "nota")]),

        # ---------- PROYECTOR ----------
        "V3-proyector-fondo-de-una-piscina": dict(**VIRAL, musica="sueño", drop=3.0, transiciones=["fundido", "corte", "corte", "negro"], segmentos=[
            dict(src=f"{C}/c2-proyector-bucle.mp4", t0=0, t1=5.0, velocidad=0.8, brillo=0.25),
            dict(src=f"{U}/u2-olas.mp4", t0=0, t1=2.4),
            dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=2.2),
            dict(src=f"{C}/c2-proyector-bucle.mp4", t0=0, t1=1.6),
            dict(src=fin("f3", "Tu cuarto, bajo el mar", f"{C}/h2-proyector-techo.png"), dur=2.0, mov="in"),
        ], textos=[("Dormir en el fondo | de una *piscina*", 0.15, 3.6, "gancho"),
                   ("Olas que se mueven solas", 3.8, 6.5, "nota"),
                   ("16 colores · con mando", 6.6, 10.4, "nota")]),

        "V4-proyector-miran-el-techo": dict(**VIRAL, musica="trap", drop=2.5, transiciones=["corte", "corte", "fundido", "negro"], segmentos=[
            dict(src=f"{U}/u2-transicion.mp4", t0=0.6, t1=4.2),
            dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=2.6),
            dict(src=f"{C}/c2-proyector-bucle.mp4", t0=1.0, t1=4.0, velocidad=0.8, brillo=0.25),
            dict(src=f"{U}/u2-olas.mp4", t0=1.5, t1=3.6),
            dict(src=fin("f4", "Tu cuarto, bajo el mar", f"{C}/h2-proyector-techo.png"), dur=2.0, mov="in"),
        ], textos=[("Para los que miran | *el techo* | antes de dormir", 0.15, 3.4, "gancho"),
                   ("Apaga la luz grande", 3.5, 6.2, "nota"),
                   ("Y que se mueva el mar", 6.3, 10.0, "nota")]),

        # ---------- GLOBO ----------
        "V5-globo-sin-explicacion": dict(**VIRAL, musica="trap", drop=3.2, transiciones=["corte", "corte", "corte", "negro"], segmentos=[
            dict(src=f"{C}/c3-globo.mp4", t0=0, t1=2.6, velocidad=0.8, brillo=0.25),
            dict(src=f"{U}/u3-dedo-globo.mp4", t0=0, t1=2.8),
            dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=2.0),
            dict(src=f"{C}/c3-globo.mp4", t0=2.6, t1=4.4, velocidad=0.7, brillo=0.3),
            dict(src=fin("f5", "El mundo, flotando en tu escritorio", f"{C}/h3-globo-oscuridad.png"), dur=2.0, mov="in"),
        ], textos=[("Sin hilos. | Sin trucos. | *Sin explicación.*", 0.15, 3.3, "gancho"),
                   ("Lo tocas y sigue flotando", 3.4, 6.3, "nota"),
                   ("Levitación magnética · 14 cm", 6.4, 11.0, "nota")]),

        "V6-globo-todo-el-mundo-lo-graba": dict(**VIRAL, musica="house", drop=3.4, transiciones=["corte", "flash", "corte", "negro"], segmentos=[
            dict(src=f"{H}/b2-caja-globo.mp4", t0=0.5, t1=4.6),
            dict(src=f"{H}/b3-moviles-graban.mp4", t0=0, t1=3.0),
            dict(src=f"{C}/c3-globo.mp4", t0=1.0, t1=3.4, velocidad=0.7, brillo=0.3),
            dict(src=f"{H}/b3-moviles-graban.mp4", t0=3.0, t1=4.6),
            dict(src=fin("f6", "El regalo que todos graban", f"{C}/h3-globo-oscuridad.png"), dur=2.0, mov="in"),
        ], textos=[("Lo que todo el mundo | *graba* | al abrirlo", 0.15, 3.4, "gancho"),
                   ("Flota y gira solo", 4.2, 7.2, "nota"),
                   ("Globo de 14 cm · mapa en inglés", 7.3, 11.4, "nota")]),

        # ---------- LOS 4 ----------
        "V7-cuatro-cambia-la-luz": dict(**VIRAL, musica="house", drop=1.6, transiciones=["negro", "flash", "fundido", "negro"], segmentos=[
            dict(src=f"{H}/c0-cuarto-antes.png", dur=1.6, mov="in", filtro=PARPADEO),
            dict(src=f"{H}/d1-se-encienden-corregido.mp4", t0=0, t1=5.0, velocidad=0.85),
            dict(src=f"{C}/h4-los-cuatro.png", dur=2.4, mov="in", brillo=0.3),
            dict(src=f"{C}/h4-los-cuatro.png", dur=1.4, mov="out", brillo=0.3),
            dict(src=fin("f7", "Decoración que se enciende", f"{C}/h4-los-cuatro.png"), dur=2.0, mov="in"),
        ], textos=[("Deja de comprar cojines. | *Cambia la luz.*", 0.15, 3.0, "gancho"),
                   ("Lámpara · Reloj · Olas · Globo", 3.2, 7.4, "nota"),
                   ("4 luces, 1 cuarto nuevo", 7.5, 11.2, "nota")]),
    }


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        pedidos = sys.argv[1:]
        for n, v in variantes(tmp).items():
            if pedidos and not any(n.startswith(p) for p in pedidos): continue
            v = dict(v); segs = v.pop("segmentos")
            montar(n, segs, OUT, formato_4x5=True, **v)
