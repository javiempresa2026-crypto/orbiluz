# TikTok orgánico · Orbiluz

10 vídeos verticales (1080×1920, 30 fps, de 10 a 18 s): 2 de cada producto y 2 con los 4 juntos.
Sin precios. Las voces en off (Ainsley, Marisol e Inés) son **narradoras de la marca** (no se hacen pasar por clientas) y no se inventan reseñas ni datos.

Montaje: `python3 tiktok/videos.py` (o `python3 tiktok/videos.py t1-lampara-apaga-el-techo` para uno solo).
- `motor.py`: el motor de edición (cortes, zoom, flash, subtítulos, sonidos, barra de progreso).
- `videos.py`: el guion de cada vídeo (planos, voz y textos).
- `musica.py`: la música original (sintetizada aquí, sin derechos de terceros).
- `preparar_voz.py`: acorta las pausas de las voces en off y las acelera un poco.
- `material/`: los clips y las voces de esta tanda.
- `videos/`: los mp4 listos para subir.

## Qué lleva cada vídeo para que la gente se quede

| Técnica | Para qué sirve |
|---|---|
| Gancho en texto grande en el primer segundo | Para el dedo antes de que pase al siguiente vídeo |
| Transiciones distintas en cada vídeo (desenfoque, deslizar, píxeles, círculo, aplastar, fundido a negro, destello…) | Que no parezcan todos de plantilla |
| Movimientos de cámara variados en las fotos (acercar, alejar, barrer a izquierda o derecha, subir) | Ninguna foto se queda quieta |
| Música propia con «drop»: intro suave, subida y entrada del ritmo justo cuando aparece el producto | El cambio de música marca el momento clave |
| En los vídeos sin voz, los cortes caen al ritmo de la música | Es lo que hace que un montaje «enganche» |
| La música baja sola cuando habla la voz | La voz se entiende siempre |
| Efectos de sonido muy bajos, y solo en algunas transiciones | Acompañan sin molestar |
| Subtítulos de 3 palabras con la palabra que suena en ámbar | Funcionan sin sonido y se leen al ritmo de la voz |
| Barra de progreso ámbar arriba y pregunta al final | Hace que se vea hasta el final y genera comentarios |

## Los 10 vídeos

| Vídeo | Producto | Voz | Música | Transiciones | Duración |
|---|---|---|---|---|---|
| `t1-lampara-apaga-el-techo` | Lámpara | Ainsley | Lofi (entra al encenderse la lámpara) | Desenfoque, destello, fundido, barrido, cortes, círculo | 15 s |
| `t2-lampara-cual-eliges` | Lámpara | — | House | Destello, deslizar, zoom | 11 s |
| `t3-globo-explicame-esto` | Globo | Marisol | Ambiental | Radial, desenfoque, círculo, fundido | 18 s |
| `t4-globo-escritorio` | Globo | — | Lofi | Corte, barrido, cortina, negro | 13 s |
| `t5-proyector-fondo-del-mar` | Proyector | Ainsley | Ambiental (entra con «y de repente») | Corte, círculo, desenfoque, radial | 11 s |
| `t6-proyector-colores` | Proyector | — | Trap | Destello, píxeles, corte, aplastar, subir | 15 s |
| `t7-reloj-las-tres-de-la-manana` | Reloj | Inés (voz grave) | Trap (entra con «o pones esto») | Desenfoque, negro, destello, corte, deslizar, zoom | 12 s |
| `t8-reloj-setup` | Reloj | — | House | Corte, aplastar, cortina | 10 s |
| `t9-cuatro-cosas-que-cambian-tu-cuarto` | Los 4 | Ainsley | House (cada producto entra con su número) | Destello, deslizar, subir, barrido | 15 s |
| `t10-cual-te-llevas` | Los 4 | — | Trap a 133 bpm (cada producto dura 4 tiempos) | Destello y cortes secos | 10 s |

## Sonido

- La música está compuesta en `musica.py` (lofi, house, trap y ambiental) y es nuestra, así que no hay problemas de derechos ni de silenciado.
- **Para el alcance**, añade además un sonido en tendencia desde TikTok **al 5-10 %**, casi sin que se oiga: TikTok también tiene en cuenta el sonido elegido para recomendar vídeos.
- Si conectas tu cuenta de TikTok a Higgsfield, puedo sacar la lista de canciones en tendencia con licencia comercial y publicar directamente con ellas.
- Las voces de Ainsley tenían pausas de hasta 1,3 s: `preparar_voz.py` las acorta a 0,25 s y acelera un 8-10 %, al ritmo de TikTok.

## Descripción, hashtags y comentario fijado

Pon tú el primer comentario y fíjalo. El enlace va en la bio.

- **T1** · La luz del techo es para buscar las llaves 🌙 #decoracionhabitacion #habitacionaesthetic #lamparadenoche #roomtour #fyp
  · Fijado: «¿Equipo luz del techo o equipo lámpara?»
- **T2** · Yo me quedo con la 1. ¿Y tú? 🪐 #lamparaplaneta #habitacionaesthetic #ideasderegalo #decoracion #fyp
  · Fijado: «Comenta tu número 👇»
- **T3** · Todavía no me lo explico 🌍 #globoflotante #gadgets #setupescritorio #curiosidades #fyp
  · Fijado: «¿Os lo explico o es más bonito sin saberlo? 👀»
- **T4** · Siempre la misma pregunta 🌍 #desksetup #setupescritorio #decoracionoficina #gadgets #fyp
  · Fijado: «¿Lo pondrías en tu escritorio o en el salón?»
- **T5** · Dormir bajo el mar 🌊 #proyectorolas #habitacionaesthetic #rutinadenoche #cozy #fyp
  · Fijado: «¿Te dormirías así?»
- **T6** · Mi parte favorita de la noche 💙 #luzambiente #habitacionaesthetic #cozy #roominspo #fyp
  · Fijado: «¿Qué color pondrías tú?»
- **T7** · Nunca más mirar el móvil a las 3 🕒 #relojdigital #insomnio #habitacion #gadgets #fyp
  · Fijado: «¿A qué hora te despiertas tú? 😅»
- **T8** · Un detalle y la estantería cambia por completo #desksetup #decoracionhabitacion #setup #gadgets #fyp
  · Fijado: «¿Pared o mesa?»
- **T9** · Las 4 cosas que más cambian un cuarto de noche ✨ #decoracionhabitacion #roommakeover #habitacionaesthetic #ideasderegalo #fyp
  · Fijado: «¿Con cuál empezarías?»
- **T10** · Solo una. Piénsalo bien 👀 #cualelegirias #decoracion #ideasderegalo #habitacionaesthetic #fyp
  · Fijado: «Comenta el número 👇»

## Plan de publicación

1. **Frecuencia:** 1 vídeo al día durante 10 días, alternando producto: t1, t3, t5, t7, t9, t2, t4, t6, t8, t10.
2. **Hora:** de 20:00 a 22:30 (hora peninsular). Sube el mismo vídeo a Reels 1-2 h después.
3. **Portada:** el fotograma con el producto encendido y el gancho visible.
4. **Primera hora:** contesta a todos los comentarios. Si alguien pregunta «¿dónde lo compro?», responde con un vídeo a ese comentario usando el mismo material.
5. **A los 3 días:** el que tenga más retención y más visualizaciones completas se vuelve a subir con otro gancho y pasa a probarse como anuncio en Meta.
6. **Qué no poner:** precios, «oferta» ni «compra ya».

## Coste

Créditos de Higgsfield gastados: **29,1** en total, con un saldo final de 164,3.

- Primera tanda (24,5): 2 escenas del proyector, 2 clips de Kling 3.0 y 5 voces de Marisol.
- Segunda tanda (4,6): 3 voces nuevas de Ainsley y 1 de Inés.

La música, las transiciones y los efectos no gastan créditos. El resto del material se reutiliza de `contenido/material/` y `fotos/`.
