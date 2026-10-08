# Campaña «Cinemática» · Meta

Es el enfoque contrario a los anuncios de estilo nativo (UGC): planos de producto tipo anuncio de marca, con macro, cámara lenta y luz dramática, y títulos de tráiler. Sirve para que Meta compare **lo premium frente a lo cercano** y quedarse con lo que mejor venda.

- **Vídeos:** `python3 anuncios/meta/cine/campana_cine.py` (9:16 y `-4x5`).
- **Imágenes:** `python3 anuncios/meta/cine/generar_imagenes_cine.py` (`-4x5` y `-9x16`).
- Todos los textos están dentro de las zonas seguras. No llevan precios.

## Vídeos (10-11 s, sin voz, con música propia)

| | Archivo | Gancho | Producto · destino |
|---|---|---|---|
| CI1 | `CI1-grabado-dentro-del-cristal` | «Esto está grabado / dentro del cristal.» | Lámpara · ficha |
| CI2 | `CI2-tu-techo-puede-hacer-esto` | «Tu techo / puede hacer esto.» | Proyector · ficha |
| CI3 | `CI3-flota-gira-brilla` | «Flota. / Gira. / Brilla.» | Globo · ficha |
| CI4 | `CI4-cuatro-luces` | «4 luces que cambian / un cuarto de noche.» | Los 4 · portada |

## Imágenes (4:5 y 9:16)

| | Archivo | Titular |
|---|---|---|
| I1 | `I1-grabado-dentro` | Grabado **dentro** del cristal. |
| I2 | `I2-tu-techo` | Tu techo **puede hacer esto.** |
| I3 | `I3-flota-gira-brilla` | Flota. Gira. **Brilla.** |
| I4 | `I4-cambia-la-luz` | Deja de comprar cojines. **Cambia la luz.** |

## Banco de ganchos nuevos

Para hacer variantes del anuncio que gane (mismo vídeo o imagen, otro texto al principio):

| Ángulo | Ganchos |
|---|---|
| Curiosidad | «Esto está grabado dentro del cristal» · «Sin hilos. Sin trucos. Sin explicación.» · «¿Cómo flota esto?» |
| Demostración | «Tu techo puede hacer esto» · «Lo enciendes y el techo se mueve» · «Flota. Gira. Brilla.» |
| Llevar la contraria | «Deja de comprar cojines. Cambia la luz.» · «No te falta decoración, te sobra luz de techo» |
| Identidad | «Para los que miran el techo antes de dormir» · «Si tu escritorio necesita una conversación» |
| Regalo | «El regalo de 5 cm que nadie olvida» · «Regala algo que se encienda» · «Lo que todo el mundo graba al abrirlo» |
| Sensación | «Dormir en el fondo de una piscina» · «Un planeta en tu mesilla» · «Tu cuarto, de noche bien hecho» |

## Textos de cada anuncio

| | Texto principal | Titular | Botón |
|---|---|---|---|
| CI1 / I1 | «Saturno, la Luna o una galaxia grabados con láser dentro de una bola de cristal de 5 cm. Luz cálida por USB. 🪐» | «Un planeta en tu mesilla» | Comprar |
| CI2 / I2 | «Apaga la luz y el techo se llena de olas que se mueven. 16 colores, mando a distancia y botón táctil. 🌊» | «Tu cuarto, bajo el mar» | Comprar |
| CI3 / I3 | «Un globo de 14 cm que flota sobre su base por levitación magnética, gira solo y se ilumina por dentro. 🌍» | «El mundo, flotando en tu escritorio» | Ver más |
| CI4 / I4 | «Lámpara planeta, proyector de olas, globo que levita y reloj 3D: cuatro luces para que tu cuarto cambie de noche. ✨» | «Decoración que se enciende» | Ver más |

Descripción para todos: «Envío con seguimiento · 14 días para devolver».

## Cómo testearla

- **Campaña:** «TEST · Cinemática · Ventas», con los mismos conjuntos por producto que la campaña UGC (lámpara, proyector y globo). En cada conjunto, el vídeo y la imagen de ese producto.
- **CI4 e I4** van en un conjunto aparte hacia la portada.
- **Presupuesto:** 10-15 €/día por conjunto durante 5-7 días.
- **Comparación:** con la campaña UGC (`../ugc/`), mira el CPA de cada estilo para el mismo producto. Donde gane uno, se le da más presupuesto y se hacen variantes con el banco de ganchos.
- **Reglas de decisión:** las de `../video/README.md`. El día 3 se pausa lo que tenga menos de un 25 % de gente viendo los 3 primeros segundos y además menos de un 0,8 % de CTR.

## Material y coste

- **Imágenes «héroe»** (Nano Banana 2, con las fotos reales de los productos como referencia): lámpara en macro, proyector en el techo, globo en la oscuridad y los 4 juntos.
- **Clips de Kling 3.0:** órbita alrededor de la lámpara y globo flotando con la cámara acercándose.
- **El clip del proyector no se usa:** Kling añadió humo saliendo del cubo, y el producto no echa vapor. Ese anuncio usa la imagen «héroe» con movimiento de cámara y los clips del proyector que ya había.
- **Coste:** 30,5 créditos de Higgsfield (4 imágenes y 3 clips). Saldo después: unos 9,8.
