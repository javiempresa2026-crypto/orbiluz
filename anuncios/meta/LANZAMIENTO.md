# Lanzamiento: Reel de Instagram y primera campaña de Meta (octubre 2026)

## A. Reel orgánico (hoy)

**Vídeo:** `contenido/virales/v7-problema-luz-del-techo-voz-ines.mp4` (9:16, 18 s, con voz).

1. Instagram › + › Reel › sube el vídeo.
2. **Música:** si añades una canción, ponla en volumen 10-15 % para que la voz se oiga bien. También puedes dejar solo la voz.
3. **Portada:** el fotograma de la lámpara encendida, segundo 9.
4. **Descripción:**
   > La luz del techo es para buscar las llaves, no para vivir tu habitación 🌙
   > ¿Equipo techo o equipo lámpara? 👇
   > #decoracionhabitacion #habitacionaesthetic #lamparadenoche #hogaracogedor #roominspo
5. **Activa «Compartir también en Facebook».**
6. **Publica entre las 20:00 y las 22:00.** Cuando lo publiques, deja este comentario y fíjalo: «¿Equipo luz del techo o equipo lámpara? 👀».
7. **Enlace en la bio:** orbiluz.com.

## B. Conectar Meta con la tienda (una vez, unos 20 min)

| # | Paso | Dónde | Estado |
|---|---|---|---|
| 1 | Instalar el canal **Facebook & Instagram** (de Meta) | Shopify › Aplicaciones › Shopify App Store | ✅ instalado (01/10/2026) |
| 2 | Conectar: Business Manager, página de Facebook, Instagram y cuenta publicitaria | Dentro de la app | ✅ |
| 3 | **Píxel:** crear o elegir uno. **Uso compartido de datos: «Máximo»** (activa la API de conversiones) | App › Configuración › Uso compartido de datos | ✅ píxel 28485803354438404 cargando en la web (cambiado el 01/10/2026) |
| 4 | **Catálogo:** sincronizar los 4 productos | App › Catálogo | ✅ los 4 productos publicados en el canal |
| 5 | **Dominio verificado** | Business Manager › Seguridad de la marca › Dominios | ✅ (etiqueta publicada en el tema 1.9) |
| 6 | **Probar eventos:** abre orbiluz.com, mira una ficha, añade al carrito y ve al pago. Deben aparecer `ViewContent`, `AddToCart` e `InitiateCheckout` | Administrador de eventos › Probar eventos | ☐ |
| 7 | **Método de pago** en la cuenta publicitaria y **límite de gasto** | Configuración de pagos de la cuenta publicitaria | ✅ límite de 100 € |

## C. Primera campaña: «PRUEBA · Lámpara · Ventas»

| Campo | Valor |
|---|---|
| Objetivo | Ventas |
| Evento | Compra (píxel de Orbiluz) |
| Presupuesto | **20 €/día** de la campaña (CBO), durante 5 días (prueba de 100 €) |
| Público | España, 18-55 años, todos los sexos, sin intereses (amplio) |
| Ubicaciones | Advantage+ (automáticas) |
| Destino | `https://orbiluz.com/products/lampara-bola-cristal-3d` |
| Parámetros de URL | `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}` |
| Mejoras creativas automáticas | **Desactivadas** (ni música ni texto añadidos) |

**Anuncios (4 conceptos distintos):**

| Nombre | Archivo 4:5 (feed) | Archivo 9:16 (Reels e Historias) | Ángulo |
|---|---|---|---|
| V7 · Luz del techo · voz | `contenido/virales/v7-problema-luz-del-techo-voz-ines-4x5.mp4` | `contenido/virales/v7-problema-luz-del-techo-voz-ines.mp4` | Problema → solución |
| A1 · Regalo mano | `anuncios/meta/A1-regalo-mano-4x5.jpg` | `anuncios/meta/A1-regalo-mano-9x16.jpg` | Regalo |
| A2 · Apaga la luz | `anuncios/meta/A2-apaga-la-luz-4x5.jpg` | `anuncios/meta/A2-apaga-la-luz-9x16.jpg` | Ambiente |
| A6 · Cuál es el tuyo | `anuncios/meta/A6-cual-es-el-tuyo-4x5.jpg` | `anuncios/meta/A6-cual-es-el-tuyo-9x16.jpg` | Elección |

**Textos del anuncio V7:**
- **Texto principal:** «La luz del techo por la noche es fría y demasiado fuerte. Apágala y enciende un planeta: luz cálida que además decora tu habitación. 🌙»
- **Titular:** «Tu cuarto, con otro ambiente»
- **Descripción:** «Envío con seguimiento · 14 días para devolver»
- **Botón:** Comprar

Los textos del resto de anuncios están en el apartado 7 de `GUIA-CAMPANAS-META.md`.

**Regla:** no se lanza la campaña hasta que el paso B6 funcione. Después, **72 horas sin tocar nada**. Luego se aplican las reglas de decisión de la guía (apartado 5).


## D. Prueba con 100 € (plan ajustado)

Con 100 € no se busca todavía rentabilidad. La prueba sirve para averiguar **qué anuncio para el scroll y lleva gente a la ficha**.

- **Presupuesto:** 20 €/día durante 5 días. Lleva **3 anuncios**, no 4, para que cada uno reciba gasto suficiente:
  - V7 «Luz del techo» con voz;
  - A2 «Apaga la luz»;
  - A1 «Regalo».
- **Punto de equilibrio de la lámpara:** CPA de unos 11 €. Si salen 5 o más compras con los 100 €, ya hay un ganador claro.

| Cuándo | Qué mirar | Qué hacer |
|---|---|---|
| Días 1-2 (unos 40 €) | Nada | No tocar |
| Día 3 (unos 60 €) | Por anuncio: **CTR del enlace**, **CPC** y si hay añadidos al carrito | Pausar el anuncio con CTR < 0,8 % **y** CPC > 1 € sin ningún añadido al carrito |
| Día 5 (100 €) | Compras, CPA y anuncio con más añadidos al carrito | El mejor se queda; se hacen 2-3 variantes de ese concepto (otro gancho, otra voz o música) para la siguiente ronda |

**Señales buenas:**
- CTR del enlace > 1,5 %
- CPC < 0,60 €
- Coste por añadido al carrito < 4 €
- Alguna compra
