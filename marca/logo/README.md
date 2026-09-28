# Logos de Orbiluz

El logotipo es la palabra **orbiluz** con la «o» convertida en un **planeta con anillo** (órbita + luz).
- **Tipografía:** Unbounded Bold, convertida en trazos (no hace falta tener la fuente instalada).
- **Colores:** Noche #12123A · Ámbar #FFB547 · Nebulosa #7C6CF6 · Luna #FFF6E9.

**Formatos:** SVG (vectorial, para imprenta y web) y PNG a varios tamaños. Los PNG sin «fondo» en el nombre son transparentes.

## `horizontal/` · logotipo completo (SVG + PNG de 600, 1200 y 2400 px de ancho)

| Versión | Cuándo usarla |
|---|---|
| `orbiluz-horizontal-fondo-noche` | **Principal.** Con su fondo azul noche |
| `orbiluz-horizontal-fondo-luna` | Con fondo claro (crema) |
| `orbiluz-horizontal-para-fondo-oscuro` | Transparente con texto claro: sobre fotos o fondos oscuros (cabecera web, anuncios) |
| `orbiluz-horizontal-para-fondo-claro` | Transparente con texto noche: sobre fondos blancos o claros |
| `orbiluz-horizontal-blanco` | A una tinta, blanco: marcas de agua, vídeos, fotos |
| `orbiluz-horizontal-negro` | A una tinta, noche: impresión a un color, sellos, grabado, etiquetas |

## `icono/` · solo el planeta (SVG + PNG de 180, 512 y 1024 px)

| Versión | Cuándo usarla |
|---|---|
| `orbiluz-icono-fondo-noche-redondeado` | Icono de app o accesos directos |
| `orbiluz-icono-fondo-noche-cuadrado` | Foto de perfil en redes (Instagram, TikTok y Facebook la recortan en círculo) |
| `orbiluz-icono-fondo-luna` | Perfil sobre fondo claro |
| `orbiluz-icono-transparente` | Planeta a color sin fondo |
| `orbiluz-icono-blanco` / `orbiluz-icono-negro` | A una tinta |

## `favicon/`

`favicon.ico` (16, 32 y 48), `favicon-16/32/48/192/512.png` y `apple-touch-icon-180.png`.

**En Shopify:** Tienda online → Temas → Personalizar → Configuración del tema → Logo y favicon.

## `redes/`

| Archivo | Uso |
|---|---|
| `perfil-1080.png` | Foto de perfil (Instagram, TikTok, Facebook) |
| `portada-facebook-1640x624.png` | Portada de la página de Facebook |
| `imagen-compartir-1200x630.png` | Imagen al compartir enlaces (WhatsApp, Facebook) |
| `portada-youtube-2560x1440.png` | Banner de YouTube |

## Archivos sueltos de esta carpeta

`orbiluz-logo-*.png/svg`, `orbiluz-icono.*` y `orbiluz-avatar.*` son las versiones originales. Las usan el tema de Shopify y los scripts de fotos y anuncios. **No las borres**; para cualquier uso nuevo, coge las de las subcarpetas.

## Normas de uso

- Deja alrededor un margen libre de, al menos, el alto de la «b».
- No deformes, gires ni cambies los colores del logo.
- No le pongas sombras ni contornos.
- Sobre fotos con mucho detalle, usa la versión `para-fondo-oscuro` o `blanco`.

**Regenerar el kit:** `python3 marca/generar_kit_logos.py` (necesita Playwright y Chromium).
