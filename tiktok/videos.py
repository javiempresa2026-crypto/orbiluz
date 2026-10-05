"""Guiones de los TikTok de Orbiluz. Uso: python3 tiktok/videos.py [nombre ...]
Cada vídeo tiene su voz, su música y su juego de transiciones, para que no se parezcan entre sí.
Voces: Ainsley (mujer, la que eligió Javier), Marisol (mujer) e Inés (voz grave de hombre)."""
import os, sys
from motor import montar, ROOT

M = f"{ROOT}/contenido/material"     # clips ya generados
T = f"{ROOT}/tiktok/material"        # clips y voces de esta tanda
F = f"{ROOT}/fotos"
E = f"{ROOT}/anuncios/meta/escenas"
OUT = f"{ROOT}/tiktok/videos"
ORB = {"orbiluz": "ORBILÚZ"}  # Whisper escribe la marca de varias formas
OSCURO = "eq=brightness=-0.3:saturation=0.6"

VIDEOS = {
    # ---------- LÁMPARA ----------
    # Voz Ainsley · lofi · el ritmo entra justo cuando se enciende la lámpara (4,2 s)
    "t1-lampara-apaga-el-techo": dict(voz=f"{T}/voz3-t1-lampara.wav", musica="lofi", drop=4.2,
        transiciones=["desenfoque", "flash", "fundido", "barrido-v", "corte", "corte", "corte", "circulo"], segmentos=[
        dict(src=f"{E}/escena-3.jpg", dur=2.4, mov="in", filtro="eq=saturation=0.75"),
        dict(src=f"{E}/escena-3.jpg", dur=1.8, mov="der", filtro=OSCURO),
        dict(src=f"{M}/viral-lampara-se-enciende-9x16.mp4", t0=1.4, t1=3.6),
        dict(src=f"{M}/viral-mano-bola-9x16.mp4", t0=0, t1=2.2),
        dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=1.5),
        dict(src=f"{F}/lampara-saturno-noche.jpg", dur=0.8, mov="in"),
        dict(src=f"{F}/lampara-luna-noche.jpg", dur=0.9, mov="out"),
        dict(src=f"{F}/lampara-galaxia-noche.jpg", dur=1.0, mov="in"),
        dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=1.4, t1=4.0),
    ], textos=[("HAZ ESTO ESTA NOCHE", 0, 2.4, "gancho")]),

    # Sin voz · house · cortes al compás
    "t2-lampara-cual-eliges": dict(voz=None, musica="house",
        transiciones=["flash", "deslizar", "deslizar", "deslizar", "zoom"], segmentos=[
        dict(src=f"{M}/viral-mano-bola-9x16.mp4", t0=0, t1=2.2),
        dict(src=f"{F}/lampara-saturno-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-luna-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-galaxia-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-sistema-solar-noche.jpg", dur=1.6),
        dict(src=f"{F}/lampara-4-modelos.jpg", dur=2.4, mov="out", ajustar=True),
    ], textos=[("ELIGE TU PLANETA", 0, 2.1, "gancho"),
               ("1 · Saturno", 2.2, 3.8, "nota"), ("2 · La Luna", 3.8, 5.4, "nota"),
               ("3 · Galaxia", 5.4, 7.0, "nota"), ("4 · Sistema solar", 7.0, 8.6, "nota"),
               ("Comenta tu número", 8.6, 11, "nota")]),

    # ---------- GLOBO ----------
    # Voz Marisol · ambiental · transiciones suaves y circulares (encaja con algo que gira y flota)
    "t3-globo-explicame-esto": dict(voz=f"{T}/voz-t3-globo.wav", musica="sueño",
        transiciones=["radial", "desenfoque", "circulo", "fundido", "radial"], segmentos=[
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=3.0),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=0, t1=3.0, velocidad=0.8),
        dict(src=f"{F}/globo-levita-noche.jpg", dur=2.4, mov="sube"),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=2.0, t1=5.0, velocidad=0.8),
        dict(src=f"{F}/globo-levita-escritorio.jpg", dur=2.2, mov="out"),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=2.0, t1=5.0),
    ], textos=[("¿CÓMO FLOTA ESTO?", 0, 2.6, "gancho")]),

    # Sin voz · lofi · cortes al compás
    "t4-globo-escritorio": dict(voz=None, musica="lofi",
        transiciones=["corte", "barrido", "cortina", "negro"], segmentos=[
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=0, t1=2.5),
        dict(src=f"{F}/globo-levita-ambiente.jpg", dur=1.8, mov="izq"),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0.5, t1=3.5, velocidad=0.7),
        dict(src=f"{F}/globo-levita-estudio.jpg", dur=1.6, mov="out"),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=2.5, t1=5.0, velocidad=0.8),
    ], textos=[("Lo que todo el mundo pregunta al entrar a mi despacho", 0, 2.6, "gancho"),
               ("No tiene hilos.", 2.7, 4.6, "nota"), ("Flota y gira solo.", 4.6, 8.8, "nota"),
               ("¿Lo pondrías en tu escritorio?", 8.8, 13, "nota")]),

    # ---------- PROYECTOR ----------
    # Voz Ainsley · ambiental · el ritmo entra con «Y de repente» (2,8 s)
    "t5-proyector-fondo-del-mar": dict(voz=f"{T}/voz3-t5-proyector.wav", musica="sueño", drop=2.8,
        transiciones=["corte", "circulo", "desenfoque", "radial"], segmentos=[
        dict(src=f"{F}/proyector-ondas-noche.jpg", dur=1.4, mov="in"),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=1.4),
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=3.8),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=1.5, t1=4.0),
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=2.7, t1=5.0),
    ], textos=[("TU CUARTO, BAJO EL MAR", 0, 2.0, "gancho")]),

    # Sin voz · trap · cortes al compás
    "t6-proyector-colores": dict(voz=None, musica="trap",
        transiciones=["flash", "pixel", "corte", "aplastar", "subir"], segmentos=[
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=3.0),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=2.5),
        dict(src=f"{F}/proyector-ondas-ambar.jpg", dur=1.4, mov="der"),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=3.6, t1=5.0),
        dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=2.5, t1=5.0),
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=2.0, t1=5.0, velocidad=0.8),
    ], textos=[("POV: pones esto antes de dormir", 0, 3.0, "gancho"),
               ("Azul para relajarte", 3.0, 5.5, "nota"), ("Ámbar para leer", 5.5, 6.9, "nota"),
               ("O el color que quieras", 6.9, 10.8, "nota"), ("¿De qué color lo pondrías?", 10.8, 15, "nota")]),

    # ---------- RELOJ ----------
    # Voz Inés (grave) · trap · el reloj desenfocado = «no sabes qué hora es»; el ritmo entra con «o pones esto» (6,2 s)
    "t7-reloj-las-tres-de-la-manana": dict(voz=f"{T}/voz3-t7-reloj.wav", musica="trap", drop=6.2,
        transiciones=["desenfoque", "negro", "flash", "corte", "deslizar", "zoom"], segmentos=[
        dict(src=f"{E}/escena-3.jpg", dur=2.0, mov="in", filtro=OSCURO),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=1.7, mov="izq", ajustar=True, filtro="gblur=sigma=28,eq=brightness=-0.2"),
        dict(src=f"{E}/escena-3.jpg", dur=2.5, mov="out", filtro="eq=brightness=-0.4:saturation=0.5"),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=1.9, mov="in", ajustar=True),
        dict(src=f"{F}/reloj-3d-perfil.jpg", dur=1.1, mov="der", ajustar=True),
        dict(src=f"{F}/reloj-3d-estante.jpg", dur=1.2, mov="sube", ajustar=True),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=1.4, mov="out", ajustar=True),
    ], textos=[("¿TE PASA ESTO A LAS 3:00?", 0, 3.0, "gancho")]),

    # Sin voz · house · cortes al compás
    "t8-reloj-setup": dict(voz=None, musica="house",
        transiciones=["corte", "aplastar", "corte", "cortina"], segmentos=[
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=2.0, ajustar=True),
        dict(src=f"{F}/reloj-3d-estante.jpg", dur=1.8, ajustar=True),
        dict(src=f"{F}/reloj-3d-perfil.jpg", dur=1.8, ajustar=True),
        dict(src=f"{F}/reloj-3d-estudio.jpg", dur=1.8, ajustar=True),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=2.4, mov="out", ajustar=True),
    ], textos=[("El detalle que cambia una estantería", 0, 2.0, "gancho"),
               ("Números que flotan en la pared", 2.0, 5.6, "nota"),
               ("De pared o de mesa", 5.6, 7.4, "nota"),
               ("¿Pared o mesa?", 7.4, 9.8, "nota")]),

    # ---------- LOS 4 ----------
    # Voz Ainsley · house · cada producto entra justo cuando la voz dice su número
    "t9-cuatro-cosas-que-cambian-tu-cuarto": dict(voz=f"{T}/voz3-t9-cuatro.wav", musica="house", drop=2.9,
        transiciones=["flash", "deslizar", "subir", "deslizar", "barrido"], segmentos=[
        dict(src=f"{E}/escena-3.jpg", dur=2.9, mov="in", filtro="eq=saturation=0.75"),
        dict(src=f"{M}/viral-lampara-se-enciende-9x16.mp4", t0=1.0, t1=3.2),
        dict(src=f"{F}/reloj-3d-noche.jpg", dur=2.6, mov="der", ajustar=True),
        dict(src=f"{T}/proyector-cuarto-9x16.mp4", t0=0, t1=2.9),
        dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=2.4),
        dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=1.0, t1=3.0),
    ], textos=[("4 COSAS QUE CAMBIAN TU CUARTO", 0, 2.4, "gancho")]),

    # Sin voz · trap a 133 bpm: cada producto dura exactamente 4 tiempos
    "t10-cual-te-llevas": dict(voz=None, musica="trap", tempo=133.33,
        transiciones=["flash", "corte", "corte", "corte"], segmentos=[
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
        v = dict(VIDEOS[n]); segs = v.pop("segmentos")
        montar(n, segs, OUT, correcciones=ORB, **v)
