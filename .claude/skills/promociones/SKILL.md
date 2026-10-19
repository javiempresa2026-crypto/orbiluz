---
name: promociones
description: "Diseña y prepara campañas de fechas señaladas para Orbiluz (Black Friday, Cyber Monday, Navidad, Reyes, San Valentín, Día de la Madre, Día del Padre, rebajas, aniversario o una oferta flash): oferta con margen calculado, descuentos programados en Shopify, versión del tema ambientada, imágenes de campaña sin precios y calendario. Úsala cuando el usuario mencione una fecha comercial, «quiero hacer una oferta», «prepara la campaña de Navidad», un código promocional o un descuento por temporada."
---

# Promociones de temporada · Orbiluz

El ejemplo completo y probado es **`black-friday/`**: su README, la sección `tema/sections/orbiluz-black-friday.liquid` y las imágenes de `imagenes/generar_black_friday.py`. Úsalo como plantilla y adapta lo que cambie.

## 1. Oferta con números (antes que nada)

- **Calcula el margen con el descuento:** `python3 .claude/skills/investigacion-productos/scripts/margen.py --todos --descuento <pct>`. Si el CPA objetivo baja de unos 6-8 €, la oferta solo se sostiene con orgánico o packs.
- **Mejor descuentos por cantidad que un porcentaje grande para todo.** Suben el valor medio del pedido.
  - Ejemplo: −15 % en todo y −25 % llevando 2 o más.
  - Ojo con el envío gratis desde 39 €. Si con el descuento el pedido baja de 39 €, el cliente paga más que sin oferta: añade el envío gratis a la propia oferta.
- **Productos caros (el globo):** mira el margen en combinación con otros productos, que puede bajar mucho.
- **Sin precio tachado inflado:** el precio de referencia tiene que ser el real de los 30 días anteriores.
- **Plazos de Navidad:** el envío tarda 6-17 días laborables según el producto. No prometas «llega antes de Navidad» sin contar los días (y los festivos). Pon una fecha límite de pedido realista o no lo prometas.

## 2. Shopify (con la skill `tienda-shopify`)

- **Descuentos automáticos programados** con su inicio y su fin en UTC, más el código si el usuario lo quiere (BLACKFRIDAY2026 se creó así).
- **Durante la oferta,** decide qué pasa con HOLA10 y con el pack de 2 lámparas. En Black Friday HOLA10 se pausó poniéndole fecha de fin; luego hay que reactivarlo.
- **Tema de la campaña:**
  - duplica el tema publicado y ambiéntalo: barra de anuncios, sección de portada con cuenta atrás, aviso en la ficha y carrito;
  - **enseña los precios rebajados solo cuando el descuento ya funciona** (estado `antes`, `activo` o `fin` según la fecha). Antes de la fecha, «desde el dd/mm».
- **Comprueba la oferta con `draftOrderCalculate`** en varios carritos: 1 producto, 2 iguales, 2 distintos y el globo.
- **Lista de tareas para el usuario:**
  - publicar el tema el día de inicio;
  - volver a publicar el tema normal al terminar («Orbiluz 2.0 (carrito nuevo)» o el que esté vigente);
  - reactivar lo que se pausó.

## 3. Creatividades (con la skill `creativos-anuncios`)

- **Solo porcentajes, sin precios.** 4:5 y 9:16.
- **Serie de imágenes:**
  - anticipo («Muy pronto»);
  - la oferta;
  - una por producto;
  - regalo;
  - último día.
- **Estilo:** fondo oscurecido con el producto real, sello de la fecha, gancho en mayúsculas con palabra clave en amarillo y pegatina con el %.

## 4. Calendario y textos

- **Calendario por fases:**
  - anticipo (una semana antes);
  - lanzamiento;
  - día fuerte (el día de la fecha);
  - último día.
- **Textos para Meta** sin precios.
- **Plan de presupuesto** según el CPA objetivo recalculado.
- **Orgánico:** prográmalo con la skill `contenido-organico` y pide permiso antes de publicar.

## Fechas de referencia (España)

| Fecha | Cuándo |
|---|---|
| San Valentín | 14-02 |
| Día del Padre | 19-03 |
| Día de la Madre | primer domingo de mayo |
| Black Friday | último viernes de noviembre (Black Week del lunes al Cyber Monday) |
| Navidad | 25-12 |
| Reyes | 06-01 (los pedidos fuertes, del 15-12 al 2-01) |
| Rebajas de enero | desde el 07-01 |
| Rebajas de verano | desde el 01-07 |
