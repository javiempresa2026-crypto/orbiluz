# Prueba de las skills (19-10-2026)

Prueba real de las skills `creativos-anuncios` y `contenido-organico`: 2 vídeos orgánicos sin voz y con el estilo «viral».

- **Escenas nuevas de Higgsfield** (`nano_banana_2`, con las fotos reales de los productos como referencia; 3 créditos):
  - `material/p1-dormitorio-olas.png`: dormitorio de noche con el proyector y la lámpara.
  - `material/p2-escritorio-globo-reloj.png`: escritorio de noche con el globo y el reloj. Se difuminó la marca del portátil.
- **El resto** son clips que ya teníamos: interruptor, cuarto antes, olas, lámpara, globo.
- **Montaje:** `python3 contenido/prueba-skills/videos_prueba.py`, que saca cada vídeo en 9:16 y en 4:5.

| Vídeo | Gancho | Etiquetas | Formato |
|---|---|---|---|
| `P1-cuarto-mal-iluminado` | TU CUARTO NO ES FEO. ESTÁ **MAL ILUMINADO.** | Apaga la luz del techo · Olas en el techo + un planeta de 5 cm · Proyector y lámpara | Problema → solución |
| `P2-escritorio-23-47` | MI ESCRITORIO A LAS **23:47** | Un globo que flota solo · 14 cm · Y un reloj de dígitos 3D | Identidad / curiosidad |

## Fallos detectados en la revisión y corregidos

- **P1:** la etiqueta tapaba el proyector y la lámpara. Se subió a y=560. Para eso se añadió a `textos_ugc.py` el estilo `"nota@<y>"`, que coloca una etiqueta a otra altura.
- **P2:** la etiqueta del reloj aparecía antes de que el reloj saliera en pantalla. Se ajustaron los tiempos.

## Textos para Meta (sin precios)

| Vídeo | Texto principal | Titular |
|---|---|---|
| P1 | «Apaga la luz del techo: olas que se mueven en el techo y un planeta de 5 cm grabado en cristal. Tu cuarto, otro.» | Tu cuarto, bien iluminado |
| P2 | «Un globo de 14 cm que flota solo y un reloj de dígitos 3D: el escritorio que da ganas de quedarse.» | Tu escritorio, de otro planeta |
