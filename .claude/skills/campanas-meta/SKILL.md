---
name: campanas-meta
description: "Planifica, monta, lee y escala campañas de publicidad de pago para Orbiluz en Meta (Facebook e Instagram) y TikTok Ads, siempre con el CPA frente al margen de cada producto. Úsala cuando el usuario hable de anuncios de pago, campañas, presupuesto, testear creativos, CPA, ROAS, escalar, apagar anuncios, públicos, retargeting, Advantage+, o pregunte «¿qué hago con esta campaña?», «¿cuánto invierto?» o «¿por qué no vende?», aunque no diga «Meta»."
---

# Campañas de pago · Orbiluz

El objetivo es vender con beneficio. Los clics y las visualizaciones solo sirven si acaban en compras con un CPA por debajo del margen.

## Fuentes que ya existen (léelas, no las repitas)

- **`anuncios/meta/GUIA-CAMPANAS-META.md`** es la guía completa:
  - lista de comprobación previa;
  - márgenes y estructura de la cuenta;
  - guion del día 0 al 30;
  - reglas de decisión, textos, retargeting, temporadas, rutina y nomenclatura.
- **`anuncios/meta/LANZAMIENTO.md`:** la primera prueba con 100 €.
- **Los README de cada tanda de anuncios** (`anuncios/meta/*/README.md`): conceptos, textos y cómo testearlos.

## Números que mandan

Calcula siempre con `python3 .claude/skills/investigacion-productos/scripts/margen.py` en lugar de memorizar cifras: los costes cambian con el dólar y el proveedor.

| Producto | CPA de equilibrio aprox. | CPA objetivo (70 %) |
|---|---|---|
| Lámpara | ~11 € | ≤ 8 € |
| Proyector | ~12 € | ≤ 8,5 € |
| Reloj | ~14 € | ≤ 10 € |
| Globo | ~35 € | ≤ 24 € |

**En promociones el margen baja mucho:** con un −15 %, una lámpara deja unos 8 €. Recalcula el CPA objetivo para cada oferta.

## Cómo se trabaja

1. **Antes de gastar nada,** comprueba:
   - que el píxel y la API de conversiones envían `Purchase` con su valor;
   - que la ficha de destino carga bien en el móvil;
   - que el usuario ha hecho una compra de prueba (modo de prueba de Shopify Payments con la tarjeta 4242 4242 4242 4242).
2. **Estructura:**
   - **Prueba:** CBO, público amplio en España, 3-5 conceptos distintos y la ficha del producto como destino.
   - **Escalado:** Advantage+, con los ganadores y su mismo ID de publicación.
   - **Retargeting:** catálogo, el 10-20 % del presupuesto.
3. **Lanzar y no tocar en 72 h.** Cualquier cambio reinicia el aprendizaje.
4. **Decidir** con al menos 3 días de datos y según la tabla del apartado 5 de la guía:
   - **Apagar** si ha gastado 1,5 × el CPA de equilibrio, sin compras y con un CTR del enlace por debajo del 0,8 %.
   - **Ganador** si tiene 5 o más compras con un CPA por debajo del objetivo.
   - **Escalar** subiendo el 20 % cada 48-72 h.
5. **Refrescar las creatividades** cuando la frecuencia pase de 3 y el CTR caiga. Las variantes se piden con la skill `creativos-anuncios`.

## Diagnóstico rápido («no vende»)

| Síntoma | Dónde está el problema | Qué hacer |
|---|---|---|
| CTR < 0,8 % | Creatividad o gancho | Ganchos nuevos y un primer plano más llamativo |
| CTR bien, pocos añadidos al carrito | Ficha: precio, fotos o confianza | Revisar la ficha con `tienda-shopify` |
| Añadidos bien, pocas compras | Pago: envío, plazos, métodos o sorpresa en el total | Revisar el carrito y la página de pago, y que no aparezca un gasto inesperado |
| Compras con CPA > equilibrio | Oferta o margen | Packs, subir el valor medio del pedido o cambiar de producto |

## Sin datos de Meta en directo

**No hay conector de Meta Ads.** Pide al usuario una captura o la exportación del Administrador de anuncios con estas columnas:
- gasto, impresiones, CTR del enlace, CPC;
- añadidos al carrito, compras, CPA y ROAS;
- frecuencia y, en vídeo, las reproducciones de 3 s.

No te inventes resultados ni des por hecho que algo funciona sin verlo. Las ventas reales sí se ven en Shopify, en Pedidos y en las analíticas con ShopifyQL.

## TikTok Ads

Hay conector de TikTok for Business: búscalo con ToolSearch «TikTok». Mismo método, con estos matices:
- creatividades 9:16 de estilo nativo;
- Smart+ como equivalente de Advantage+;
- CPA medido igual.

Lee la configuración real de la cuenta antes de proponer cambios. **No crees ni actives campañas ni gastes dinero sin que el usuario lo confirme explícitamente.**

## Textos

- **Sin precios, sin reseñas inventadas, español de España.**
- **Texto principal:** beneficio más dato real. Ejemplo: «Saturno, la Luna o una galaxia grabados con láser dentro de una bola de cristal de 5 cm».
- **Titular corto.**
- **Parámetros UTM** para verlo en Shopify: `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`.
