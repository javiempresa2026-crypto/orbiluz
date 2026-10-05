# TikTok orgánico · Orbiluz

10 vídeos verticales (1080×1920, 30 fps, de 10 a 18 s): 2 de cada producto y 2 con los 4 juntos.
Sin precios. La voz en off es la **narradora de la marca** (no se hace pasar por una clienta) y no se inventan reseñas ni datos.

Montaje: `python3 tiktok/videos.py` (o `python3 tiktok/videos.py t1-lampara-apaga-el-techo` para uno solo).
- `motor.py`: el motor de edición (cortes, zoom, flash, subtítulos, sonidos, barra de progreso).
- `videos.py`: el guion de cada vídeo (planos, voz y textos).
- `material/`: los clips y las voces de esta tanda.
- `videos/`: los mp4 listos para subir.

## Qué lleva cada vídeo para que la gente se quede

| Técnica | Para qué sirve |
|---|---|
| Gancho en texto grande en el primer segundo | Para el dedo antes de que pase al siguiente vídeo |
| Corte cada 1,5-3 s con zoom de entrada y un destello blanco | Mantiene el ritmo y no deja que el ojo se aburra |
| «Whoosh» en cada corte y un «pop» al final | El cambio de plano también se oye |
| Subtítulos de 3 palabras con la palabra que suena en ámbar | Funcionan sin sonido (la mayoría ve TikTok en silencio) y se leen al ritmo de la voz |
| Barra de progreso ámbar arriba | Hace que se vea hasta el final |
| Pregunta o «comenta el número» al final | Genera comentarios, que es lo que más alcance da |
| Final que enlaza con el principio | El vídeo se repite solo y cuenta como volver a verlo |

## Los 10 vídeos

| Vídeo | Producto | Voz | Gancho | Duración |
|---|---|---|---|---|
| `t1-lampara-apaga-el-techo` | Lámpara | Sí | HAZ ESTO ESTA NOCHE | 16 s |
| `t2-lampara-cual-eliges` | Lámpara | No | ELIGE TU PLANETA (1-4, comenta tu número) | 11 s |
| `t3-globo-explicame-esto` | Globo | Sí | ¿CÓMO FLOTA ESTO? | 18 s |
| `t4-globo-escritorio` | Globo | No | Lo que todo el mundo pregunta al entrar a mi despacho | 13 s |
| `t5-proyector-fondo-del-mar` | Proyector | Sí | TU CUARTO, BAJO EL MAR | 12 s |
| `t6-proyector-colores` | Proyector | No | POV: pones esto antes de dormir | 15 s |
| `t7-reloj-las-tres-de-la-manana` | Reloj | Sí | ¿TE PASA ESTO A LAS 3:00? | 16 s |
| `t8-reloj-setup` | Reloj | No | El detalle que cambia una estantería | 10 s |
| `t9-cuatro-cosas-que-cambian-tu-cuarto` | Los 4 | Sí | 4 COSAS QUE CAMBIAN TU CUARTO | 16 s |
| `t10-cual-te-llevas` | Los 4 | No | Solo puedes quedarte con UNO (1-4) | 10 s |

## Sonido

- **Vídeos con voz (t1, t3, t5, t7, t9):** añade en TikTok un sonido en tendencia tranquilo y **bájalo al 10-15 %** para que la voz se oiga bien.
- **Vídeos sin voz (t2, t4, t6, t8, t10):** ya llevan los «whoosh». Ponles un sonido en tendencia al volumen normal. En t2 y t10 va mejor uno con golpes marcados, para que cada número caiga en un golpe.
- La música no va dentro del archivo: la de la biblioteca de TikTok es la que ayuda al alcance y no da problemas de derechos.

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

Créditos de Higgsfield gastados en esta tanda: **24,5** (2 escenas del proyector, 2 clips de Kling 3.0 y 5 voces de Marisol). Saldo después: 168,9.
El resto del material se reutiliza de `contenido/material/` y `fotos/`.
