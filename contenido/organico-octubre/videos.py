"""6 vídeos orgánicos (TikTok, Reels, Facebook) hechos solo con material existente, sin créditos de IA.
Estilo «viral» (gancho en mayúsculas palabra a palabra, palabra clave en amarillo), sin voz, con grano.
Uso: python3 contenido/organico-octubre/videos.py [O1 O2 ...]"""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tiktok"))
from motor import montar, tarjeta_final, ROOT

C = f"{ROOT}/anuncios/meta/cine/material"
U = f"{ROOT}/anuncios/meta/ugc/material"
H = f"{ROOT}/tiktok/historias/material"
M = f"{ROOT}/contenido/material"
T = f"{ROOT}/tiktok/material"
OUT = f"{ROOT}/contenido/organico-octubre"
VIRAL = dict(estilo_texto="viral", real="grano", logo=False, barra=False, voz=None, compas=False)


def videos(tmp):
    fin = lambda n, frase, fondo: tarjeta_final(f"{tmp}/{n}.jpg", frase=frase, fondo=fondo)
    return {
        # POV: el cambio de luz en un solo plano (problema → solución)
        "O1-pov-apagas-la-luz": dict(**VIRAL, musica="sueño", drop=4.6, transiciones=["corte", "fundido", "negro"], segmentos=[
            dict(src=f"{U}/u2-transicion.mp4", t0=0, t1=5.0),
            dict(src=f"{H}/a3-cuarto-calido.mp4", t0=0, t1=2.6, brillo=0.2),
            dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=2.4),
            dict(src=fin("f1", "Luz que cambia tu cuarto", f"{C}/h2-proyector-techo.png"), dur=2.0, mov="in"),
        ], textos=[("POV: apagas la luz del techo | por *primera vez*", 0.15, 4.6, "gancho"),
                   ("Olas en el techo + un planeta de 5 cm", 5.0, 9.6, "nota@560")]),

        # Lista: 4 cosas (formato muy nativo de TikTok)
        "O2-cosas-que-no-sabia": dict(**VIRAL, musica="house", drop=2.4, transiciones=["corte", "flash", "corte", "flash", "corte", "negro"], segmentos=[
            dict(src=f"{H}/a1-movil-luz-techo.mp4", t0=0.5, t1=2.5),
            dict(src=f"{C}/c1-lampara.mp4", t0=0.5, t1=2.6, velocidad=0.8, brillo=0.3),
            dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=1.0, t1=3.2),
            dict(src=f"{C}/c3-globo.mp4", t0=0.5, t1=2.7, velocidad=0.8, brillo=0.25),
            dict(src=f"{H}/d1-se-encienden-corregido.mp4", t0=2.6, t1=5.0),
            dict(src=fin("f2", "Decoración que se enciende", f"{C}/h4-los-cuatro.png"), dur=2.0, mov="in"),
        ], textos=[("Cosas que mi cuarto | necesitaba | y *no sabía*", 0.15, 2.2, "gancho"),
                   ("1. Un planeta de 5 cm", 2.1, 4.5, "nota@560"),
                   ("2. Olas en el techo", 4.7, 6.7, "nota@560"),
                   ("3. Un globo que flota", 6.9, 9.2, "nota@560"),
                   ("4. Un reloj de dígitos 3D", 9.6, 11.9, "nota@560")]),

        # Regalo: llevar la contraria
        "O3-no-regales-calcetines": dict(**VIRAL, musica="trap", drop=2.6, transiciones=["corte", "flash", "corte", "corte", "negro"], segmentos=[
            dict(src=f"{H}/b1-regalos-calcetines.mp4", t0=0, t1=2.6),
            dict(src=f"{M}/viral-regalo-lampara-9x16.mp4", t0=0, t1=2.4, brillo=0.2),
            dict(src=f"{U}/u1-unboxing.mp4", t0=1.0, t1=3.6),
            dict(src=f"{H}/b2-caja-globo.mp4", t0=1.5, t1=5.0),
            dict(src=f"{H}/b3-moviles-graban.mp4", t0=1.0, t1=3.4),
            dict(src=fin("f3", "Regala algo que se encienda", f"{C}/h4-los-cuatro.png"), dur=2.0, mov="in"),
        ], textos=[("Este año | *no regales calcetines*", 0.15, 2.6, "gancho"),
                   ("Regala algo que se encienda", 2.7, 7.4, "nota@560"),
                   ("Y que todos quieran grabar", 11.2, 13.4, "nota@560")]),

        # Curiosidad: el globo
        "O4-como-flota-esto": dict(**VIRAL, musica="trap", drop=3.0, transiciones=["corte", "corte", "flash", "negro"], segmentos=[
            dict(src=f"{C}/c3-globo.mp4", t0=0, t1=2.8, velocidad=0.8, brillo=0.25),
            dict(src=f"{U}/u3-dedo-globo.mp4", t0=0, t1=3.0),
            dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=0, t1=2.6),
            dict(src=f"{H}/b2-caja-globo.mp4", t0=2.6, t1=5.0, velocidad=0.8),
            dict(src=fin("f4", "El mundo, flotando en tu escritorio", f"{C}/h3-globo-oscuridad.png"), dur=2.0, mov="in"),
        ], textos=[("¿Cómo flota | *esto?*", 0.15, 3.2, "gancho"),
                   ("Levitación magnética: la base lo sostiene", 3.3, 7.4, "nota@560"),
                   ("Gira solo y se ilumina · 14 cm", 7.5, 11.0, "nota@560")]),

        # Producto: la lámpara, con su medida real
        "O5-planeta-en-tu-mano": dict(**VIRAL, musica="lofi", drop=2.8, transiciones=["corte", "corte", "fundido", "corte", "negro"], segmentos=[
            dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=0, t1=3.0),
            dict(src=f"{M}/viral-mano-bola-9x16.mp4", t0=0.5, t1=3.0),
            dict(src=f"{C}/c1-lampara.mp4", t0=0, t1=2.6, velocidad=0.7, brillo=0.3),
            dict(src=f"{M}/viral-lampara-se-enciende-9x16.mp4", t0=1.0, t1=4.0),
            dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=2.2),
            dict(src=fin("f5", "Un planeta en tu mesilla", f"{C}/h1-lampara-macro.png"), dur=2.0, mov="in"),
        ], textos=[("El planeta | que cabe en tu *mano*", 0.15, 3.0, "gancho"),
                   ("Bola de cristal de 5 cm", 3.1, 5.4, "nota@560"),
                   ("Saturno, Luna, Galaxia o Sistema solar", 5.5, 9.4, "nota@560"),
                   ("Luz cálida por USB", 9.5, 12.0, "nota@560")]),

        # Identidad: rutina de noche
        "O6-mi-rutina-de-noche": dict(**VIRAL, musica="sueño", drop=2.0, transiciones=["corte", "negro", "fundido", "corte", "negro"], segmentos=[
            dict(src=f"{H}/a2-interruptor.mp4", t0=1.2, t1=3.4),
            dict(src=f"{C}/c2-proyector-bucle.mp4", t0=0, t1=3.0, velocidad=0.8, brillo=0.25),
            dict(src=f"{U}/u2-olas.mp4", t0=0, t1=2.6),
            dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=1.0, t1=3.4, brillo=0.2),
            dict(src=f"{H}/a3-cuarto-calido.mp4", t0=1.0, t1=3.6),
            dict(src=fin("f6", "Tu cuarto, de noche bien hecho", f"{C}/h2-proyector-techo.png"), dur=2.0, mov="in"),
        ], textos=[("Mi rutina | de *noche*", 0.15, 2.2, "gancho"),
                   ("Apago la luz del techo", 0.9, 2.2, "nota"),
                   ("Enciendo las olas", 2.3, 8.5, "nota@560"),
                   ("Y un planeta en la mesilla", 8.7, 10.4, "nota@560"),
                   ("Móvil fuera. A dormir.", 10.5, 13.0, "nota@560")]),
    }


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        pedidos = sys.argv[1:]
        for n, v in videos(tmp).items():
            if pedidos and not any(n.startswith(p) for p in pedidos): continue
            v = dict(v); segs = v.pop("segmentos")
            montar(n, segs, OUT, formato_4x5=True, **v)
