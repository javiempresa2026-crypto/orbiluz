# Orgánico de finales de octubre (6 vídeos sin créditos de IA)

Montados solo con material que ya existía, con la skill `creativos-anuncios`. El estilo es «viral», sin voz y con grano. Cada vídeo sale en 9:16 y en 4:5.

- **Montaje:** `python3 contenido/organico-octubre/videos.py`
- **Revisión:** hoja de fotogramas con `.claude/skills/creativos-anuncios/scripts/hoja_contactos.py`.

| Vídeo | Gancho | Ángulo | Publicación |
|---|---|---|---|
| O1-pov-apagas-la-luz | POV: APAGAS LA LUZ DEL TECHO POR **PRIMERA VEZ** | Problema → solución | mar 21-10 · 18:00 |
| O2-cosas-que-no-sabia | COSAS QUE MI CUARTO NECESITABA Y **NO SABÍA** | Lista de los 4 productos | lun 26-10 · 18:00 |
| O4-como-flota-esto | ¿CÓMO FLOTA **ESTO?** | Curiosidad (globo) | mar 27-10 · 18:00 |
| O5-planeta-en-tu-mano | EL PLANETA QUE CABE EN TU **MANO** | Producto con su medida real (lámpara) | mié 28-10 · 18:00 |
| O6-mi-rutina-de-noche | MI RUTINA DE **NOCHE** | Identidad | jue 29-10 · 18:00 |
| O3-no-regales-calcetines | ESTE AÑO **NO REGALES CALCETINES** | Regalo (llevar la contraria) | lun 02-11 · 18:00 |

## Fallos encontrados en la revisión y corregidos

- **O2:**
  - el gancho, en una línea, se salía por los bordes; se partió en 3 líneas;
  - las etiquetas numeradas entraban antes que su producto; se ajustaron a los cortes reales.
- **O3 y O6:** etiquetas que entraban antes de que su plano apareciera en pantalla.
- **O4:** con `*esto*?`, el asterisco salía escrito. Hay que dejar el signo dentro de los asteriscos: `*esto?*`.
- **O5:** la etiqueta del grabado era demasiado larga y salía diminuta; se acortó.
