"""Guiones de los TikTok de Orbiluz. Uso: python3 tiktok/videos.py [nombre ...]"""
import os, sys
from motor import montar, ROOT

M = f"{ROOT}/contenido/material"     # clips ya generados
T = f"{ROOT}/tiktok/material"        # clips y voces de esta tanda
F = f"{ROOT}/fotos"
E = f"{ROOT}/anuncios/meta/escenas"
OUT = f"{ROOT}/tiktok/videos"
ORB = {"orbiluz": "ORBILÚZ"}  # Whisper escribe la marca de varias formas

VIDEOS = {
    # ---------- LÁMPARA ----------
    "t1-lampara-apaga-el-techo": dict(voz=f"{T}/voz-t1-lampara.wav", segmentos=[
        dict(src=f"{E}/escena-3.jpg", dur=2.6, zoom="in", filtro="eq=saturation=0.75"),
        dict(src=f"{M}/viral-lampara-se-enciende-9x16.mp4", t0=0.6, t1=4.4),
        dict(src=f"{M}/viral-mano-bola-9x16.mp4", t0=0, t1=2.6),
        dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=2.2),
        dict(src=f"{F}/lampara-saturno-noche.jpg", dur=1.1),
        dict(src=f"{F}/lampara-luna-noche.jpg", dur=1.1),
        dict(src=f"{F}/lampara-galaxia-noche.jpg", dur=1.1),
        dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=2.2, t1=4.0),
    ], textos=[("HAZ ESTO ESTA NOCHE", 0, 2.4, "gancho")]),

    "t2-lampara-cual-eliges": dict(voz=None, segmentos=[
        dict(src=f"{M}/viral-mano-bola-9x16.mp4", t0=0, t1=2.2),
        dict(src=f"{F}/lampara-saturno-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-luna-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-galaxia-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-sistema-solar-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-4-modelos.jpg", dur=2.4, zoom="out", ajustar=True),
    ], textos=[("ELIGE TU PLANETA", 0, 2.1, "gancho"),
               ("1 · Saturno", 2.2, 3.8, "nota"), ("2 · La Luna", 3.8, 5.4, "nota"),
               ("3 · Galaxia", 5.4, 7.0, "nota"), ("4 · Sistema solar", 7.0, 8.6, "nota"),
               ("Comenta tu número", 8.6, 11, "nota")]),

    # ---------- GLOBO ----------
    "t3-globo-explicame-esto": dict(voz=f"{T}/voz-t3-globo.wav", segmentos=[
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=3.0),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=0, t1=3.0, velocidad=0.8),
        dict(src=f"{F}/globo-levita-noche.jpg", dur=2.4),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=2.0, t1=5.0, velocidad=0.8),
        dict(src=f"{F}/globo-levita-escritorio.jpg", dur=2.2, zoom="out"),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=2.0, t1=5.0),
    ], textos=[("¿CÓMO FLOTA ESTO?", 0, 2.6, "gancho")]),

    "t4-globo-escritorio": dict(voz=None, segmentos=[
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=0, t1=2.5),
        dict(src=f"{F}/globo-levita-ambiente.jpg", dur=1.8),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0.5, t1=3.5, velocidad=0.7),
        dict(src=f"{F}/globo-levita-estudio.jpg", dur=1.6, zoom="out"),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=2.5, t1=5.0, velocidad=0.8),
    ], textos=[("Lo que todo el mundo pregunta al entrar a mi despacho", 0, 2.6, "gancho"),
               ("No tiene hilos.", 2.7, 4.6, "nota"), ("Flota y gira solo.", 4.6, 8.8, "nota"),
               ("¿Lo pondrías en tu escritorio?", 8.8, 13, "nota")]),

    # ---------- PROYECTOR ----------
    "t5-proyector-fondo-del-mar": dict(voz=f"{T}/voz-t5-proyector.wav", segmentos=[
        dict(src=f"{F}/proyector-ondas-noche.jpg", dur=1.6),
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=5.0),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=4.0),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=3.4, t1=5.0),
    ], textos=[("TU CUARTO, BAJO EL MAR", 0, 2.0, "gancho")]),

    "t6-proyector-colores": dict(voz=None, segmentos=[
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=3.0),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=2.5),
        dict(src=f"{F}/proyector-ondas-ambar.jpg", dur=1.4),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=3.6, t1=5.0),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=2.5, t1=5.0),
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=2.0, t1=5.0, velocidad=0.8),
    ], textos=[("POV: pones esto antes de dormir", 0, 3.0, "gancho"),
               ("Azul para relajarte", 3.0, 5.5, "nota"), ("Ámbar para leer", 5.5, 6.9, "nota"),
               ("O el color que quieras", 6.9, 10.8, "nota"), ("¿De qué color lo pondrías?", 10.8, 15, "nota")]),

    # ---------- RELOJ ----------
    "t7-reloj-las-tres-de-la-manana": dict(voz=f"{T}/voz-t7-reloj.wav", segmentos=[
        dict(src=f"{E}/escena-3.jpg", dur=3.2, zoom="in", filtro="eq=brightness=-0.35:saturation=0.6"),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=3.0, ajustar=True),
        dict(src=f"{F}/reloj-3d-perfil.jpg", dur=2.6, zoom="out", ajustar=True),
        dict(src=f"{F}/reloj-3d-estante.jpg", dur=3.0, ajustar=True),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=3.8, zoom="out", ajustar=True),
    ], textos=[("¿TE PASA ESTO A LAS 3:00?", 0, 3.0, "gancho")]),

    "t8-reloj-setup": dict(voz=None, segmentos=[
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=2.0, ajustar=True),
        dict(src=f"{F}/reloj-3d-estante.jpg", dur=1.8, zoom="out", ajustar=True),
        dict(src=f"{F}/reloj-3d-perfil.jpg", dur=1.8, ajustar=True),
        dict(src=f"{F}/reloj-3d-estudio.jpg", dur=1.8, zoom="out", ajustar=True),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=2.4, ajustar=True),
    ], textos=[("El detalle que cambia una estantería", 0, 2.0, "gancho"),
               ("Números que flotan en la pared", 2.0, 5.6, "nota"),
               ("De pared o de mesa", 5.6, 7.4, "nota"),
               ("¿Pared o mesa?", 7.4, 9.8, "nota")]),

    # ---------- LOS 4 ----------
    "t9-cuatro-cosas-que-cambian-tu-cuarto": dict(voz=f"{T}/voz-t9-cuatro.wav", segmentos=[
        dict(src=f"{E}/escena-3.jpg", dur=2.6, filtro="eq=saturation=0.75"),
        dict(src=f"{M}/viral-lampara-se-enciende-9x16.mp4", t0=1.0, t1=4.0),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=3.0, ajustar=True),
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=3.0),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=2.4),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=1.0, t1=2.6),
    ], textos=[("4 COSAS QUE CAMBIAN TU CUARTO", 0, 2.4, "gancho")]),

    "t10-cual-te-llevas": dict(voz=None, segmentos=[
        dict(src=f"{M}/viral-mano-bola-9x16.mp4", t0=0, t1=1.8),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=1.8, ajustar=True),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=1.8),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=1.8),
        dict(src=f"{M}/viral-lampara-se-enciende-9x16.mp4", t0=1.2, t1=3.6),
    ], textos=[("Solo puedes quedarte con UNO", 0, 1.2, "gancho"),
               ("1 · Lámpara planeta", 1.2, 1.8, "nota"), ("2 · Reloj 3D", 1.8, 3.6, "nota"),
               ("3 · Proyector de olas", 3.6, 5.4, "nota"), ("4 · Globo que flota", 5.4, 7.2, "nota"),
               ("Comenta el número", 7.2, 9.6, "nota")]),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n in (sys.argv[1:] or VIDEOS):
        v = VIDEOS[n]
        montar(n, v["segmentos"], OUT, voz=v["voz"], textos=v["textos"], correcciones=ORB, desfase_voz=0.0)
