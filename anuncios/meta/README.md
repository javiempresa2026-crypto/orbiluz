# Orbiluz: creatividades estáticas para Meta Ads (ciclo 3)

**Normas:**
- Sin precios ni ofertas: el enlace lo pone el usuario.
- Los anuncios presentan el producto, crean la necesidad y resuelven un problema.
- Solo aparecen manos, nunca personas presentadas como clientes. Nada de reseñas inventadas.

**Cómo se han hecho:**
- La escena fotorrealista la ha generado **Nano Banana 2** (en Higgsfield) usando la **foto real del producto** como referencia: 2 créditos por imagen.
- Los titulares se han compuesto con la tipografía de la marca (Unbounded y DM Sans) en `make_ads.py`.

## Investigación: qué funciona en Meta con estos productos

- **El regalo como gancho número 1** («un regalo que de verdad sorprenda»).
- **El brillo en la oscuridad** como efecto «wow», con estética de galaxia o universo.
- **Una mano sujetando el producto:** da la escala real y lo hace tangible.
- **Antes y después** en pantalla partida.
- **Variantes** («¿cuál es el tuyo?»), ideal para el carrusel.
- **Titulares de beneficio grandes**, legibles sin sonido.

**Limitación:** la Biblioteca de Anuncios de Meta no se puede consultar de forma automática (devuelve 403). Conviene revisarla a mano buscando «lámpara bola de cristal», «crystal ball lamp» y «globo levitación», y quedarse con los anuncios que lleven **más de 30 días activos**, que suelen ser los rentables.

## Anuncios (cada uno en `-4x5.jpg` para el feed y `-9x16.jpg` para Historias y Reels)

| # | Archivo | Producto | Ángulo | Texto principal (sin precios) | Titular |
|---|---|---|---|---|---|
| A1 | A1-regalo-mano | Lámpara | Regalo con efecto «wow» | «¿Buscas un regalo que de verdad sorprenda? Una bola de cristal con un planeta grabado por láser que se ilumina con luz cálida. De las que no acaban en un cajón.» | El regalo que sí sorprende |
| A2 | A2-apaga-la-luz | Lámpara | Ambiente de noche | «Apaga la luz del techo y deja que un planeta ilumine tu habitación. Luz cálida y suave, perfecta para desconectar antes de dormir.» | Enciende un planeta |
| A3 | A3-quien-lo-tiene-todo | Lámpara | Regalo de temporada (Navidad y Reyes) | «Para esa persona que ya lo tiene todo: un planeta grabado dentro del cristal que se ilumina en su mesilla. Original, bonito y con historia.» | Para quien ya lo tiene todo |
| A4 | A4-antes-despues | Lámpara | Problema → solución | «La luz del techo por la noche es fría y demasiado fuerte. Cámbiala por una luz cálida que además decora: tu dormitorio, con otro ambiente.» | Tu dormitorio, por la noche |
| A5 | A5-como-flota | Globo | Curiosidad | «Flota, gira y se ilumina. Un globo terráqueo que levita sobre su base gracias a la levitación magnética. La pieza que todo el mundo pregunta cuando entra en tu despacho.» | ¿Cómo está flotando? |
| A6 | A6-cual-es-el-tuyo | Lámpara | Elección y comentarios | «Saturno, la Luna, una galaxia o el sistema solar. ¿Cuál pondrías en tu mesilla?» | ¿Cuál es el tuyo? |

- **Descripción para todos:** «Orbiluz · decoración que se enciende».
- **CTA:** Comprar (o Más información en frío).

## Estructura de test recomendada

- **Campaña de lámpara (ventas):** 1 conjunto Advantage+ con España, 18-50 años y ubicaciones Advantage+. Presupuesto de 15 €/día.
  - Anuncios: **A1, A2, A3 y A4**, cada uno con su 4:5 y 9:16 por ubicación.
  - Aviso: A3 es de ambiente navideño; mejor lanzarlo a partir de noviembre.
- **A6** como **carrusel** o para retargeting (quien visitó la ficha).
- **Globo (A5):** en campaña aparte y con más presupuesto por venta, porque necesita un ROAS de ~3,8 para no perder dinero.
- **Decisión a los 4-5 días:**
  - El ganador se mide por **CPA**, no por clics.
  - Apagar lo que gaste 1,5 veces el CPA objetivo sin compras.
  - Del ganador, 2 variantes de titular: coste 0, se recompone con `make_ads.py`.

## Coste de este ciclo

6 escenas × 2 créditos = **12 créditos**. La escena 5 («mano bajo el globo») se descartó porque la mano parecía sujetarlo y el anuncio podía leerse como engañoso.
