---
name: informe-semanal
description: "Saca y analiza las estadísticas de Orbiluz (redes sociales con Metricool, ventas, carritos y tráfico de Shopify) y convierte los datos en decisiones concretas para la semana siguiente. Úsala cuando el usuario pregunte «¿cómo va la tienda?», «¿qué ha funcionado?», «revisa las estadísticas», «informe semanal», «¿cuánto he vendido?», o cuando salte una revisión programada de redes o de ventas."
---

# Informe semanal · Orbiluz

Un informe solo sirve si termina en **qué repetir, qué cambiar y qué dejar de hacer**. Con pocos datos, dilo y no saques conclusiones fuertes.

## 1. Redes (Metricool, marca 7279692, Europe/Madrid)

1. **Estado de las publicaciones:** `getScheduledPosts` de las fechas del periodo; el estado de cada red está en `providers[]`.
   - `ERROR` con «Could not add the first comment» quiere decir que **sí se publicó**: solo falló el primer comentario.
2. **Estadísticas por publicación** con `getAnalyticsDataByMetrics` (fechas ISO con +01:00 o +02:00):
   - **Reels de Instagram:**
     - `IGRE02` fecha;
     - `IGRE06` URL;
     - `IGRE11` alcance;
     - `IGRE23` reproducciones;
     - `IGRE24` tiempo medio de visualización;
     - `IGRE28` % que pasa de 3 s;
     - `IGRE10` me gusta;
     - `IGRE07` comentarios;
     - `IGRE12` guardados;
     - `IGRE21` compartidos.
   - **Publicaciones y carruseles de Instagram:**
     - `IGPO02` fecha;
     - `IGPO06` URL;
     - `IGPO07` tipo;
     - `IGPO14` alcance;
     - `IGPO28` visualizaciones;
     - `IGPO13` me gusta;
     - `IGPO08` comentarios;
     - `IGPO15` guardados;
     - `IGPO27` compartidos.
   - **TikTok:**
     - `TKPO02` fecha;
     - `TKPO03` URL;
     - `TKPO22` tipo;
     - `TKPO06` duración;
     - `TKPO07` reproducciones;
     - `TKPO08` me gusta;
     - `TKPO09` comentarios;
     - `TKPO10` compartidos;
     - `TKPO13` % que lo ve entero;
     - `TKPO15` tiempo medio.
   - **Reels de Facebook:** `FBRE02` fecha, `FBRE06` URL, `FBRE10` reproducciones y `FBRE13` tiempo medio. **Publicaciones de Facebook:** `FBPO12` alcance.
   - **Seguidores:** `IGEV01` en Instagram, `TKEV07` en TikTok y `FBEV17` en Facebook.
   - **Cuidado con el orden de las columnas:** la respuesta las devuelve en el mismo orden en que las pides. Comprueba que encajan antes de interpretarlas.
3. **Compara por formato** (problema-solución, animación, transformación, producto, carrusel) y por red. **Lo que más importa:** tiempo medio y % que pasa de 3 s (retención) y, después, guardados y compartidos. Los me gusta valen poco.

## 2. Tienda (Shopify)

- **Pedidos del periodo:** `orders`, sin los de prueba (`test: true`) ni los cancelados.
- **Carritos abandonados:** `abandonedCheckouts`.
- **Analíticas con ShopifyQL** (herramienta `run-analytics-query`): sesiones, tasa de conversión, ventas por canal (UTM) y productos más vistos.
- **Beneficio real:** ingresos sin IVA − coste de los productos − comisión − gasto en anuncios (pídeselo al usuario). Usa `.claude/skills/investigacion-productos/scripts/margen.py` como referencia.

## 3. Formato del informe (en el chat, en español)

1. **Estado:** qué se publicó bien y qué falló, en una línea por problema.
2. **Tabla por publicación:** fecha, formato, y en cada red alcance o reproducciones, retención e interacciones.
3. **Ventas:** pedidos, ingresos, carritos abandonados y conversión, con la comparación frente a la semana anterior si hay datos.
4. **Qué funciona y por qué,** en 3-4 frases y avisando si la muestra es pequeña.
5. **Propuestas para la semana siguiente:** 3-5 acciones concretas (qué repetir, qué cambiar y qué probar).

## Normas

- **No publiques, no borres y no cambies nada:** el informe solo informa. Las propuestas las aprueba el usuario.
- **Revisión periódica:** si el usuario la quiere, prográmala con `create_trigger` (por ejemplo, los sábados por la tarde, hora de Madrid) con un mensaje que diga «no publiques ni cambies nada sin preguntar».
