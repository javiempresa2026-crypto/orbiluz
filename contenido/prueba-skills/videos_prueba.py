"""Prueba de las skills (creativos-anuncios + contenido-organico): 2 vídeos orgánicos 9:16 con estilo «viral»,
sin voz, con 2 escenas nuevas de Higgsfield (nano_banana_2, 3 créditos) y clips que ya teníamos.
Uso: python3 contenido/prueba-skills/videos_prueba.py [P1 P2]"""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tiktok"))
from motor import montar, tarjeta_final, ROOT

N = f"{ROOT}/contenido/prueba-skills/material"
C = f"{ROOT}/anuncios/meta/cine/material"
U = f"{ROOT}/anuncios/meta/ugc/material"
H = f"{ROOT}/tiktok/historias/material"
M = f"{ROOT}/contenido/material"
OUT = f"{ROOT}/contenido/prueba-skills"
VIRAL = dict(estilo_texto="viral", real="grano", logo=False, barra=False, voz=None, compas=False)
PARPADEO = "eq=eval=frame:brightness='if(lt(mod(t*6\\,1)\\,0.12)\\,-0.22\\,0)'"


def videos(tmp):
    fin = lambda n, frase, fondo: tarjeta_final(f"{tmp}/{n}.jpg", frase=frase, fondo=fondo)
    return {
        # Problema → solución (el formato que mejor retuvo en orgánico)
        "P1-cuarto-mal-iluminado": dict(**VIRAL, musica="lofi", drop=4.2, transiciones=["corte", "negro", "flash", "corte", "fundido"], segmentos=[
            dict(src=f"{H}/c0-cuarto-antes.png", dur=2.4, mov="in", filtro=PARPADEO),
            dict(src=f"{H}/a2-interruptor.mp4", t0=1.4, t1=3.4),
            dict(src=f"{N}/p1-dormitorio-olas.png", dur=2.8, mov="in", ajustar=True, brillo=0.25),
            dict(src=f"{U}/u2-olas.mp4", t0=0, t1=2.2),
            dict(src=f"{C}/c1-lampara.mp4", t0=0.5, t1=2.6, velocidad=0.7, brillo=0.3),
            dict(src=fin("f1", "Luz que cambia tu cuarto", f"{N}/p1-dormitorio-olas.png"), dur=2.0, mov="in"),
        ], textos=[("Tu cuarto no es feo. | Está *mal iluminado.*", 0.15, 4.2, "gancho"),
                   ("Apaga la luz del techo", 2.6, 4.2, "nota"),
                   ("Olas en el techo + un planeta de 5 cm", 4.4, 8.4, "nota@560"),
                   ("Proyector y lámpara · orbiluz.com", 8.5, 11.6, "nota@560")]),

        # Identidad / curiosidad: escritorio de noche
        "P2-escritorio-23-47": dict(**VIRAL, musica="house", drop=2.8, transiciones=["corte", "flash", "corte", "negro"], segmentos=[
            dict(src=f"{N}/p2-escritorio-globo-reloj.png", dur=2.8, mov="in", ajustar=True, brillo=0.25),
            dict(src=f"{C}/c3-globo.mp4", t0=0, t1=2.6, velocidad=0.8, brillo=0.25),
            dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=2.6),
            dict(src=f"{N}/p2-escritorio-globo-reloj.png", dur=2.8, mov="out", ajustar=True, brillo=0.2),
            dict(src=fin("f2", "Tu escritorio, de otro planeta", f"{N}/p2-escritorio-globo-reloj.png"), dur=2.0, mov="in"),
        ], textos=[("Mi escritorio | a las *23:47*", 0.15, 3.0, "gancho"),
                   ("Un globo que flota solo · 14 cm", 3.1, 8.4, "nota"),
                   ("Y un reloj de dígitos 3D", 8.7, 10.9, "nota@560")]),
    }


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        pedidos = sys.argv[1:]
        for n, v in videos(tmp).items():
            if pedidos and not any(n.startswith(p) for p in pedidos): continue
            v = dict(v); segs = v.pop("segmentos")
            montar(n, segs, OUT, formato_4x5=True, **v)
