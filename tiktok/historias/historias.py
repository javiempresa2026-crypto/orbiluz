"""3 vídeos de historia para TikTok/Reels: problema → análisis → solución, historia de regalo y transformación.
Uso: python3 tiktok/historias/historias.py [nombre ...]
Las voces hablan en segunda persona («tú»): son narradoras de la marca, no clientas, y no se dan datos inventados."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from motor import montar, ROOT

H = f"{ROOT}/tiktok/historias/material"
M = f"{ROOT}/contenido/material"
E = f"{ROOT}/anuncios/meta/escenas"
OUT = f"{ROOT}/tiktok/historias/videos"
PARPADEO = "eq=eval=frame:brightness='if(lt(mod(t*6\\,1)\\,0.12)\\,-0.22\\,0)'"  # fluorescente que falla
ORB = {"orbiluz": "ORBILÚZ", "grave": "GRABE"}

VIDEOS = {
    # 1 · PROBLEMA → ANÁLISIS → SOLUCIÓN · voz Inés (grave, tono de explicación) · el ritmo entra al apagar la luz
    "h1-lo-que-te-quita-el-sueno": dict(voz=f"{H}/voz-h1-por-que-no-duermes.wav", musica="lofi", drop=13.1,
        transiciones=["corte", "corte", "desenfoque", "corte", "fundido", "fundido", "circulo"], segmentos=[
        dict(src=f"{H}/a1-movil-luz-techo.mp4", t0=0, t1=3.8),
        dict(src=f"{H}/c0-cuarto-antes.png", dur=1.8, mov="in", filtro=PARPADEO),
        dict(src=f"{H}/a1-movil-luz-techo.png", dur=2.3, mov="sube"),
        dict(src=f"{E}/escena-3.jpg", dur=3.2, mov="out", filtro="eq=saturation=0.7"),
        dict(src=f"{H}/a2-interruptor.mp4", t0=0.5, t1=3.8),
        dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=1.4, t1=4.3),
        dict(src=f"{H}/a3-cuarto-calido.mp4", t0=0, t1=4.4),
        dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=1.9),
    ], textos=[("LO QUE TE QUITA EL SUEÑO (Y NO ES EL MÓVIL)", 0, 2.8, "gancho"),
               ("Fuerte", 5.2, 5.8, "nota"), ("Fría", 5.8, 6.3, "nota"), ("Desde arriba", 6.3, 7.9, "nota"),
               ("Para tu cuerpo, sigue siendo de día", 8.0, 11.0, "nota"),
               ("Desde las 22:00", 12.4, 14.4, "nota"),
               ("Luz baja y cálida", 14.5, 17.2, "nota"),
               ("Guárdalo para esta noche", 21.7, 23.6, "nota")]),

    # 2 · HISTORIA · voz Marisol · la música se corta en «Silencio» y vuelve con fuerza cuando todos sacan el móvil
    "h2-el-regalo-que-se-graba": dict(voz=f"{H}/voz-h2-el-regalo.wav", musica="house", drop=10.9, silencio=(8.5, 10.9),
        transiciones=["corte", "corte", "desenfoque", "corte", "flash", "corte", "fundido"], segmentos=[
        dict(src=f"{H}/b1-regalos-calcetines.mp4", t0=0, t1=2.2),
        dict(src=f"{H}/b1-regalos-calcetines.mp4", t0=2.2, t1=5.0),
        dict(src=f"{H}/b1-regalos-calcetines.png", dur=1.4, mov="der"),
        dict(src=f"{H}/b2-caja-globo.mp4", t0=0, t1=2.2),
        dict(src=f"{H}/b2-caja-globo.mp4", t0=2.2, t1=4.5),
        dict(src=f"{H}/b3-moviles-graban.mp4", t0=0, t1=2.4),
        dict(src=f"{H}/b3-moviles-graban.mp4", t0=2.4, t1=5.0),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=2.5),
    ], textos=[("EL REGALO QUE DEJÓ A TODOS CALLADOS", 0, 2.6, "gancho")]),

    # 3 · TRANSFORMACIÓN · voz Ainsley · el mismo cuarto, un producto en cada paso, con adelanto del final en el segundo 5
    "h3-mismo-cuarto-otra-vida": dict(voz=f"{H}/voz-h3-cuarto-4-cosas.wav", musica="trap", drop=7.6,
        transiciones=["corte", "flash", "corte", "negro", "fundido", "fundido", "fundido", "fundido"], segmentos=[
        dict(src=f"{H}/c0-cuarto-antes.png", dur=3.5, mov="in", filtro=PARPADEO),
        dict(src=f"{H}/c0-cuarto-antes.png", dur=1.4, mov="out", filtro=PARPADEO),
        dict(src=f"{H}/c4-globo-final.png", dur=0.8, mov="in"),
        dict(src=f"{H}/a2-interruptor.mp4", t0=1.4, t1=3.3),
        dict(src=f"{H}/c1-lampara.png", dur=2.5, mov="in"),
        dict(src=f"{H}/c2-reloj.png", dur=1.8, mov="in"),
        dict(src=f"{H}/c3-proyector.png", dur=1.2, mov="in"),
        dict(src=f"{H}/c4-globo-final.png", dur=2.9, mov="in"),
        dict(src=f"{H}/c4-globo-final.png", dur=3.6, mov="out"),  # el clip animado deformaba los números del reloj
    ], textos=[("4 COSAS. MISMO CUARTO.", 0, 2.8, "gancho"), ("Antes", 2.9, 4.9, "nota"),
               ("Después", 4.9, 5.7, "nota"),
               ("Primero: fuera la luz del techo", 5.7, 7.6, "nota"), ("1/4 · Lámpara cálida", 7.6, 10.1, "nota"),
               ("2/4 · Reloj que se ve desde la cama", 10.1, 11.9, "nota"), ("3/4 · Olas en el techo", 11.9, 13.1, "nota"),
               ("4/4 · Globo que flota", 13.1, 16.0, "nota"), ("¿Cuál pondrías tú primero?", 17.6, 19.6, "nota")]),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n in (sys.argv[1:] or VIDEOS):
        v = dict(VIDEOS[n]); segs = v.pop("segmentos")
        montar(n, segs, OUT, correcciones=ORB, **v)
