# Orbiluz · reglas de trabajo

Tienda de dropshipping en España (Shopify, orbiluz.com): decoración que se enciende. El usuario no es técnico. Háblale en español de España, directo y sin jerga, y piensa siempre primero en el móvil.

## Normas que no se negocian
- **Nada inventado:** ni reseñas, ni testimonios («lo compré y me encanta»), ni cifras de ventas, ni clientes. Si un dato no está medido, no se pone.
- **Personas hechas con IA:** pueden salir en escenas, pero nunca como clientes ni opinando del producto. El contenido con IA se marca en Instagram (`isAiGenerated`) y TikTok (`isAigc`).
- **Sin precios en los anuncios.** La oferta puede ir en porcentaje (−15 %) solo en campañas de promoción.
- **Producto honesto:**
  - La lámpara mide 5 cm, y se dice.
  - Ningún efecto que el producto no haga (se descartó un vídeo de Kling que añadía humo al proyector).
  - No se prometen plazos de entrega que no se cumplan: 6-17 días laborables según producto.
- **Ni tokens ni claves en el repositorio**, y nunca se le piden al usuario. Los datos de clientes van en `gestion/datos/` y en `*.csv`, que están fuera de Git.
- **Ahorra créditos de Higgsfield y Kling:** primero reutiliza el material de `contenido/material`, `anuncios/*/material` y `tiktok/historias/material`.
- **Solo Orbiluz.** La otra tienda (Jarandana) no se toca.

## Datos clave (revísalos en Shopify antes de usarlos en algo importante)
| Producto | Handle | PVP | Coste aprox. con envío | CPA de equilibrio | Plazo |
|---|---|---|---|---|---|
| Lámpara bola de cristal 3D (4 modelos) | `lampara-bola-cristal-3d` | 24,90 € (2 por 39,90 €) | ~8,3 € | ~11 € | 6-12 días lab. |
| Proyector de ondas de agua | `proyector-ondas-de-agua` | 29,90 € | ~11,3 € | ~12 € | 6-12 días lab. |
| Reloj LED 3D | `reloj-led-3d` | 29,90 € | ~8,6 € | ~14 € | 8-17 días lab. |
| Globo terráqueo que levita (14 cm) | `globo-terraqueo-que-levita` | 129 € | ~64 € | ~35 € | 10-15 días lab. |

- **Envío:** gratis desde 39 € y 3,95 € por debajo. Se devuelve en 14 días.
- **Descuentos:** HOLA10 (−10 % en la primera compra) y «2 lámparas por 39,90 €» (automático).
- **IVA:** los precios lo llevan incluido. El usuario aún no está dado de alta; no se toca nada de impuestos en Shopify sin que lo pida.
- **Calcular márgenes:** `python3 .claude/skills/investigacion-productos/scripts/margen.py`.

## Herramientas y cuentas
- **Shopify:** conector Admin GraphQL.
  - Tema publicado: «Orbiluz 2.0 (carrito nuevo)».
  - Los temas no se pueden publicar desde aquí: se prepara una copia sin publicar y la publica el usuario.
- **Metricool:** marca 7279692, zona horaria Europe/Madrid. Publica en Instagram @orbiluzspain, TikTok @orbiluzspain y Facebook.
- **DSers:** el usuario tiene el plan gratuito y el conector de DSers exige el plan Advance. Para ver proveedores y vínculos, pide al usuario que lo mire.
- **Repositorio público:** las URL `raw.githubusercontent.com` sirven como enlaces públicos de archivos para Metricool y para subir archivos al tema de Shopify.

## Skills del proyecto (`.claude/skills/`)
| Skill | Para qué |
|---|---|
| `creativos-anuncios` | Imágenes y vídeos de anuncios y orgánicos |
| `campanas-meta` | Montar, leer y escalar campañas de Meta |
| `contenido-organico` | TikTok, Reels y carruseles, programados con Metricool |
| `investigacion-productos` | Buscar, validar y calcular el margen de productos nuevos |
| `tienda-shopify` | Temas, descuentos, fichas y pruebas de la tienda |
| `promociones` | Black Friday, Navidad, rebajas y otras fechas |
| `captacion-clientes` | Emails, captación de suscriptores y fidelización |
| `informe-semanal` | Estadísticas de redes y ventas, y qué hacer después |
| `atencion-cliente` | Responder a clientes, devoluciones y posibles estafas |
