---
name: creativos-anuncios
description: "Crea creatividades para Orbiluz: imágenes estáticas de anuncios (4:5 y 9:16), vídeos de anuncios y vídeos virales con ganchos, títulos llamativos, cinemáticas y UGC sin voz o con voz natural. Úsala siempre que el usuario pida anuncios, creativos, imágenes para Meta o TikTok, ganchos (hooks), variantes de un anuncio ganador, vídeos virales, cinemáticas, comparativas o imágenes de problema y solución. También cuando diga «hazme algo que llame la atención», «otra versión de este anuncio» o «imágenes para la campaña», aunque no diga «creativo»."
---

# Creativos de anuncios · Orbiluz

Un creativo de Orbiluz tiene que parar el scroll en 1 segundo, enseñar el producto real encendido y no mentir. Esta skill recoge el sistema que ya funciona en el repositorio, para no empezar de cero cada vez.

## 1. Antes de crear: lo que ya existe

Reutiliza antes de generar con IA. Cada clip de Kling cuesta unos 7,5 créditos y el saldo suele ser bajo.

| Necesitas | Dónde está |
|---|---|
| Fotos «héroe» de los 4 productos (macro, techo, oscuridad, los cuatro juntos) | `anuncios/meta/cine/material/h1…h4*.png` |
| Clips cinemáticos (órbita de la lámpara, globo flotando, bucle del proyector) | `anuncios/meta/cine/material/c1…c3*.mp4` |
| Escenas UGC (unboxing, dedo en el globo, olas en el techo) | `anuncios/meta/ugc/material/` |
| Escenas de historias (cuarto antes y después, interruptor, regalos, móviles grabando) | `tiktok/historias/material/` |
| Clips de producto y vídeos virales anteriores | `contenido/material/`, `tiktok/material/` |
| Fotos limpias de producto | `fotos/` |
| Bancos de ganchos ya escritos | `anuncios/meta/cine/README.md` y `contenido/sistema-contenido.md` (apartado 5) |

Lee el README de la carpeta que vayas a usar: explica qué funcionó y qué se descartó, y por qué.

## 2. Motores (no los reescribas, úsalos)

- **Vídeos:** `tiktok/motor.py` → `montar(nombre, segmentos, salida_dir, ...)`.
  - **Segmentos:** imágenes (`dur`, `mov` = in, out, izq, der, sube; `ajustar`) o clips (`t0`, `t1`, `velocidad`, `rev`).
  - **Efectos:** `brillo` (resplandor, 0,2-0,3) y `filtro` (cadena de ffmpeg).
  - **Transiciones:** corte, flash, negro, fundido…
  - **Música:** `musica.py`, con los estilos lofi, house, trap y sueño, más `drop`.
  - **Texto:** `estilo_texto` = «viral» (mayúsculas que aparecen palabra a palabra, palabra clave en recuadro amarillo), «ugc», «cine» o «marca».
  - **Acabado:** `real="grano"` (grano de película), `formato_4x5=True` (saca también la versión 4:5) y `tarjeta_final(...)` para el cierre con la marca.
  - **Ejemplo completo:** `anuncios/meta/variantes/variantes.py`. Cópialo como plantilla.
- **Textos sobre la imagen:** `tiktok/textos_ugc.py`.
  - `gancho_viral(im, "Texto | *palabra clave*", 99, 1.0, y_centro=...)`: `|` fuerza el salto de línea y `*…*` pone el recuadro amarillo.
  - `nota_viral(im, texto, 1.0, y=...)` hace una etiqueta amarilla.
- **Imágenes estáticas:** usa como plantilla `anuncios/meta/variantes/imagenes_virales.py` o `black-friday/imagenes/generar_black_friday.py`. Tienen fondo oscurecido, sello, gancho, pegatina, etiqueta y botón.
- **Generar con IA, solo si falta material:**
  - **Higgsfield:** `nano_banana_2` para imágenes (2 créditos) con la foto real del producto como referencia; `kling3_0` de 5 s sin sonido (`sound:"off"`) para vídeo.
  - **Kling:** acepta imagen inicial y final, lo que permite hacer bucles perfectos con la misma imagen al principio y al final.
  - Revisa siempre el resultado fotograma a fotograma: Kling deforma los dígitos de los relojes y a veces se inventa humo o luces.

## 3. Medidas y zonas seguras

- **9:16:** 1080×1920. El texto importante va entre y≈250 y y≈1250, porque abajo tapan la interfaz y el botón de Meta o TikTok. Sin botón propio: Meta pone el suyo.
- **4:5:** 1080×1350, o el recorte del 9:16 en y 220-1570. Aquí sí puede ir el botón «Ver en orbiluz.com».
- **Siempre las dos versiones** de cada anuncio, con el sufijo `-4x5` y `-9x16`.

## 4. Qué funciona (aprendido con datos)

- En orgánico, los **ganchos de problema y solución** («No es el móvil, es la luz que tienes encima») retuvieron el doble que la animación pura (8 s de media frente a 3,6 s).
- **El mensaje tiene que estar en el primer segundo.** Una animación bonita sin texto inicial atrae, pero la gente se va.
- **Ángulos que tenemos:**
  - curiosidad («Sin hilos. Sin trucos. Sin explicación.»);
  - demostración («Tu techo puede hacer esto»);
  - llevar la contraria («Deja de comprar cojines. Cambia la luz.»);
  - identidad («Para los que miran el techo antes de dormir»);
  - regalo («El regalo de 5 cm que nadie olvida»);
  - sensación («Dormir en el fondo de una piscina»).
- **Para un ganador, varía el gancho y el primer plano**, no todo el vídeo. Así se sabe qué cambió el resultado.
- **Voz:** solo si suena natural. Si no, mejor sin voz, con texto cinético y música.

## 5. Normas (por qué importan)

Meta y TikTok penalizan las promesas falsas, y un cliente engañado devuelve el producto y deja de confiar en la marca.

- **Sin precios** en la creatividad, salvo porcentajes en promociones.
- **Sin reseñas ni clientes inventados.** Los actores de IA solo aparecen en escenas y sin opinar.
- **Medidas reales:** la lámpara mide 5 cm y el globo 14 cm. Ningún efecto falso.
- **Español de España,** frases cortas y en mayúsculas cuando el estilo es viral.

## 6. Comprobar antes de entregar

1. **Hoja de contactos de los vídeos:** extrae un fotograma cada 0,5-1 s con ffmpeg, júntalos y míralos. Busca textos cortados, recuadros fuera de sitio, fotogramas negros, saltos y efectos raros.
2. **Imágenes:** únelas en una hoja con PIL y míralas antes de dar nada por bueno.
3. **Sincronía:** que el cierre no aparezca antes de tiempo y que el gancho se lea completo antes del primer corte.
4. **Entrega:**
   - Sube al repositorio, en la carpeta de la campaña, el script, los archivos y un README con la tabla de gancho, etiquetas, destino y textos para Meta.
   - Manda al usuario la hoja de contactos con `SendUserFile`.

## 7. Textos que acompañan al anuncio

Para cada creatividad, entrega:
- **Texto principal:** 1-3 frases, beneficio más dato concreto, sin precio.
- **Titular:** 3-6 palabras.
- **Botón:** Comprar o Ver más.

La descripción común es «Envío con seguimiento · 14 días para devolver».
