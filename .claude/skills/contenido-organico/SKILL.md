---
name: contenido-organico
description: "Crea y programa contenido orgánico de Orbiluz para TikTok, Instagram (Reels y carruseles) y Facebook mediante Metricool: vídeos virales, historias, carruseles de valor y calendario de publicaciones. Úsala cuando el usuario pida subir, programar o publicar contenido, carruseles de consejos, vídeos para TikTok o Reels, un calendario de publicaciones, «sube esto a Instagram» o «programa la semana», aunque no mencione Metricool."
---

# Contenido orgánico · Orbiluz

El orgánico sirve para dar a conocer la marca y para probar ganchos gratis antes de pagar por ellos. Lo que funciona en orgánico es el mejor candidato a anuncio.

## Cuentas (Metricool)

- **Marca (blogId):** 7279692, zona horaria **Europe/Madrid**.
- **Redes:** Instagram y TikTok @orbiluzspain, y la página de Facebook 1344568635413187.
- **Herramientas** (cárgalas con ToolSearch «Metricool»):
  - `createScheduledPost` para programar;
  - `getScheduledPosts` para ver el calendario;
  - `updateScheduledPost` (cambia el `id` pero mantiene el `uuid`);
  - `getBestTimeToPostByNetwork` para las mejores horas;
  - `getAnalyticsDataByMetrics` para las estadísticas.
- **Archivos:** Metricool necesita URL públicas. Sube el archivo al repositorio (que es público), haz push y usa `https://raw.githubusercontent.com/javiempresa2026-crypto/orbiluz/<commit>/<ruta>`. Usa el hash del commit, no `main`, para que la URL no cambie.

## Al programar

- **Una misma publicación para las tres redes**, con:
  - `instagramData.type` REEL o POST;
  - `facebookData.type` REEL o POST;
  - `tiktokData.title`, `privacyOption` PUBLIC_TO_EVERYONE y `commercialContentOwnBrand: true`.
- **Si hay IA en el vídeo, márcalo:** `instagramData.isAiGenerated: true` y `tiktokData.isAigc: true`.
- **No uses el primer comentario en Instagram:** falla siempre. Pon la pregunta para comentar en el propio texto.
- **Horas:** los vídeos a las **18:00** (el pico en TikTok) y los carruseles a las 12:00. Comprueba antes con `getBestTimeToPostByNetwork`. En octubre de 2026 los mejores momentos en TikTok fueron el miércoles y el jueves a las 18:00 y a las 10:00; el fin de semana rinde la mitad.
- **Hora de verano:** hasta el último domingo de octubre, Madrid va en +02:00 y después en +01:00. Pon el desfase correcto en `date`.
- **Texto:**
  - gancho en la primera línea;
  - una pregunta que invite a comentar;
  - «🔗 Enlace en la bio»;
  - 4-5 hashtags del nicho (#decoracionhabitacion, #habitacionaesthetic, #roommakeover, #luzambiente, #fyp).
- **No dupliques:** mira el calendario con `getScheduledPosts` antes de añadir nada. Así evitas dos vídeos el mismo día o repetir uno.
- **Repasa el texto antes de programar:** las erratas en los hashtags (#deskssetup en vez de #desksetup) los dejan inútiles. Si ya está programado, corrígelo con `updateScheduledPost`: manda el contenido completo, usa como `media` la URL de static.metricool.com que devolvió la creación, y ten en cuenta que el `id` cambia.

## Qué publicar (aprendido con datos)

- **Sí:** vídeos de **problema y solución**. Son los que más alcance y retención tuvieron: 787 reproducciones en TikTok y 49 % de gente que pasa de los 3 primeros segundos en Instagram.
- **Con matiz:** la **animación del producto** atrae alcance en Facebook e Instagram, pero se abandona antes. Añade el mensaje en el primer segundo.
- **Mejor en Instagram que en TikTok:** los **carruseles**. En TikTok, las fotos subidas desde Metricool salen sin sonido y apenas se reparten. Si van a TikTok, que el usuario les ponga un sonido en tendencia a mano.
- **Ritmo:** 1 vídeo al día y 2-3 carruseles por semana. Mejor constancia que picos.

## Crear el contenido

- **Vídeos:** skill `creativos-anuncios`, con `tiktok/motor.py` y el estilo «viral». Hay ejemplos en `tiktok/videos.py`, `tiktok/historias/` y `anuncios/meta/variantes/`.
- **Carruseles de valor** (consejos, rutinas, guías de regalo): plantilla en `contenido/carruseles/generar_carruseles_valor.py`, con 7 diapositivas de 1080×1350.
  - **Estructura:** gancho → 5 pasos o ideas → cierre con la marca.
  - **Que sean útiles por sí mismos,** no un anuncio disfrazado: así la gente los guarda.

## Normas

- **Nada de testimonios inventados.** Las personas hechas con IA solo aparecen en escenas.
- **Español de España,** y pensado para verse en móvil.
- **No publiques ni cambies nada sin que el usuario lo haya pedido.** Si pide «revisar», solo informa.
