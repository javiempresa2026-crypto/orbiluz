# Historias · 3 vídeos para que la gente se quede hasta el final

Tres formatos que funcionan muy bien en TikTok y Reels, con escenas nuevas y realistas (grabadas «con el móvil», en pisos normales).
Las voces hablan en segunda persona («tú»): son narradoras de la marca, no clientas, y no se dan datos ni testimonios inventados.

Montaje: `python3 tiktok/historias/historias.py` (usa el mismo motor que `tiktok/videos.py`).

| Vídeo | Formato | Voz | Música | Duración |
|---|---|---|---|---|
| `h1-lo-que-te-quita-el-sueno` | Problema → análisis → solución | Inés (grave, tono de explicación) | Lofi; el ritmo entra al apagar la luz | 24 s |
| `h2-el-regalo-que-se-graba` | Historia con giro | Marisol | House; la música se corta en «Silencio» y vuelve cuando todos sacan el móvil | 18 s |
| `h3-mismo-cuarto-otra-vida` | Transformación antes/después | Ainsley | Trap; el ritmo entra cuando aparece la primera luz | 20 s |
| `h4-se-encienden-uno-a-uno-v2` | Animación de producto | — | Ambiental; el ritmo entra al apagarse el techo | 10 s |

## 1 · Lo que te quita el sueño (y no es el móvil)

**Por qué engancha:** el gancho contradice lo que todo el mundo cree («no es el móvil»). Analiza el problema con 3 palabras en pantalla («Fuerte · Fría · Desde arriba»), da un consejo que se puede probar esa misma noche y termina con «Guárdalo», que dispara los guardados.

**Historia:** tumbado con el móvil y la luz del techo puesta → el cuarto frío con el fluorescente parpadeando → «para tu cuerpo, sigue siendo de día» → una mano apaga la luz → se enciende la lámpara → el cuarto con luz cálida y olas en el techo.

- **Descripción:** No es el móvil. Es la luz que tienes encima 💡 Pruébalo una semana y me cuentas. #dormirmejor #rutinadenoche #habitacionaesthetic #consejos #fyp
- **Comentario fijado:** «¿Cuántos tenéis la luz del techo puesta ahora mismo? 👀»

## 2 · El regalo que dejó a todos callados

**Por qué engancha:** todo el mundo ha vivido lo de abrir calcetines y sonreír por compromiso. El silencio de verdad (la música se corta) crea tensión, y la recompensa llega a la vez: el globo sale flotando de la caja y todos sacan el móvil para grabarlo. Encaja con la temporada de regalos de Navidad.

**Historia:** calcetines, otra vela, una taza → «hasta que llega la última caja» → el globo sale de la caja y empieza a flotar → silencio → todos lo graban.

- **Descripción:** Este año, que lo graben 🎁 ¿A quién se lo regalarías? #ideasderegalo #regalosoriginales #amigoinvisible #navidad #fyp
- **Comentario fijado:** «Etiqueta a quien siempre regala calcetines 🧦»

## 3 · Mismo cuarto. Otra vida.

**Por qué engancha:** las transformaciones son de lo que más se ve en TikTok. En el segundo 5 se enseña un adelanto del resultado final para que la gente quiera ver cómo se llega. Después, el mismo cuarto va cambiando paso a paso con un contador (1/4, 2/4…), y la pregunta del final genera comentarios.

**Historia:** cuarto de piso de estudiantes con fluorescente parpadeando → adelanto del final → se apaga el techo → lámpara → reloj → olas en el techo → globo.

- **Descripción:** De sala de espera a esto, con 4 cosas ✨ #roommakeover #antesydespues #decoracionhabitacion #habitacionaesthetic #fyp
- **Comentario fijado:** «¿Cuál pondrías tú primero? 1 lámpara, 2 reloj, 3 olas, 4 globo»

## 4 · Apaga el techo y mira (animación)

**Por qué engancha:** es corto (10 s), muy visual y se repite solo. En un mismo plano, sin cortes, los 4 productos se encienden uno a uno: lámpara, reloj, olas que se extienden por el techo y el globo que se levanta con destellos dorados.

Se ha hecho con un clip de Kling 3.0 que va de la foto «solo la lámpara» a la foto final (`animacion.py`). Kling deformaba los minutos del reloj (salía «97»), así que en `d1-se-encienden-corregido.mp4` se pegan encima, fotograma a fotograma, los minutos reales de la foto final.

- **Descripción:** Apaga el techo y deja que se enciendan solos ✨ #roommakeover #habitacionaesthetic #luzambiente #decoracion #fyp
- **Comentario fijado:** «¿Cuál encenderías primero? 1, 2, 3 o 4»

## Cómo publicarlos

- Uno cada dos días, entre las 20:00 y las 22:30. Empieza por el 3 (el más visual), luego el 1 y deja el 2 para noviembre (regalos de Navidad).
- Añade un sonido en tendencia desde la app al 5-10 %.
- Los tres sirven también como anuncio en Meta: si alguno funciona bien en orgánico, conviértelo en anuncio.

## Material (`material/`)

- **Fotogramas generados con Nano Banana 2:** las escenas y la transformación del cuarto. Los pasos `c1`-`c4` son ediciones sucesivas de `c0`, con las fotos reales de los productos como referencia.
- **Clips animados con Kling 3.0:** 5 s cada uno.
- **Voces:** `voz-bruta-*` son las originales; `voz-h*` son las ya ajustadas con `preparar_voz.py`.

## Coste

**83,4 créditos** de Higgsfield: 75,9 de los tres primeros vídeos y 7,5 de la animación. Saldo después: 80,9.

| Concepto | Créditos |
|---|---|
| 11 imágenes | 22 |
| 7 clips de Kling | 52,5 |
| 3 voces | ≈ 1,5 |

El clip animado del cuarto final no se usa: deformaba los números del reloj. En su lugar va la foto con movimiento de cámara.
