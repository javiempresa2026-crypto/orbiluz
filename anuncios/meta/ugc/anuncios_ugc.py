"""3 anuncios para Meta con formato de vídeo nativo (sin logo ni barra durante el vídeo; la marca va en la tarjeta final).
U1 · POV unboxing de la lámpara (sin voz, texto estilo Instagram).
U2 · «Haz esto esta noche»: una chica pasa de la luz del techo a las olas del proyector (voz de Marisol).
U3 · «Es imposible no tocarlo»: el globo que levita (voz de Inés).
Las personas que aparecen son actores generados con IA: usan el producto, pero no opinan ni se presentan como clientes.
Uso: python3 anuncios/meta/ugc/anuncios_ugc.py [U1 U2 U3]"""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tiktok"))
from motor import montar, tarjeta_final, ROOT

U = f"{ROOT}/anuncios/meta/ugc/material"
M = f"{ROOT}/contenido/material"
T = f"{ROOT}/tiktok/material"
F = f"{ROOT}/fotos"
OUT = f"{ROOT}/anuncios/meta/ugc"


def anuncios(tmp):
    fin_lampara = tarjeta_final(f"{tmp}/fin-lampara.jpg", frase="Elige el suyo", fondo=f"{F}/lampara-saturno-noche.jpg")
    fin_proyector = tarjeta_final(f"{tmp}/fin-proyector.jpg", frase="Tu cuarto, bajo el mar", fondo=f"{F}/proyector-ondas-noche.jpg")
    fin_globo = tarjeta_final(f"{tmp}/fin-globo.jpg", frase="El mundo, flotando en tu escritorio", fondo=f"{F}/globo-levita-noche.jpg")
    nativo = dict(logo=False, barra=False)
    return {
        # U1 · POV UNBOXING · gancho de regalo · sin voz
        "U1-pov-amigo-invisible": dict(**nativo, voz=None, musica="house", drop=5.0, compas=False, estilo_texto="ig",
            transiciones=["corte", "corte", "deslizar", "negro"], segmentos=[
                dict(src=f"{U}/u1-unboxing.mp4", t0=0, t1=5.0),
                dict(src=f"{M}/viral-mano-coge-y-enciende-9x16.mp4", t0=2.2, t1=4.3),
                dict(src=f"{F}/lampara-4-modelos.jpg", dur=1.8, mov="in", ajustar=True),
                dict(src=f"{M}/lampara-saturno-mesilla-9x16.mp4", t0=0, t1=2.2),
                dict(src=fin_lampara, dur=2.0, mov="in"),
            ],
            textos=[("POV: tu amigo invisible por fin acierta", 0, 2.6, "gancho"),
                    ("Una bola de cristal con Saturno dentro", 2.7, 5.0, "nota"),
                    ("Se enciende con luz cálida", 5.0, 7.1, "nota"),
                    ("Saturno, Luna, Galaxia o Sistema solar", 7.1, 8.9, "nota"),
                    ("Es mini (5 cm): cabe en cualquier mesilla", 8.9, 11.1, "nota")],
            correcciones={}),

        # U2 · «HAZ ESTO ESTA NOCHE» · problema → solución con persona en escena
        "U2-haz-esto-esta-noche": dict(**nativo, voz=f"{U}/voz-u2-desconectar.wav", musica="sueño", drop=6.7,
            transiciones=["corte", "corte", "desenfoque", "corte", "negro"], segmentos=[
                dict(src=f"{U}/u2-chica-luz-techo.png", dur=2.7, mov="in"),
                dict(src=f"{U}/u2-transicion.mp4", t0=0, t1=5.0),
                dict(src=f"{U}/u2-olas.mp4", t0=0, t1=1.9),
                dict(src=f"{T}/proyector-cerca-9x16.mp4", t0=0, t1=2.0),
                dict(src=f"{U}/u2-olas.mp4", t0=2.0, t1=3.4),
                dict(src=fin_proyector, dur=2.0, mov="in"),
            ],
            textos=[("HAZ ESTO ESTA NOCHE SI NO CONSIGUES DESCONECTAR", 0, 2.6, "gancho")],
            correcciones={}),

        # U3 · «ES IMPOSIBLE NO TOCARLO» · curiosidad con el globo
        "U3-imposible-no-tocarlo": dict(**nativo, voz=f"{U}/voz-u3-globo.wav", musica="trap", drop=1.9,
            transiciones=["corte", "corte", "negro"], segmentos=[
                dict(src=f"{U}/u3-dedo-globo.mp4", t0=0, t1=5.0),
                dict(src=f"{M}/viral-globo-despacho-9x16.mp4", t0=0, t1=2.5),
                dict(src=f"{M}/globo-flotando-escritorio-9x16.mp4", t0=1.0, t1=3.8),
                dict(src=fin_globo, dur=2.0, mov="in"),
            ],
            textos=[("ES IMPOSIBLE NO TOCARLO", 0, 1.8, "gancho"),
                    ("Sin hilos ni soportes", 5.0, 7.5, "nota"),
                    ("Globo de 14 cm · mapa en inglés", 7.5, 10.3, "nota")],
            correcciones={"habitación": "levitación", "tu": "¿Tú"}),
    }


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        pedidos = sys.argv[1:]
        for n, v in anuncios(tmp).items():
            if pedidos and not any(n.startswith(p) for p in pedidos): continue
            v = dict(v); segs = v.pop("segmentos")
            montar(n, segs, OUT, formato_4x5=True, **v)
