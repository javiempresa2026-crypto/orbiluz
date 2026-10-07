# Campaña de Meta · 3 anuncios con personas y formato viral

Son vídeos con aspecto de contenido normal: sin logo ni barra mientras se ven, y la marca solo en la tarjeta final. Cada uno tiene versión **9:16** (Reels e Historias) y **4:5** (`-4x5`, feed).

**Acabado nativo** (`tiktok/textos_ugc.py`):
- **Tipografía:** TikTok Sans (licencia OFL, en `marca/fuentes/ugc`).
- **Gancho:** cajas blancas redondeadas, como el texto de la app.
- **Notas:** caja amarilla.
- **Subtítulos:** palabras blancas con borde negro; la palabra que suena va sobre un recuadro amarillo que «salta».
- **Imagen:** grano de móvil, un ligero movimiento de cámara en mano y cortes secos, sin transiciones de edición.

**Medidas:** todos los textos están entre y = 300 e y = 1250 del 9:16. Así no los tapa la interfaz de Reels e Historias (unos 270 px arriba y 670 px abajo) y entran enteros en el recorte 4:5 (y = 220 a 1570).
Montaje: `python3 anuncios/meta/ugc/anuncios_ugc.py`.

**Las personas que aparecen son actores generados con IA.** Usan el producto, pero no hablan a cámara, no opinan y no se presentan como clientes. Nunca se debe poner un texto del tipo «lo compré y me encanta» sobre ellos: sería un testimonio falso. Si un día hay reseñas reales, se usan esas.

| | Archivo | Producto · destino | Ángulo | Gancho (primeros 2 s) | Duración |
|---|---|---|---|---|---|
| **U1** | `U1-pov-amigo-invisible` | Lámpara · ficha | Regalo, en primera persona (POV) | «POV: tu amigo invisible por fin acierta» | 13 s |
| **U2** | `U2-haz-esto-esta-noche` | Proyector · ficha | Problema → solución, con una persona | «Haz esto esta noche si no consigues desconectar» | 15 s |
| **U3** | `U3-imposible-no-tocarlo` | Globo · ficha | Curiosidad / satisfactorio | «Es imposible no tocarlo» | 12 s |

## Por qué cada gancho

- **U1 · POV unboxing.** En TikTok y Reels, «POV» y abrir un regalo son de los formatos más vistos. No lleva voz: se entiende sin sonido, que es como se ve la mayor parte del feed. Al final dice que la bola es mini (5 cm), para que nadie se lleve una sorpresa al recibirla y no haya devoluciones.
- **U2 · «Haz esto esta noche».** Da una instrucción concreta a quien tiene el problema: no desconecta por la noche. Se ve el antes (luz del techo y móvil) y el después (las olas en el techo) en la misma persona. Es la estructura problema → solución que mejor funciona con público frío. Voz de Marisol.
- **U3 · «Es imposible no tocarlo».** Un dedo empuja el globo, este se balancea y sigue flotando. Genera curiosidad («¿cómo flota?»), engancha y hace que se vea más de una vez. Es el producto con más margen (≈ 35 € por venta). Voz de Inés.

## Textos de cada anuncio

| | Texto principal | Titular | Descripción | Botón |
|---|---|---|---|---|
| U1 | «POV: abres el regalo y es un planeta. 🪐 Bola de cristal con Saturno, la Luna, una galaxia o el sistema solar grabado dentro, con luz cálida. Pídelo con tiempo para el amigo invisible.» | «El regalo que sí acierta» | Envío con seguimiento · 14 días para devolver | Comprar |
| U2 | «Si por la noche no desconectas, prueba esto: móvil fuera, luz del techo apagada y olas en el techo. 🌊 16 colores, mando a distancia y botón táctil.» | «Tu cuarto, bajo el mar» | Envío con seguimiento · 14 días para devolver | Comprar |
| U3 | «Lo tocas, se balancea… y sigue flotando. 🌍 Globo de 14 cm con levitación magnética, sin hilos ni soportes. Gira solo y se ilumina por dentro.» | «El mundo, flotando en tu escritorio» | Envío gratis con seguimiento · 14 días para devolver | Ver más |

## Cómo lanzarla

**Campaña «TEST · UGC · Ventas»** (objetivo: Ventas, evento: Compra). Un conjunto de anuncios **por producto**, porque cada uno tiene un precio y un margen distinto y Meta los optimiza mejor por separado:

| Conjunto | Anuncio | Presupuesto | CPA máximo para no perder |
|---|---|---|---|
| Lámpara | U1 (+ M3 y E3 si quieres comparar el mismo ángulo en otro formato) | 15 €/día | ≈ 11 € |
| Proyector | U2 (+ E4) | 10 €/día | ≈ 12 € |
| Globo | U3 | 10 €/día | ≈ 35 € |

- **Configuración:** España, 18-55 años, público amplio, ubicaciones Advantage+ y mejoras creativas automáticas **desactivadas**.
- **No tocar nada durante 72 horas.**
- **Día 3:** pausar el anuncio en el que menos de un 25 % de la gente vea los 3 primeros segundos y además tenga un CTR del enlace menor del 0,8 %.
- **Día 5-7:** el conjunto con CPA por debajo de su máximo sube un 20 % cada 2-3 días. Del anuncio ganador se hacen 2-3 variantes cambiando solo el gancho.

**Ganchos alternativos para esas variantes** (el mismo vídeo con otro texto al principio):

| | Variantes |
|---|---|
| U1 | «Lo que nadie espera encontrar en su amigo invisible» · «El regalo que se queda en la mesilla, no en el cajón» |
| U2 | «Tu techo esta noche:» · «Apaga la luz grande y mira lo que pasa» |
| U3 | «Todo el mundo hace lo mismo al verlo» · «¿Cómo flota esto?» |

## El anuncio que más puede funcionar: grabado por ti

Cuando te lleguen las primeras unidades, graba esto con el móvil, en vertical y con la luz de tu cuarto. Es real, da confianza y es justo lo que mejor funciona en este nicho.

1. **0-2 s · gancho, hablando a cámara:** «Os enseño lo que más me preguntan de la tienda.» (o «He montado una tienda de cosas que se encienden. Mirad esto.»)
2. **2-8 s:** apagas la luz del techo y enciendes el proyector. Que se vea el techo de verdad, sin efectos.
3. **8-12 s:** coges la lámpara, la giras delante de la cámara y la enciendes. Di que es pequeña: «Es mini, del tamaño de una pelota de golf.»
4. **12-15 s:** «Están en orbiluz.com, en la bio.»

Como eres el dueño de la tienda, hablar en primera persona es honesto. Monto el vídeo con subtítulos y música en cuanto me lo pases.

## Coste

**39,1 créditos** de Higgsfield. Saldo después: 40,3.

| Concepto | Créditos |
|---|---|
| 4 imágenes | 8 |
| 4 clips de Kling | 30 |
| 2 voces | ≈ 1,1 |
