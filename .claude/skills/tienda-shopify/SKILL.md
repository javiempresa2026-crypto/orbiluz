---
name: tienda-shopify
description: "Trabaja en la tienda Shopify de Orbiluz: cambios del tema (portada, carrito, fichas, estilos), descuentos y códigos, comprobación de precios, envíos y stock, fichas de producto, pruebas de compra y capturas de cómo se ve en móvil. Úsala cuando el usuario pida cambiar algo de la web o del carrito, crear o revisar descuentos, comprobar que la tienda o el pago funcionan, mejorar una ficha, «no me sale el descuento», «revisa la web» o «haz una versión del tema»."
---

# Tienda Shopify · Orbiluz

Tienda **orbiluz.com** (atzezc-eb.myshopify.com), con el tema Horizon personalizado y la zona horaria Europe/Madrid. Se usa el conector de Shopify (Admin GraphQL): descubre con `graphql_schema`, valida con `validate_graphql_codeblocks` y ejecuta.

## Temas: nunca se toca el publicado

1. **No se puede escribir en el tema publicado (MAIN)** y tampoco se puede publicar un tema desde aquí.
   - Duplica el publicado con `themeDuplicate`, dale un nombre claro («Orbiluz 2.1 (lo que cambie)»), edita la copia y que el usuario la publique.
   - Para saber cuál está publicado, consulta los temas con el rol MAIN (`roles: [MAIN]`).
2. **Archivos:**
   - Lee el archivo real de la copia con `theme(id){ files(filenames:[...]){ body } }` antes de editarlo, porque el usuario cambia cosas desde el editor.
   - Guarda tu versión en el repositorio (`tema/` o la carpeta de la campaña), haz commit y push.
   - Súbela con `themeFilesUpsert` y `body: {type: "URL", value: "https://raw.githubusercontent.com/javiempresa2026-crypto/orbiluz/<commit>/<ruta>"}`. Así te ahorras pegar archivos enormes.
   - **Orden de subida:** primero las secciones y los bloques nuevos, después los JSON que los usan.
3. **Personalizaciones que ya existen:**
   - `assets/orbiluz.css` es la capa de marca (estrellas, cabecera de noche, carrito de noche);
   - `sections/orbiluz-*.liquid` son la portada, la página, el pie, el banner y la sección cruzada;
   - `snippets/orbiluz-carrito-info.liquid` es la barra de envío gratis, la confianza y los iconos de pago;
   - la plantilla de cada promoción está en su carpeta, como `black-friday/tema/`.
   - **Estilo:** clases con prefijo propio (`.orb-`, `.bf-`) y paleta de marca:
     - noche #12123A;
     - ámbar #FFB547;
     - nebulosa #7C6CF6;
     - luna #FFF6E9;
     - coral #FF7A59.
   - **Fuentes:** Unbounded para los titulares y DM Sans para el texto.
4. **Si cambias colores de fondo en Horizon,** sobrescribe también sus variables: `--color-foreground`, `-rgb`, `-subdued`, `-muted`, `--color-input-*` y `--color-primary-button-*`. Si no, quedan textos oscuros sobre el fondo oscuro.

## Comprobar que funciona (siempre, antes de decir «hecho»)

- **Vista previa:** `https://orbiluz.com/?preview_theme_id=<id>`.
  - Con `requests` y `verify="/root/.ccr/ca-bundle.crt"` busca `Liquid error` en el HTML.
  - El estado del carrito se ve con `/?sections=cart-drawer-section`.
- **Capturas en móvil (390×844):** Playwright con `executable_path="/opt/pw-browsers/chromium"`.
  - **Pasa todas las peticiones por un `route`** que las descargue con `requests` y la CA del proxy. Si no, Chromium da `ERR_CERT_AUTHORITY_INVALID`.
  - Para el carrito, añade el producto primero con `POST /cart/add.js` en la misma sesión de `requests`.
- **Shopify bloquea las ráfagas de peticiones** (429 y «Verifying your connection…»). Si un carrito sale vacío, puede ser eso y no un fallo: espera y repite con calma.
- **Precios, envío y descuentos sin comprar:** `draftOrderCalculate` con `acceptAutomaticDiscounts: true`, una dirección española y `discountCodes` si toca. Da los descuentos aplicados y las tarifas de envío.
- **Compra de prueba real:** solo la puede hacer el usuario, con el modo de prueba de Shopify Payments (Configuración → Pagos) y la tarjeta 4242 4242 4242 4242. Después tiene que desactivarlo.

## Descuentos

- **Creación:**
  - automáticos con `discountAutomaticBasicCreate`;
  - de envío gratis con `discountAutomaticFreeShippingCreate`;
  - códigos con `discountCodeBasicCreate`.
- **Fechas en UTC:** las 00:00 de Madrid en invierno son las 23:00 UTC del día anterior.
- **Combinaciones:** con `combinesWith` en false para los de producto, Shopify aplica **el que más ahorra**. Explícaselo al usuario: no se suman.
- **Programados:** no se ven en el carrito hasta su fecha. Si el usuario quiere probarlos antes, crea una copia de prueba limitada a su ficha de cliente (`context.customers`) o un código temporal, y bórrala después.
- **Ofertas que ya existen:**
  - HOLA10;
  - «2 lámparas por 39,90 €»;
  - los descuentos de Black Friday (ver `black-friday/README.md`).

## Fichas de producto

- **Título:** claro, con la medida real.
- **Primeras líneas:** el beneficio.
- **Ficha técnica:** en tabla (dimensiones, alimentación, qué incluye).
- **Envío y devoluciones:** plazos reales y 14 días para devolver.
- **Nada de reseñas inventadas.** Las reales, cuando las haya, con una app de reseñas.
- **Precio tachado:** solo si es el precio real de los 30 días anteriores (norma europea de rebajas).

## Lo que no se toca sin permiso

Impuestos, pagos, envíos y políticas: se le explica al usuario dónde cambiarlo. Tampoco se borran productos, clientes ni pedidos.
