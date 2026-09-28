# Guía de campañas de Meta Ads para Orbiluz

*Versión 1 · 28-09-2026 · Para Facebook e Instagram (Meta Ads Manager)*

**Objetivo:** vender con beneficio, no conseguir clics ni visualizaciones. Cada decisión de esta guía se toma mirando **el coste por compra (CPA) frente al margen de cada producto**.

**Normas de la marca que se aplican a todos los anuncios:**
- Sin precios ni ofertas en la creatividad. El enlace lleva a la ficha y el precio se ve allí.
- Nada de reseñas, cifras ni clientes inventados.
- Nada de personas generadas por IA presentadas como clientes.
- Español de España.

---

## Índice

1. Antes de gastar un euro (lista de comprobación)
2. Los números que mandan (margen, ROAS y CPA de equilibrio)
3. Estructura de la cuenta
4. Guion paso a paso: del día 0 al día 30
5. Reglas de decisión: cuándo apagar, mantener o escalar
6. Sistema de creatividades (cómo producir ganadores sin quemar dinero)
7. Textos del anuncio: plantillas sin precios
8. Retargeting y catálogo
9. Temporadas: Black Friday, Navidad y Reyes
10. Rutina diaria y semanal (15 minutos al día)
11. La ficha de producto también es parte del anuncio
12. Errores que más dinero cuestan
13. Nomenclatura
14. Plantilla de seguimiento

---

## 1. Antes de gastar un euro

Sin estos puntos, Meta no puede aprender quién compra y el dinero se pierde a ciegas.

| # | Tarea | Dónde | Hecho |
|---|---|---|---|
| 1 | **Pagos activados**: Shopify Payments con tarjeta, Apple Pay y Google Pay, más PayPal | Shopify → Configuración → Pagos | ☐ |
| 2 | **Tienda sin contraseña** y con un plan de pago elegido | Shopify → Tienda online → Preferencias | ☐ |
| 3 | **Business Manager** (Meta Business Suite) con la página de Facebook y la cuenta de Instagram de Orbiluz | business.facebook.com | ☐ |
| 4 | **Canal «Facebook e Instagram»** de Shopify instalado y conectado. Crea el **píxel** y activa la **API de conversiones** con el nivel de datos «Máximo» | Shopify → Aplicaciones → Facebook & Instagram | ☐ |
| 5 | **Dominio verificado** en Meta | Business Suite → Seguridad de la marca → Dominios | ☐ |
| 6 | **Catálogo sincronizado**: los productos de Shopify aparecen en Meta, con fotos limpias | Commerce Manager | ☐ |
| 7 | **Comprobar los eventos**: `ViewContent`, `AddToCart`, `InitiateCheckout` y `Purchase` llegan con valor y moneda | Administrador de eventos → Probar eventos | ☐ |
| 8 | **Método de pago** en la cuenta publicitaria y un límite de gasto de seguridad | Configuración de pagos | ☐ |
| 9 | **Políticas legales pegadas** en Shopify (privacidad, devoluciones, envíos y términos) y **aviso de cookies** activado | Shopify → Configuración → Políticas / Privacidad del cliente | ☐ |
| 10 | **Una compra de prueba real** (y reembolsarla) para ver que `Purchase` se registra con su valor | Tienda + Administrador de eventos | ☐ |

> **Regla:** si el punto 7 o el 10 fallan, no se lanza la campaña. Sin el evento de compra bien medido, Meta optimiza a ciegas.

---

## 2. Los números que mandan

### 2.1 Margen por pedido (datos de `estudio-mercado.md`, con el 21 % de IVA y un 2,5 % de pasarela)

| Producto | PVP | Margen neto por pedido | **CPA de equilibrio** | **ROAS de equilibrio** | CPA objetivo (≈70 % del margen) |
|---|---|---|---|---|---|
| Lámpara bola 3D | 24,90 € | ≈ 11,2 € | 11,2 € | **2,2** | ≤ 8 € |
| Pack 2 lámparas | 39,90 € | ≈ 14,4 € | 14,4 € | **2,8** | ≤ 10 € |
| Reloj LED 3D | 29,90 € | ≈ 14,5 € | 14,5 € | **2,1** | ≤ 10 € |
| Globo que levita | 129 € | ≈ 34 € | 34 € | **3,8** | ≤ 24 € |
| Proyector de ondas | 29,90 € | *(calcular con la fórmula)* | | | |

**Fórmulas** (apúntalas):
- **Margen neto** = PVP ÷ 1,21 − coste del producto con su envío − 2,5 % del PVP.
- **CPA de equilibrio** = margen neto. Por encima de esa cifra, cada venta pierde dinero.
- **ROAS de equilibrio** = PVP ÷ margen neto.
- **CPA objetivo** = margen × 0,7. Así queda un 30 % de beneficio real por venta.
- **Si se usa HOLA10:** el margen baja un 10 % del PVP sin IVA (la lámpara queda en unos 9,1 €).

### 2.2 Qué implica

- **La lámpara y el reloj** son los productos para **empezar en pago**: margen fino, pero ROAS de equilibrio bajo y compra por impulso.
- **El globo** es una pieza para **llamar la atención**. En pago necesita un ROAS de 3,8, así que se prueba cuando ya haya datos y con su propia campaña.
- **El envío gratis desde 39 €** anima a comprar dos. El **valor medio del pedido** es la palanca más rentable: cada euro de más en el carrito no cuesta publicidad extra.

---

## 3. Estructura de la cuenta

Menos campañas y más presupuesto por conjunto. Meta necesita **unas 50 compras por semana en un conjunto de anuncios** para salir de la fase de aprendizaje. Si repartes el dinero en muchos conjuntos, ninguno aprende.

```
CUENTA ORBILUZ
│
├── 1. PRUEBA DE CREATIVIDADES (ventas · CBO · 1 conjunto amplio)       ← 60-70 % del presupuesto al inicio
│      Anuncios: 3-5 conceptos distintos (p. ej. A1, A2, A4, A6)
│
├── 2. ESCALADO: Advantage+ de ventas (ASC) con los anuncios ganadores   ← se abre cuando hay 2-3 ganadores
│
└── 3. RETARGETING / CATÁLOGO (ventas · anuncios de catálogo Advantage+)  ← 10-20 % del presupuesto; desde el día 14
```

**Configuración base de la campaña de prueba:**

| Campo | Valor |
|---|---|
| Objetivo | **Ventas** |
| Evento de conversión | **Compra (Purchase)**, píxel de Orbiluz |
| Presupuesto | **Presupuesto de campaña (CBO)**: 20-30 €/día al inicio |
| Atribución | 7 días tras el clic y 1 día tras la visualización (la estándar) |
| Público | **Amplio**: España, 18-55 años, todos los sexos, sin intereses. La creatividad hace la segmentación |
| Ubicaciones | **Advantage+** (automáticas). Cada anuncio lleva la versión 4:5 para el feed y la 9:16 para Historias y Reels («Personalizar recurso por ubicación») |
| Idioma | Español |
| Destino | La **ficha del producto**, no la portada |
| Mejoras creativas automáticas de Meta | **Desactiva** las que añaden texto, música o cambian la imagen, para mantener la marca. Deja «ajustar brillo y contraste» si quieres |

> **Por qué un público amplio:** con el píxel y la API de conversiones bien configurados, Meta encuentra al comprador mejor que los intereses manuales. Tu trabajo es la **creatividad** (quién se para a mirar) y la **ficha** (quién compra).

---

## 4. Guion paso a paso: del día 0 al día 30

### Día 0: lanzamiento

1. **Campaña «PRUEBA · Lámpara · Ventas»**, con la configuración del punto 3.
   - **Presupuesto:** 25 €/día. Con un CPA objetivo de unos 8 €, deberían salir unas 3 compras al día si funciona.
2. **Un conjunto de anuncios amplio** con **4 anuncios**, uno por concepto (no variantes del mismo):
   - **A1** «El regalo que sí sorprende»: regalo.
   - **A2** «Apaga la luz. Enciende un planeta»: ambiente.
   - **A4** «Tu dormitorio por la noche»: problema → solución.
   - **A6** «¿Cuál es el tuyo?»: elección.
3. **Cada anuncio:** la imagen 4:5 y la 9:16, un texto principal, un titular y el CTA «Comprar». Los textos están en el apartado 7.
4. **Parámetros de URL** para verlos en Shopify: `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`.
5. **Publicar y NO TOCAR** durante 72 horas. Cada cambio reinicia el aprendizaje.

### Días 1 a 3: observar sin tocar

**Revisar una vez al día**, sin cambiar nada:
- ¿Se entregan los anuncios?
- ¿Llegan los eventos?
- ¿El CTR del enlace pasa del 1 %?
- ¿Hay añadidos al carrito?

**Única excepción:** un anuncio con un error evidente (enlace roto o imagen mal recortada) se corrige.

### Días 4 y 5: primera criba

Aplica las **reglas del apartado 5**:
- Apaga los anuncios que hayan gastado **1,5 veces el CPA de equilibrio sin ninguna compra** (lámpara: unos 17 €) **y** que además tengan un CTR del enlace bajo (menos del 0,8 %).
- Deja los que tengan compras o señales fuertes: CTR alto y añadidos al carrito.
- Si **ninguno** tiene señales, el problema no es el anuncio sino la **ficha o la oferta**. Revisa el apartado 11 antes de lanzar más anuncios.

### Días 6 a 10: segunda tanda de creatividades

- **Añade 2-3 anuncios nuevos** al mismo conjunto:
  - **Variantes del ganador:** mismo concepto, otro titular u otra escena (se hacen con `make_ads.py`, sin coste de IA).
  - **Un concepto totalmente nuevo** (apartado 6).
- **Mantén siempre entre 3 y 6 anuncios activos** en la prueba.

### Días 10 a 14: abrir el escalado

Cuando **2-3 anuncios** tengan un CPA por debajo del objetivo con **al menos 5 compras cada uno**:
1. Crea **«ESCALA · Lámpara · ASC»**, una campaña Advantage+ de ventas.
   - **Presupuesto:** el mismo que la prueba.
   - **Anuncios:** los ganadores. Usa el **mismo ID de publicación** («Usar publicación existente») para conservar los «me gusta» y los comentarios.
2. **La prueba sigue viva**, con menos presupuesto (15-20 €/día), para seguir buscando el siguiente ganador.

### Días 14 a 21: retargeting y catálogo

- Crea **«RETARGETING · Catálogo»** (apartado 8), con un 10-20 % del gasto total.
- **Excluye a los compradores de los últimos 30 días** en todas las campañas de adquisición.

### Días 21 a 30: escalar con cuidado

- **Sube el presupuesto un 20 % cada 48-72 horas** en las campañas cuyo CPA de los últimos 3 días esté por debajo del objetivo.
- **Nunca más de un 20-30 % de golpe:** una subida grande reinicia el aprendizaje.
- **Si el CPA sube durante 3 días seguidos:** vuelve al último presupuesto estable y refresca las creatividades.
- **Prueba el globo** (solo si la lámpara ya es rentable):
  - Campaña aparte con A5 «¿Cómo está flotando?».
  - 30 €/día y CPA objetivo de 24 €.
  - Paciencia: al ser caro, tarda más en juntar compras.

---

## 5. Reglas de decisión

Se decide con datos de **al menos 3 días** y siempre mirando el **CPA frente al margen**, no los clics.

| Situación | Acción |
|---|---|
| Gasto ≥ 1,5 × CPA de equilibrio, **0 compras** y CTR del enlace < 0,8 % | **Apagar** |
| Gasto ≥ 1,5 × CPA de equilibrio, 0 compras, pero CTR > 1,5 % y añadidos al carrito | **Mantener 2 días más**. El problema puede estar en la ficha: revisar el apartado 11 |
| CPA ≤ objetivo con ≥ 3 compras | **Ganador provisional**: crear 2 variantes |
| CPA ≤ objetivo con ≥ 5 compras | **Ganador**: pasar a la campaña de escalado |
| CPA entre el objetivo y el equilibrio | **Mantener**; probar otro titular o texto |
| CPA > equilibrio durante 3 días | Bajar presupuesto o apagar ese anuncio |
| Frecuencia > 3 en 7 días y el CTR cayendo | **Fatiga**: meter creatividades nuevas |
| Coste por añadir al carrito bajo, pero muy pocas compras | Problema de pago o de confianza: revisar envío, métodos de pago y políticas |

**Señales guía** (lectura orientativa; lo que manda es el CPA):
- **Hook rate** (solo vídeo: reproducciones de 3 s ÷ impresiones) ≥ 25-30 %.
- **CTR del enlace** ≥ 1-1,5 %.
- **CPC del enlace** ≤ 0,50-0,70 €.
- **Añadir al carrito ÷ clics** ≥ 8-10 %.
- **Tasa de conversión de la web** ≥ 1,5-2,5 %.

> Los umbrales son puntos de partida, no cifras del sector garantizadas. Ajústalos con tus propios datos a partir de la tercera semana.

---

## 6. Sistema de creatividades

La creatividad es el **factor que más influye** en el resultado. La regla: **conceptos distintos para encontrar ganadores; variantes solo del ganador**.

### 6.1 Matriz de conceptos (ya tienes 6 hechos en esta carpeta)

| Concepto | Ángulo | Archivo | Producto |
|---|---|---|---|
| El regalo que sí sorprende | Regalo con efecto «wow» | A1 | Lámpara |
| Apaga la luz. Enciende un planeta | Ambiente | A2 | Lámpara |
| Para quien ya lo tiene todo | Regalo de temporada | A3 | Lámpara (desde noviembre) |
| Tu dormitorio por la noche | Problema → solución | A4 | Lámpara |
| ¿Cómo está flotando? | Curiosidad | A5 | Globo |
| ¿Cuál es el tuyo? | Elección | A6 | Lámpara |

**Conceptos siguientes** (por orden de prioridad):
1. **Escala real:** una mano junto a la bola para que se vea que es mini. Reduce devoluciones y aumenta la confianza.
2. **Mesilla vacía frente a mesilla con lámpara** (otra variante del antes y después).
3. **«Para tu pareja»**, pensado para San Valentín y aniversarios.
4. **Reloj LED 3D:** «Tu cuarto gamer necesitaba esto».
5. **Proyector:** «Apaga la luz. Enciende el mar».

### 6.2 Formatos a probar (por este orden)

1. **Imagen estática 4:5 + 9:16:** lo más barato de producir. Es lo que tienes ya.
2. **Carrusel:** los 4 modelos de lámpara (A6) o «4 motivos para regalarla».
3. **Vídeo corto de 6-15 s grabado por ti con el móvil:**
   - apagar la luz y encender la lámpara;
   - la mano con la bola;
   - el unboxing.
   El vídeo real y hecho a mano suele superar a la animación generada.
4. **Anuncios de catálogo Advantage+** (retargeting, apartado 8).

### 6.3 Producción de variantes (sin coste)

- Los titulares se cambian en `anuncios/meta/make_ads.py`. Se reutilizan las escenas de `escenas/`, así que no hace falta generar imágenes nuevas.
- **Variantes útiles:**
  - otro titular con el mismo ángulo;
  - otro color de resalte;
  - la palabra clave arriba o abajo;
  - otro recorte de la escena.
- **Solo se genera una escena nueva** (unos 2 créditos en Higgsfield) cuando se prueba un **concepto nuevo**.

### 6.4 Ritmo de producción

- **Fase de prueba:** 2-3 creatividades nuevas por semana.
- **Fase de escalado:** 3-5 por semana, para no fatigar a la audiencia.

---

## 7. Textos del anuncio (plantillas, sin precios)

**Estructura del texto principal:** gancho (1 línea) → beneficio → detalle que da confianza → CTA suave.

| Ángulo | Texto principal | Titular | Descripción |
|---|---|---|---|
| Regalo | «¿Buscas un regalo que de verdad sorprenda? Una bola de cristal con un planeta grabado por láser que se ilumina con luz cálida. De las que no acaban en un cajón.» | El regalo que sí sorprende | Orbiluz · decoración que se enciende |
| Ambiente | «Apaga la luz del techo y deja que un planeta ilumine tu habitación. Luz cálida y suave, perfecta para desconectar antes de dormir.» | Enciende un planeta | Envío con seguimiento |
| Problema | «La luz del techo por la noche es fría y demasiado fuerte. Cámbiala por una luz cálida que además decora.» | Tu dormitorio, con otro ambiente | 14 días para devolver |
| Elección | «Saturno, la Luna, una galaxia o el sistema solar. ¿Cuál pondrías en tu mesilla?» | ¿Cuál es el tuyo? | Orbiluz |
| Curiosidad (globo) | «Flota, gira y se ilumina. Un globo terráqueo que levita gracias a la levitación magnética. La pieza que todo el mundo pregunta.» | ¿Cómo está flotando? | Envío gratis con seguimiento |

**Reglas del texto:**
- Frases cortas y tuteo.
- Máximo 2-3 emojis.
- Nada de mayúsculas gritando.
- **Ni urgencias falsas ni escasez inventada** («últimas unidades» solo si es verdad).
- Nada de «el más vendido» sin datos.

**Varios textos:** usa la opción «Añadir opciones de texto» (hasta 5 textos principales y 5 titulares por anuncio). Meta combina los que mejor funcionan.

---

## 8. Retargeting y catálogo

**Cuándo:** desde el día 14, o cuando la web supere unas 1.000 visitas al mes.

| Público (personalizado, desde el píxel) | Ventana | Mensaje |
|---|---|---|
| Añadió al carrito sin comprar | 14 días | Recordatorio del producto que dejó y garantías (envío con seguimiento, 14 días para devolver) |
| Vio el producto sin añadirlo | 30 días | Otro ángulo del mismo producto, o los 4 modelos |
| Interactuó con Instagram o Facebook | 30 días | Presentación de la marca y el mejor anuncio |
| **Excluir:** compradores | 30 días | — |

- **Formato recomendado:** **anuncios de catálogo Advantage+** («Ventas → Catálogo»). Muestran a cada persona el producto que vio.
- **Plantilla del catálogo:** usa marcos con el logo de Orbiluz y **sin precio superpuesto**, que va con tu norma. Meta enseña el precio del catálogo en la ficha, no en la imagen.
- **Presupuesto:** un 10-20 % del gasto total. Si la frecuencia pasa de 4 en 7 días, bájalo.

---

## 9. Temporadas: Black Friday, Navidad y Reyes

| Fecha | Qué hacer |
|---|---|
| Hasta el 31 de octubre | Encontrar 2-3 ganadores con presupuesto de prueba. **Es la fase más importante:** en temporada alta el CPM se encarece |
| 1-20 de noviembre | Activar A3 «Para quien ya lo tiene todo» y otros conceptos de regalo. Subir presupuesto un 20 % cada 2-3 días |
| Black Friday (27-11-2026) y Cyber Monday | Si decides hacer oferta, anúnciala en la **ficha y el carrito**, no en la creatividad (norma: sin precios en anuncios). Duplica los ganadores con el texto «Black Friday en Orbiluz» |
| **Fecha límite de pedido** (plazo máximo del proveedor + 1-3 días de preparación, en días laborables, descontando festivos) | **Para Navidad (24-12):** lámpara y proyector antes del **1-12**; globo antes del **26-11**; reloj antes del **24-11**. **Para Reyes (5-01):** lámpara y proyector antes del **13-12**; globo antes del **8-12**; reloj antes del **2-12**. Ponlo en la ficha y en el texto del anuncio desde mediados de noviembre. Pasada la fecha, cambia el mensaje a «para ti» o «regalo para después de fiestas» |
| 26-12 a 6-01 | Mensaje de autorregalo y de «nuevo año, nueva habitación» |

**Aviso:** no prometas «llega para Navidad» si el plazo del proveedor no lo garantiza.

---

## 10. Rutina diaria y semanal

**Cada día (10-15 min):**
1. Gasto de ayer frente a ventas en Shopify (con UTMs).
2. CPA de cada anuncio y conjunto frente al objetivo.
3. Frecuencia y comentarios. Responde a los comentarios en menos de 24 h; eso ayuda al anuncio.
4. Apunta los números en la plantilla (apartado 14).
5. **Cambios solo según las reglas del apartado 5**, nunca por intuición ni por un mal día suelto.

**Cada semana (lunes, 30-45 min):**
1. ROAS y beneficio real de la semana: ventas − coste de producto − publicidad − comisiones.
2. Ranking de anuncios por CPA. ¿Qué ángulo gana?
3. Encargar 2-5 creatividades nuevas con el ángulo ganador y 1 concepto nuevo.
4. Revisar la ficha según el apartado 11: ¿dónde abandonan?
5. Decidir el presupuesto de la semana (escalar, mantener o recortar).

---

## 11. La ficha de producto también es parte del anuncio

Si hay clics pero no hay compras, el problema está aquí:
- [ ] **Primera foto** = la misma escena que el anuncio (continuidad). Segunda foto: tamaño real.
- [ ] **Precio y envío visibles** sin hacer scroll en el móvil.
- [ ] **Qué incluye y qué no** (cargador) y el **tamaño de 5 cm** bien claros. Menos devoluciones y más confianza.
- [ ] **Plazo de entrega honesto** (6-12 días laborables) y «envío con seguimiento».
- [ ] **Garantías visibles:** 14 días para devolver, pago seguro, atención en español.
- [ ] **Botones de pago rápido** (Apple Pay, Google Pay, Shop Pay) debajo de «Añadir al carrito».
- [ ] **Velocidad:** la ficha carga en menos de 3 s en el móvil (compruébalo con PageSpeed Insights).
- [ ] **Subir el valor del pedido:**
  - «Añade otra lámpara y el envío es gratis» (umbral de 39 €);
  - en el carrito, sugerir un segundo modelo.
- [ ] **Reseñas:** solo **reales**. Cuando lleguen los primeros pedidos, pide la opinión por correo 10 días después de la entrega con una app de reseñas y enséñalas en la ficha.

---

## 12. Errores que más dinero cuestan

1. **Tocar la campaña cada día** (presupuesto, público, anuncios). Cada cambio grande reinicia el aprendizaje.
2. **Demasiados conjuntos con poco dinero.** Mejor 1 conjunto con 25 € que 5 conjuntos con 5 €.
3. **Juzgar por los clics o las visualizaciones** en lugar del CPA frente al margen.
4. **Intereses muy estrechos.** Con el píxel funcionando, lo amplio suele ganar.
5. **Escalar a lo bruto** (duplicar el presupuesto de golpe).
6. **No excluir a los compradores** de las campañas de adquisición.
7. **Mandar el tráfico a la portada** en lugar de a la ficha del producto.
8. **Quemar un ganador por fatiga** sin tener el relevo preparado.
9. **Prometer lo que no controlas:** plazos para Navidad, «últimas unidades» o reseñas que no existen. Aparte del problema legal (Ley de Competencia Desleal), dispara las devoluciones y los comentarios negativos.

---

## 13. Nomenclatura

`[FASE] · [PRODUCTO] · [OBJETIVO] · [FECHA]`, por ejemplo:
- Campaña: `PRUEBA · Lampara · Ventas · 2026-10`
- Conjunto: `Amplio ES 18-55 · Advantage+`
- Anuncio: `A1-regalo-mano · T1` (T1, T2… = versión del texto)

---

## 14. Plantilla de seguimiento (copiar a una hoja de cálculo)

| Fecha | Campaña | Anuncio | Gasto | Impresiones | CTR enlace | CPC | Añadidos al carrito | Compras | Ingresos | CPA | ROAS | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

**Beneficio real semanal:** ingresos ÷ 1,21 − coste de producto y envío − gasto en publicidad − comisiones de pago − devoluciones.

---

### Resumen en una línea

**Mide bien → prueba 4 conceptos distintos con un público amplio → no toques en 72 h → apaga por CPA → itera sobre el ganador → escala un 20 % cada 2-3 días → retargeting con catálogo → prepara la temporada antes de noviembre.**
