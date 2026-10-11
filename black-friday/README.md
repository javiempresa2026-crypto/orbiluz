# Black Friday 2026 · Orbiluz

Del **lunes 23 al lunes 30 de noviembre** (Cyber Monday), a las 23:59 hora de Madrid.

## La oferta

| Descuento | Condición | Cómo se aplica |
|---|---|---|
| **−15 %** | En todo | Automático en el carrito |
| **−25 %** | Llevando 2 o más unidades (se pueden combinar productos) | Automático en el carrito |
| **Envío gratis** | Llevando 2 o más, o desde 39 € como siempre | Automático en el carrito |

- **HOLA10 está pausado** del 23 al 30 de noviembre: caduca el 22 a las 23:59. El 1 de diciembre hay que reactivarlo (Descuentos → HOLA10 → quitar la fecha de fin).
- **No se acumulan:** Shopify aplica siempre el descuento mejor, sea uno de estos o el «2 lámparas por 39,90 €». El de 2 o más (−25 %) sale más barato que el «2 por 39,90 €», así que ese deja de aplicarse en estas fechas sin tocarlo.
- **Envío gratis llevando 2:** sin él, 2 lámparas con el −25 % se quedan en 37,35 €, por debajo de los 39 € del envío gratis, y el cliente pagaría más que con la oferta normal.

### Margen por pedido

Margen después de IVA, coste del proveedor y envío, sin contar la publicidad. Es una aproximación a partir del punto de equilibrio de cada producto.

| Pedido | Margen normal | Con Black Friday |
|---|---|---|
| 1 lámpara | ~11 € | ~8 € |
| 1 proyector | ~12 € | ~8 € |
| 1 reloj | ~14 € | ~10 € |
| 1 globo | ~35 € | ~19 € |
| 2 lámparas | ~22 € | ~8-12 € |
| Lámpara + reloj | ~25 € | ~14 € |
| Globo + lámpara | ~46 € | ~14 € |

- **El −25 % aprieta el margen.** Con estos márgenes, el coste por compra en anuncios tiene que quedar por debajo de unos 8 € para no perder dinero en un pedido de 1 producto.
- **Globo + otro producto:** deja menos margen que el globo solo. Si se ve que pasa a menudo, se puede excluir el globo del −25 %.

### Ya creado en Shopify

Los tres descuentos están **programados** y no hacen nada hasta el 23 de noviembre:

- «Black Friday · −15 % en todo»;
- «Black Friday · −25 % llevando 2 o más»;
- «Black Friday · envío gratis llevando 2 o más».

Se ven en Shopify, en **Descuentos**.

## La tienda: tema «Orbiluz Black Friday»

Es una copia del tema publicado («Orbiluz 1.9»), **sin publicar**. La tienda actual no cambia. Los archivos están en `tema/`.

- **Barra superior:** negra con letras doradas. Muestra «BLACK FRIDAY · −15 % en todo», «−25 % llevando 2 o más · sin códigos» y «Envío gratis llevando 2 o desde 39 €».
- **Portada:**
  - Sección nueva «Black Friday» arriba: título, las dos ofertas, cuenta atrás, los 4 productos con precio tachado y precio rebajado, y una nota legal.
  - La cuenta atrás dice «Empieza en» antes del 23, «Termina en» durante la oferta, y se oculta al terminar.
  - En el resto de la portada:
    - el botón «−10 % con HOLA10» pasa a «Ofertas Black Friday»;
    - la etiqueta de la lámpara pasa a «−25 % llevando 2»;
    - se quitan las tarjetas de HOLA10 y del «2 × 39,90 €»;
    - la pregunta sobre HOLA10 pasa a «¿Cómo funciona el descuento de Black Friday?».
- **Ficha de producto:** aviso negro bajo el precio: «BLACK FRIDAY · −15 % en todo · −25 % llevando 2 o más. Sin códigos: se aplica solo en el carrito».
- **Vista previa:** https://orbiluz.com/?preview_theme_id=190632100168

### Para activarlo (a mano)

Shopify no deja publicar temas desde aquí.

1. **El 23 de noviembre a primera hora:** Tienda online → Temas → «Orbiluz Black Friday» → **Publicar**. No antes: el precio tachado solo es cierto cuando el descuento ya funciona.
2. **El 1 de diciembre:** volver a publicar «Orbiluz 1.9» y reactivar HOLA10.

**Antes del 23 de noviembre** el tema no enseña precios rebajados: las tarjetas muestran el precio de siempre con «−15 % del 23 al 30/11», porque el descuento todavía no funciona en el carrito. A las 00:00 del 23 cambia solo a precio tachado y rebajado.

### Legal

- **Precio tachado:** es el precio de siempre, el mismo de los 30 días anteriores. Por eso cumple la norma de indicar el precio anterior en las rebajas. No hay que subir precios antes del Black Friday.
- **Nota legal:** la portada explica el precio tachado, que el −25 % se aplica al llevar 2 o más, que no se acumula con otros descuentos y las fechas.

## Imágenes de la campaña (`imagenes/`)

Cada imagen está en 4:5 (feed) y 9:16 (Historias y Reels). No llevan precios: la oferta va en porcentaje.

- **Regenerarlas:** `python3 black-friday/imagenes/generar_black_friday.py`
- **Estilo:**
  - fondo oscurecido y viñeta;
  - sello «BLACK FRIDAY» arriba;
  - gancho en mayúsculas con la palabra clave en recuadro amarillo;
  - pegatina con el descuento y etiqueta amarilla;
  - en 4:5, botón «Ver ofertas en orbiluz.com»;
  - en 9:16, todo queda entre y=250 e y=1250 y no hay botón, porque Meta pone el suyo.

| | Archivo | Gancho | Etiqueta | Cuándo |
|---|---|---|---|---|
| BF1 | `BF1-se-ve-a-oscuras` | ESTE AÑO EL BLACK FRIDAY SE VE **A OSCURAS** | Del 23 al 30 de noviembre | Anticipo, 16-22 nov |
| BF2 | `BF2-oferta` | LLÉVATE 2. **PAGA MENOS.** | −15 % en todo · −25 % llevando 2 | Toda la semana |
| BF3 | `BF3-lampara-regala-un-planeta` | REGALA UN **PLANETA** ESTE BLACK FRIDAY | Combina modelos y ahorra un 25 % | Toda la semana |
| BF4 | `BF4-proyector-bajo-el-mar` | TU TECHO, **BAJO EL MAR** | Olas en movimiento · 16 colores | Toda la semana |
| BF5 | `BF5-globo-que-flota` | EL GLOBO QUE **FLOTA** AHORA CON DESCUENTO | Levitación magnética · 14 cm | Toda la semana |
| BF6 | `BF6-regalos-resueltos` | LOS REGALOS DE NAVIDAD, **RESUELTOS** | Sin códigos · se aplica en el carrito | 26-30 nov |
| BF7 | `BF7-ultimo-dia` | **ÚLTIMO DÍA** DE BLACK FRIDAY | Termina hoy a las 23:59 | Solo el 30 nov |

## Textos para Meta (sin precios)

| | Texto principal | Titular | Botón |
|---|---|---|---|
| BF1 | «Este año apaga la luz del techo. Del 23 al 30 de noviembre, Black Friday en Orbiluz: decoración que se enciende. 🖤» | Black Friday a oscuras | Más información |
| BF2 | «−15 % en todo y −25 % si te llevas 2 (puedes combinar). Sin códigos: el descuento sale solo en el carrito. Y llevando 2, el envío es gratis. 🖤» | −25 % llevando 2 | Comprar |
| BF3 | «Saturno, la Luna o una galaxia grabados dentro de una bola de cristal de 5 cm. Llévate 2 modelos y ahorra un 25 %. 🪐» | Un planeta en tu mesilla | Comprar |
| BF4 | «Apaga la luz y el techo se llena de olas en movimiento. 16 colores y mando. −15 % en Black Friday. 🌊» | Tu cuarto, bajo el mar | Comprar |
| BF5 | «Un globo de 14 cm que flota por levitación magnética y gira solo. −15 % hasta el 30 de noviembre. 🌍» | El globo que flota | Comprar |
| BF6 | «Regalos que se encienden y no acaban en un cajón. −25 % llevando 2, sin códigos. 🎁» | Regalos resueltos | Comprar |
| BF7 | «Último día: el Black Friday de Orbiluz termina hoy a las 23:59. −25 % llevando 2 y envío gratis. 🖤» | Termina hoy | Comprar |

Descripción para todos: «Envío con seguimiento · 14 días para devolver».

## Calendario propuesto

- **16-22 nov · anticipo:**
  - BF1 en orgánico (Instagram, Facebook y TikTok);
  - un anuncio pequeño de alcance o de visitas a la web para crear público.
- **23 nov · inicio:**
  - publicar el tema;
  - campaña «BF · Ventas» con BF2 a BF5, un conjunto por producto más BF2 para la portada;
  - al público de visitantes de la web y de quienes han interactuado con la cuenta, más uno amplio.
- **26-29 nov:**
  - el día 27 es el Black Friday en sí: subir el presupuesto a lo que esté funcionando;
  - añadir BF6.
- **30 nov · Cyber Monday:**
  - cambiar todo a BF7 «Último día»;
  - el 1 de diciembre, volver a publicar «Orbiluz 1.9».

**Plazos de envío:** se mantienen los de siempre, de 6 a 17 días laborables según el producto. No hay que prometer entrega antes de Navidad en los anuncios.
