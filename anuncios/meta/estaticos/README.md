# Anuncios de imagen para Meta

5 anuncios de imagen fija. Cada uno tiene versión **4:5** (feed) y **9:16** (Historias y Reels; el contenido queda dentro de la zona que no tapa la interfaz).
Las ventajas que aparecen salen de la ficha real de cada producto. No llevan precios.
Se generan con `python3 anuncios/meta/estaticos/generar_estaticos.py`.

| Archivo | Formato | Producto · destino | Por qué puede funcionar |
|---|---|---|---|
| `E1-sala-de-espera` | Problema explicado → solución | Lámpara · ficha | Explica el problema con 3 señalizaciones sobre la foto y da la solución en una línea. Funciona con quien no te conoce. |
| `E2-techo-vs-lampara` | Comparativa (nosotros contra la alternativa) | Lámpara · ficha | Las comparativas en imagen fija son de los anuncios estáticos que más convierten. Compara con la luz del techo, no con otra marca. Dice que la bola mide 5 cm para que nadie se lleve una sorpresa. |
| `E3-regalo-de-siempre` | Comparativa con humor | Lámpara · ficha | El ángulo de amigo invisible en imagen: barato de producir y muy compartible. Va con M3 (vídeo). |
| `E4-proyector-ventajas` | Ventajas señaladas sobre la foto | Proyector · ficha | Ventajas reales de la ficha: ondas en movimiento, 16 colores con mando, botón táctil y USB. |
| `E5-antes-despues` | Antes / después | Los 4 · portada | El mismo cuarto antes y después. Se entiende en un segundo. |

## Textos

| | Texto principal | Titular | Botón |
|---|---|---|---|
| E1 | «La luz del techo aplana todo y por la noche es fría. Apágala y deja una luz baja y cálida en la mesilla: el cuarto cambia por completo. 🌙» | «Luz cálida para tu mesilla» | Comprar |
| E2 | «De noche, la luz del techo es para buscar las llaves. Para estar, luz cálida a la altura de la mesilla: una bola de cristal con un planeta grabado dentro. ✨» | «Un planeta en tu mesilla» | Comprar |
| E3 | «Este año, ni calcetines ni otra vela. 🎁 Una bola de cristal con Saturno, la Luna, una galaxia o el sistema solar dentro. Pídelo con tiempo.» | «El regalo que no acaba en un cajón» | Comprar |
| E4 | «Apaga la luz y llena el techo de olas que se mueven. 16 colores, mando a distancia y botón táctil. 🌊» | «Tu cuarto, bajo el mar» | Comprar |
| E5 | «Mismo cuarto, 4 cosas: lámpara planeta, reloj 3D, proyector de olas y globo que levita. ✨» | «Decoración que se enciende» | Ver más |

Descripción para todos: «Envío con seguimiento · 14 días para devolver».

## Cómo combinarlos con los vídeos

Con 100-150 € de prueba no conviene repartir entre 8 anuncios: ninguno recibiría gasto suficiente.

- **Ronda 1 (lámpara):** un conjunto amplio con **M1, M3, E2 y E3**. Son dos vídeos y dos imágenes, con los ángulos «problema» y «regalo». 20-25 €/día durante 5 días. Las reglas para decidir son las de `../video/README.md`.
- **Ronda 2:** el ganador de la ronda 1 frente a **M2 y E5**, que llevan a la portada (los 4 productos).
- **Proyector:** cuando la lámpara sea rentable, una campaña aparte con E4 hacia su ficha.
