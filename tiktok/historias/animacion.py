"""Animación de producto: el cuarto a oscuras y los 4 productos se encienden uno a uno.
Clip de Kling 3.0 con foto de inicio (solo la lámpara) y foto final (los 4 encendidos), Kling deformaba los minutos del reloj (salía «97»), así que en `-corregido` se pegan encima, fotograma a fotograma, los minutos reales de la foto final (23:47).
Uso: python3 tiktok/historias/animacion.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from motor import montar, ROOT

H = f"{ROOT}/tiktok/historias/material"
OUT = f"{ROOT}/tiktok/historias/videos"

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    montar("h4-se-encienden-uno-a-uno-v2", [
        dict(src=f"{H}/c0-cuarto-antes.png", dur=1.6, mov="in",
             filtro="eq=eval=frame:brightness='if(lt(mod(t*6\\,1)\\,0.12)\\,-0.22\\,0)'"),
        # el clip dura 6,3 s a 0,8x y se congela su último fotograma 2,6 s más: un fundido con la foto final
        # superponía dos relojes porque no encajan al píxel
        dict(src=f"{H}/d1-se-encienden-corregido.mp4", t0=0, t1=5.0, velocidad=0.8, dur=8.9),
    ], OUT, estilo_texto="ugc", logo=False, barra=False, real=True, voz=None, musica="sueño", drop=1.6, compas=False,
       transiciones=["negro"],
       textos=[("Apaga el techo y mira", 0, 1.6, "gancho"),
               ("1 · Lámpara", 1.9, 3.2, "nota"), ("2 · Reloj", 3.2, 4.6, "nota"),
               ("3 · Olas en el techo", 4.6, 6.2, "nota"), ("4 · Globo que flota", 6.2, 7.8, "nota"),
               ("¿Cuál encenderías primero?", 7.9, 10.4, "nota")])
