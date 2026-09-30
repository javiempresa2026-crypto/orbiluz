# Vídeos virales · TikTok e Instagram Reels

6 vídeos verticales (1080×1920, 8-10 s, en bucle). Solo el producto y un texto que crea la necesidad.
Sin voz, sin precios y sin características. **Se suben sin audio: añade un sonido en tendencia desde la propia app**
(en TikTok e Instagram la música de la biblioteca es la que ayuda al alcance; no la metemos en el archivo por derechos).

Montaje: `python3 contenido/virales/montar_virales.py` (usa los clips de `contenido/material/`).

| Vídeo | Producto | Texto en pantalla | Ángulo |
|---|---|---|---|
| `v1-pov-luz-del-techo.mp4` | Lámpara Saturno | «POV: por fin quitaste la luz del techo» → «y tu cuarto cambió por completo» | Ambiente / antes-después |
| `v2-regalo-que-sorprende.mp4` | Lámpara Saturno | «Cuando encuentras el regalo que de verdad sorprende» | Regalo |
| `v3-no-regalo-otra-taza.mp4` | Lámpara Saturno | «Este año no regalo otra taza» → «regalo esto» | Regalo / Navidad |
| `v4-nadie-sabe-como-funciona.mp4` | Globo que levita | «Nadie en mi casa sabe cómo funciona esto» → «y nadie deja de mirarlo» | Curiosidad |
| `v5-mi-cuarto-a-las-23.mp4` | Lámpara Saturno | «Mi parte favorita del día: apagar la luz grande» | Rutina / calma |
| `v6-lo-pongo-y-todos-preguntan.mp4` | Globo que levita | «Lo puse en el escritorio y ahora todos preguntan» → «¿y esto cómo flota?» | Curiosidad / escritorio |

## Descripciones para publicar

Cortas, en tono de persona y sin precio. El enlace va en la bio.

- **V1**: Nunca más luz del techo por la noche 🌙 #decoracionhabitacion #habitacionaesthetic #lamparadenoche #roomtour #hogar
- **V2**: El regalo que nadie se espera ✨ #ideasderegalo #regalosoriginales #regaloperfecto #aesthetic #fyp
- **V3**: Este año cambio la taza por esto 🎁 #regalosnavidad #amigoinvisible #ideasderegalo #navidad2026 #regalosoriginales
- **V4**: Todavía no me lo explico 🌍 #globoflotante #setupescritorio #gadgets #decoracion #fyp
- **V5**: La mejor hora del día 🪐 #rutinadenoche #habitacionaesthetic #cozy #lamparadenoche #hogar
- **V6**: Todas las visitas preguntan lo mismo 🌍 #desksetup #setupescritorio #decoracionoficina #gadgets #curiosidades

Deja el primer comentario tú, fijado: «¿Os lo explico o es más bonito sin saberlo? 👀» (V4, V6) o «¿Para quién lo pillarías?» (V2, V3). Los comentarios dan alcance.

## Cómo publicarlos

1. **Frecuencia**: 1 vídeo al día, alternando lámpara y globo. Publica el mismo vídeo en TikTok y en Reels, con 1-2 h de diferencia.
2. **Hora**: de 20:00 a 22:30 (hora peninsular). El producto se ve mejor de noche y es cuando más se usa el móvil.
3. **Portada**: el fotograma con el producto encendido y el texto visible.
4. **A los 3 días**: mira la retención y cuántas veces se ven de principio a fin. El que más retenga se convierte en anuncio de Meta (el texto ya está fuera de la zona de la interfaz) y se vuelve a publicar con otro gancho en el mismo clip.
5. **Qué no poner**: precios, «oferta», «compra ya» ni la lista de características. En orgánico, que te pregunten; el enlace va en la bio.

## Siguientes variantes (gasto 0)

Con los mismos clips cambiando solo el texto del principio:

- «Cosas que no sabía que necesitaba hasta tenerlas»
- «Mi pareja pensaba que era una tontería hasta que lo encendí»
- «El regalo que siempre acaba en el salón de otra persona»
- «Esto es lo último que veo antes de dormir»

Se añaden en `VIDEOS` dentro de `montar_virales.py`.

## Coste

Generación de esta tanda en Higgsfield:

| Concepto | Créditos |
|---|---|
| 5 escenas con Nano Banana 2 | 10 |
| 4 clips con Kling 3.0 (5 s std, sin sonido) | 30 |
| **Total** | **40** |

V5 y V6 reutilizan clips que ya estaban generados.

## V7 · Problema → solución (18 s)

`v7-problema-luz-del-techo.mp4` se monta con `python3 contenido/virales/montar_problema_solucion.py`. Reutiliza material ya generado, así que no gasta créditos.

| Segundos | Imagen | Texto |
|---|---|---|
| 0-2,8 | Cuarto frío con luz de techo | «Si tu cuarto de noche parece una sala de espera…» |
| 2,8-5 | Mismo cuarto | «…no es la decoración. Es la luz del techo.» |
| 5-10 | Se apaga y se enciende la lámpara | «Apágala. Y enciende esto.» |
| 10-15 | Una mano la coge y la enciende | «Un solo punto de luz y tu cuarto cambia por completo» |
| 15-18 | Cierre | orbiluz · Decoración que se enciende |

**Descripción:** La luz del techo es para buscar las llaves, no para vivir tu habitación 🌙 ¿Equipo techo o equipo lámpara? #decoracionhabitacion #habitacionaesthetic #lamparadenoche #hogaracogedor #roominspo #fyp

**Sonido:** una canción tranquila en tendencia que cambie de ritmo hacia el segundo 5, cuando se enciende la lámpara.
