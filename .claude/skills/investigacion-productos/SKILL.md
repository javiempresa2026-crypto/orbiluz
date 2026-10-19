---
name: investigacion-productos
description: "Busca, valida y calcula la rentabilidad de productos para la tienda de dropshipping Orbiluz (decoración que se enciende, regalos y gadgets de escritorio), compara proveedores de AliExpress o DSers y decide si añadir, sustituir o quitar un producto. Úsala cuando el usuario pida productos nuevos, ganadores o en tendencia, preguntar si un producto es rentable, calcular márgenes o el CPA de equilibrio, cambiar de proveedor, revisar stock o plazos, o «¿qué más puedo vender?»."
---

# Investigación de productos · Orbiluz

Un buen producto para Orbiluz cumple cuatro cosas:
- **Efecto visual:** se enciende, flota, se mueve o proyecta. Un vídeo de 3 s lo vende.
- **Compra por impulso o regalo:** entre 20 y 60 €.
- **Margen suficiente** para pagar los anuncios.
- **Envío fiable a España:** con seguimiento y en menos de 15 días.

## Paso 1 · Calcular el margen (siempre primero)

```bash
python3 .claude/skills/investigacion-productos/scripts/margen.py --pvp 24.90 --coste-usd 7.72 --envio-usd 1.99
python3 .claude/skills/investigacion-productos/scripts/margen.py --todos            # los 4 productos actuales
python3 .claude/skills/investigacion-productos/scripts/margen.py --todos --descuento 15   # con una promoción del −15 %
```

El script da:
- **margen neto:** PVP sin IVA − coste − envío − comisión de pago;
- **CPA de equilibrio** y **CPA objetivo** (70 % del margen);
- **ROAS de equilibrio.**

Revisa el cambio del dólar (`--cambio`) y la comisión de pago (`--comision`, por defecto 2,5 %).

**Cuándo merece la pena:** si el CPA objetivo baja de unos 8 €, el producto solo funciona con packs o con orgánico. Un margen neto de 12 € o más deja aire para los anuncios.

## Paso 2 · Validar demanda y proveedor

- **Proveedor:**
  - **AliExpress** (por DSers): más de 1.000 pedidos, 4,5 ★ o más, stock de la variante que vas a vender (no del total) y envío a España con seguimiento («AliExpress Selection» o similar).
  - **Mira el stock de cada variante:** el de la lámpara Galaxia era bajo (43 unidades), así que hay que vigilarlo o tener un segundo proveedor.
- **Enchufes y certificados:** si el producto va a la corriente (12 V o 220 V), confirma el **enchufe europeo** y la marca CE antes de venderlo. Con el globo quedó pendiente.
- **Tendencia y competencia:** busca en la web el producto en España, con sus nombres en español e inglés, y mira si ya lo anuncian otras tiendas. Mucha competencia con el mismo vídeo = guerra de precios.
  - La Biblioteca de anuncios de Meta no se consulta automáticamente (da 403): pide al usuario que busque allí anuncios con más de 30 días activos.
- **Encaje con la marca:** que se pueda fotografiar de noche y combine con los otros cuatro, para que se compren juntos.

## Paso 3 · Decidir

Presenta 3-5 candidatos en una tabla con:

| Columna | Qué poner |
|---|---|
| Producto | Nombre y foto o enlace |
| Proveedor | ID de AliExpress o DSers |
| Coste | Coste + envío, en USD y en € |
| PVP propuesto | Precio de venta |
| Margen | Margen neto |
| CPA | CPA objetivo |
| Plazo | Días hasta España |
| Stock | Stock de la variante que se va a vender |
| Ángulo | Ángulo creativo |
| Riesgos | Lo que pueda fallar |

Recomienda uno y explica por qué. **No crees productos en Shopify sin el visto bueno del usuario.**

## Herramientas y limitaciones

- **DSers:** el usuario tiene el **plan gratuito**, y el conector de DSers pide el plan Advance (da el error `PLAN_RESTRICTION`). Lo que no se pueda leer, pídelo al usuario: enlaces de proveedor, stock o capturas.
- **AliExpress bloquea las descargas automáticas:** devuelve páginas de verificación de 2 KB. No sirven como prueba de nada.
- **Shopify:** los productos actuales y su stock se ven con el conector (`products`, `inventoryQuantity`).
- **Al dar de alta un producto nuevo:**
  - fotos sin marcas de agua y que no parezcan de AliExpress;
  - medidas reales en el título o las primeras líneas;
  - plazos de envío reales en la ficha;
  - ficha técnica en tabla.
- **Historial de candidatos y descartes:** `productos-candidatos.md`, `estudio-mercado.md` y `TRASPASO.md`. Léelos para no proponer lo que ya se descartó.
