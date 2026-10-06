"""Carruseles de valor (consejos y temas de marca), 7 diapositivas de 1080x1350 cada uno.
Mismo estilo que generar_carrusel.py. Salida: contenido/carruseles/<nombre>/slide-N.jpg
Uso: python3 contenido/carruseles/generar_carruseles_valor.py"""
import os
from playwright.sync_api import sync_playwright
from generar_carrusel import CSS, CHROME, LOGO, STARS, ROOT, page

def f(p): return f"file://{ROOT}/{p}"

IMG = {
    "techo": f("tiktok/historias/material/c0-cuarto-antes.png"),
    "lampara_cuarto": f("tiktok/historias/material/c1-lampara.png"),
    "reloj_cuarto": f("tiktok/historias/material/c2-reloj.png"),
    "olas_cuarto": f("tiktok/historias/material/c3-proyector.png"),
    "final": f("tiktok/historias/material/c4-globo-final.png"),
    "movil": f("tiktok/historias/material/a1-movil-luz-techo.png"),
    "interruptor": f("tiktok/historias/material/a2-interruptor.png"),
    "calido": f("tiktok/historias/material/a3-cuarto-calido.png"),
    "regalos": f("tiktok/historias/material/b1-regalos-calcetines.png"),
    "caja": f("tiktok/historias/material/b2-caja-globo.png"),
    "mesilla": f("anuncios/meta/escenas/escena-1.jpg"),
    "saturno": f("fotos/lampara-saturno-noche.jpg"),
    "olas_techo": f("fotos/proyector-ondas-techo.jpg"),
    "proyector": f("fotos/proyector-ondas-noche.jpg"),
    "globo": f("fotos/globo-levita-noche.jpg"),
    "reloj": f("fotos/reloj-3d-noche.jpg"),
    "modelos": f("fotos/lampara-4-modelos.jpg"),
}

def fondo(img, pos="50% 50%", sombra="shade-top"):
    return f'<img class="bg" src="{IMG[img]}" style="object-position:{pos}"><div class="{sombra}"></div>'

def paso(img, tag, titulo, texto, pos="50% 50%", abajo=False):
    caja = "pad bot" if abajo else "pad top"
    return (fondo(img, pos, "shade-bot" if abajo else "shade-top") +
            f'<div class="{caja}"><span class="tag">{tag}</span><h2>{titulo}</h2><p>{texto}</p></div>')

def cierre(img, titulo, pasos):
    items = "".join(f"<div><b>{i}</b>{t}</div>" for i, t in enumerate(pasos, 1))
    return (f'<img class="bg" src="{IMG[img]}" style="object-position:50% 40%;opacity:.45"><div class="stars" style="opacity:.5"></div>'
            f'<div class="pad top" style="top:150px"><h1>{titulo}</h1><div class="cta">{items}</div></div>')

CARRUSELES = {
    # 1 · CONSEJOS DE LUZ
    "trucos-de-luz": [
        fondo("final", "50% 45%") +
        '<div class="pad top"><h1>5 trucos de luz que cambian un cuarto <span class="amb">sin obras.</span></h1>'
        '<p>Tu habitación no necesita más cosas. Necesita mejor luz.</p><div class="swipe">Desliza →</div></div>',
        paso("techo", "Truco 1", "Por la noche, <span class=\"amb\">apaga el techo.</span>",
             "La luz que cae desde arriba aplana todo y borra las sombras. Úsala para limpiar o buscar las llaves, no para estar.", "50% 40%"),
        paso("lampara_cuarto", "Truco 2", "Luz cálida, <span class=\"amb\">nunca blanca fría.</span>",
             "Mira la caja de la bombilla: busca 2700 K. Cuanto más bajo es ese número, más cálida y acogedora se ve la luz.", "50% 55%"),
        paso("reloj_cuarto", "Truco 3", "Varios puntos pequeños <span class=\"amb\">mejor que uno grande.</span>",
             "Uno en la mesilla, otro en la estantería, otro a ras de suelo. Luz a distintas alturas = un cuarto con profundidad.", "50% 55%"),
        paso("saturno", "Truco 4", "Un objeto <span class=\"amb\">que brille.</span>",
             "Los cuartos que te enamoran tienen algo que atrae la mirada. Si además da luz, hace dos trabajos a la vez.", "50% 50%", abajo=True),
        paso("calido", "Truco 5", "No te olvides <span class=\"amb\">del techo.</span>",
             "Es la superficie más grande del cuarto y casi nadie la usa. Sombras, reflejos o color ahí arriba lo cambian todo.", "50% 40%"),
        cierre("final", 'Esta noche, <span class="amb">prueba uno.</span>',
               ["Guárdalo para cuando cambies tu cuarto", "Mándaselo a quien vive con la luz del techo puesta",
                "Nuestras luces, en el enlace de la bio"]),
    ],
    # 2 · RUTINA PARA DESCONECTAR
    "rutina-de-noche": [
        fondo("movil", "50% 40%") +
        '<div class="pad top"><h1>¿Te acuestas y tu cabeza <span class="amb">sigue a mil?</span></h1>'
        '<p>Prueba esta rutina de 30 minutos antes de dormir.</p><div class="swipe">Desliza →</div></div>',
        paso("interruptor", "30 min antes", "Baja las luces.",
             "Apaga la luz grande y deja solo luz cálida y baja. Es la señal de que el día se acaba.", "50% 50%"),
        paso("techo", "25 min antes", "Deja listo el mañana.",
             "Ropa, mochila, lo que tengas que llevar. Una cosa menos dando vueltas en la cabeza.", "50% 45%"),
        paso("reloj", "20 min antes", "El móvil, <span class=\"amb\">fuera de la cama.</span>",
             "Ponlo a cargar lejos. Si lo usas para mirar la hora, cámbialo por un reloj que se vea desde la cama.", "50% 50%", abajo=True),
        paso("mesilla", "15 min antes", "Algo que no sea una pantalla.",
             "Leer unas páginas, estirar o apuntar tres cosas del día. Lo que te ayude a soltar.", "50% 65%"),
        paso("olas_cuarto", "5 min antes", "Crea tu ambiente.",
             "Luz tenue, olas en el techo o silencio total. No hay una fórmula: lo que te relaje a ti.", "50% 40%"),
        cierre("calido", 'Pruébala <span class="amb">esta semana.</span>',
               ["Guárdala para esta noche", "Cuéntanos qué paso te cuesta más", "Compártela con quien duerme con el móvil en la mano"]),
    ],
    # 3 · GUÍA DE REGALOS
    "guia-de-regalos": [
        fondo("caja", "50% 50%") +
        '<div class="pad top"><h1>Regalos que <span class="amb">no acaban en un cajón.</span></h1>'
        '<p>Guía rápida según a quién se lo regales.</p><div class="swipe">Desliza →</div></div>',
        paso("globo", "Para quien lo tiene todo", "Algo que no haya visto nunca.",
             "Un globo terráqueo que flota en el aire y gira solo. Nadie se queda indiferente.", "50% 45%", abajo=True),
        paso("proyector", "Para quien cuida su descanso", "Su cuarto, bajo el mar.",
             "Un proyector que llena el techo de olas que se mueven. Para apagar la luz y desconectar.", "50% 50%", abajo=True),
        paso("reloj", "Para quien estudia o trabaja en casa", "El detalle del escritorio.",
             "Un reloj 3D de pared o de mesa que se lee desde lejos. Útil todos los días.", "50% 50%", abajo=True),
        paso("modelos", "Para los soñadores", "Un planeta en la mesilla.",
             "Lámparas de cristal con Saturno, la Luna o una galaxia dentro. Perfecto para el amigo invisible.", "50% 40%", abajo=True),
        paso("regalos", "El truco para acertar", "Que se use <span class=\"amb\">y que se vea.</span>",
             "Los mejores regalos se usan a diario y están a la vista. Cada vez que se enciende, se acuerdan de ti.", "50% 45%"),
        cierre("final", 'Etiqueta a quien <span class="amb">le regalarías cada uno.</span>',
               ["Guárdalo para Navidad y cumpleaños", "Comparte la guía con quien siempre regala calcetines",
                "Los 4, en el enlace de la bio"]),
    ],
}

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for nombre, slides in CARRUSELES.items():
            out = f"{ROOT}/contenido/carruseles/{nombre}"; os.makedirs(out, exist_ok=True)
            for i, body in enumerate(slides, 1):
                tmp = f"{out}/.tmp.html"; open(tmp, "w").write(page(i, body))
                pg.goto(f"file://{tmp}"); pg.wait_for_timeout(600)
                pg.screenshot(path=f"{out}/slide-{i}.jpg", type="jpeg", quality=90); os.remove(tmp)
            print(nombre, len(slides))
        b.close()

if __name__ == "__main__":
    main()
