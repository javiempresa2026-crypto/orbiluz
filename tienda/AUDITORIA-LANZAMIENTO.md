# Auditoría de la tienda tras el lanzamiento (29/09/2026)

He recorrido orbiluz.myshopify.com como cliente, en móvil: portada, colecciones, las 4 fichas, carrito, pago, páginas legales y 67 URL internas.

## Lo que está bien
- Sin enlaces rotos (67 páginas revisadas). `/policies/refund-policy` redirige a la página de devoluciones en español.
- Pagos: Shopify Payments activo con Apple Pay, Google Pay y Shop Pay. El pie muestra además Visa, Mastercard, Maestro, Amex, PayPal y Klarna.
- Envíos coherentes con lo que anuncias: 3,95 € por debajo de 39 € y gratis desde 39 €, con seguimiento.
- Descuentos activos: HOLA10 (10 % en la primera compra) y 2 lámparas por 39,90 €.
- Páginas legales en español y enlazadas en el pie: condiciones de venta, devoluciones (14 días), envíos, aviso legal, privacidad y cookies.

## Corregido por mí
- Textos en inglés del tema. Traducidos en el tema **Orbiluz 1.7**, que hay que publicar:
  - «Cart» → «Tu carrito»
  - «You may also like» → «También te puede gustar»
  - «View all» → «Ver todo»
  - Página 404: «Página no encontrada» y «Seguir comprando»
  - «Collections» → «Colecciones»
  - Página de contraseña: «Muy pronto»
- Blog «News» → «Novedades».

## Pendiente (lo tienes que hacer tú en el panel)
| # | Qué | Dónde | Por qué |
|---|---|---|---|
| 1 | Publicar el tema **Orbiluz 1.7** | Tienda online › Temas › Orbiluz 1.7 › Publicar | Quita los textos en inglés |
| 2 | Idioma predeterminado: **español**; despublicar el inglés | Configuración › Idiomas | El predeterminado de la tienda es el inglés. Existe una versión /en a medio traducir, y partes del pago y de la cuenta de cliente pueden salir en inglés |
| 3 | Pegar las políticas en español | Configuración › Políticas (textos en `politicas-para-pegar.html`) | La política de privacidad de Shopify está en inglés, con tu Gmail personal y la dirección mal («18600, 18600 Motril»). Las de reembolso, envío y condiciones están vacías, y son las que se enlazan en la página de pago |
| 4 | Correo de la tienda: orbiluzsupport@gmail.com | Configuración › General › Correo del remitente | Ahora los emails a clientes salen desde javiempresa2026@gmail.com |
| 5 | Aviso legal completo: nombre y apellidos (o razón social), NIF y dirección completa | Pásamelos y lo actualizo | Lo exige el art. 10 de la LSSI. Ahora solo pone «Orbiluz, Granada» |
| 6 | Banner de cookies activado para España/UE | Configuración › Privacidad del cliente › Banner de cookies | No lo puedo comprobar desde aquí: no tengo permiso y el servidor no está en la UE |
| 7 | Pedido de prueba real | Compra una lámpara con HOLA10 y luego reembolsa | La pantalla de pago bloquea las pruebas automáticas, así que conviene comprobarla con un pago de verdad |
| 8 | Dominio propio | Ver abajo | Quitar «myshopify» |

## Mejoras recomendadas
- **Reloj:** la ficha dice «8-17 días laborables», pero el proveedor tarda ahora 5-9 días (AliExpress Selection Premium). Pon «6-12 días laborables» como en las lámparas: prometer menos días vende más.
- **DSers:** hay 3 productos duplicados en estado «Deleted». Bórralos para no liarte al tramitar pedidos.
- **Globo:** el mapa está en inglés (ya se indica en la variante). Mantenlo visible en la ficha para evitar devoluciones.

## Dominio orbiluz.com
Según las DNS, a 29/09/2026 ni orbiluz.com ni orbiluz.es están registrados.
1. Shopify › Configuración › Dominios › **Comprar dominio nuevo** › `orbiluz.com` (unos 14 €/año). Se configura solo.
2. Si lo compras fuera (Namecheap, DonDominio…): **Conectar dominio existente**. Registro A `@` → `23.227.38.65` y CNAME `www` → `shops.myshopify.com`.
3. Márcalo como **dominio principal**. Las visitas a myshopify.com se redirigen solas.
4. Después, cambia la URL en Meta (píxel y dominio verificado), en la bio de Instagram y en TikTok.

Opcional: compra también orbiluz.es y redirígelo al .com.

## Cobros (dónde poner el IBAN)
- **Tarjetas, Apple Pay, Google Pay y Bizum:** Configuración › Pagos › Shopify Payments › Gestionar › **Cuenta de depósito**: IBAN a tu nombre (o al de tu empresa). Shopify también pide DNI y datos fiscales para verificar la cuenta. Hasta completarlo, los cobros se retienen.
- **PayPal:** el dinero va a tu cuenta PayPal; desde ahí lo retiras a tu banco.
- **Klarna:** se liquida junto con Shopify Payments.
