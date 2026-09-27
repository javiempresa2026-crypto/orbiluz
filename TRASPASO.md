# Orbiluz: traspaso para el chat nuevo

## ⚡ Estado a 27-09-2026 (última sesión)

### Tienda y conexiones
- **Tienda:** atzezc-eb.myshopify.com (dominio de Shopify: orbiluz.myshopify.com).
  - Plan de prueba y con contraseña.
  - El nombre sigue siendo «My Store 3»: lo cambia el usuario en el panel.
- **Correo de la tienda:** orbiluzsupport@gmail.com. Lo pone el usuario en Configuración → Detalles de la tienda.
- **DSers:** conectado (dsers_store_id 2103839554244116480). Los 3 productos están vinculados a AliExpress.

### Productos (activos)
| Producto | Handle | ID | Precio | Proveedor |
|---|---|---|---|---|
| Proyector de ondas de agua | `proyector-ondas-de-agua` | 10305883111752 | 29,90 € | 1005009888234857 |
| Lámpara bola de cristal 3D (4 modelos) | `lampara-bola-cristal-3d` | 10305883078984 | 24,90 € | 1005008323008233 |
| Reloj LED 3D, solo variante negro y luz blanca | `reloj-led-3d` | 10305883013448 | 29,90 € | 1005007090990814 (variante 04) |

### Hecho en Shopify
- **Colecciones:** Lámparas, Relojes y Todos los productos (automáticas por tipo o marca).
- **Páginas:** contacto, preguntas-frecuentes, politica-de-cookies y sobre-orbiluz.
- **Menús:**
  - Principal: Inicio, Lámparas, Relojes, Todo, Preguntas frecuentes, Contacto.
  - Pie: Sobre Orbiluz, Preguntas frecuentes, Contacto, Política de cookies, Buscar.
- **Descuentos:**
  - HOLA10: 10 %, un uso por cliente.
  - Automático: 2 lámparas bola por 39,90 € (−9,90 € a partir de 2 unidades).
- **Envíos:** solo España peninsular y Baleares. 3,95 € por debajo de 39 € y gratis desde 39 €.
- **Tema «Orbiluz 1.0»** (Horizon 4.2), ya publicado por el usuario:
  - Portada propia en `sections/orbiluz-home.liquid`.
  - CSS de marca y fuente Unbounded como recurso del tema.
  - Cabecera con 3 anuncios y pie con enlaces.
  - Los archivos están en `orbiluz/tema/`.
  - **Para editar un tema publicado** hay que duplicarlo, porque la API bloquea escribir en el tema MAIN.
  - **Para subir archivos grandes:** `stagedUploadsCreate` (FILE, PUT con curl) y después `themeFilesUpsert` con body type URL.

### Pendiente
- **Del usuario:**
  - Pegar las políticas desde `orbiluz/politicas-para-pegar.html`. La API no tiene permiso para escribirlas.
  - Poner el español como idioma principal (ya está activado como secundario).
  - Cambiar el nombre de la tienda.
  - Activar la pasarela de pago y el banner de cookies.
  - Elegir plan, quitar la contraseña y comprar orbiluz.com.
- **Revisar la tienda visualmente** cuando el usuario pase la contraseña de la tienda.
- **Aviso legal:** conviene añadir el nombre y el NIF del titular cuando sea autónomo.

## Encargo del usuario (literal, resumido)
- Estudio de mercado con datos.
- Buscar en DSers productos de **decoración del hogar llamativos y originales**: tipo lámpara de Saturno, relojes con alguna novedad, o relacionados del sector.
- Público: **18-50 años, hombres y mujeres**.
- Crear **otra tienda Shopify aparte** con **2-3 productos**, todo listo:
  - bases legales, política de privacidad, etc.;
  - **nombre en español, corto, con .com libre**;
  - logotipo, paleta y tipografía;
  - **fotos sin marcas de agua que no parezcan de AliExpress** (creadas o retocadas);
  - UX fácil e intuitiva;
  - **código de descuento en la primera compra** y **envío gratis a partir de X €** (precios a criterio);
  - cualquier otra cosa conveniente para dejarla lista.
- Al final, enviar las **direcciones de los proveedores** para enlazarlos en DSers, con stock suficiente y todas las características.
- **El dominio lo compra el usuario al final**, cuando esté todo hecho.

## Nombre: Orbiluz ✅
- «Órbita + luz». Español, 7 letras.
- **orbiluz.com libre** (16 $/año; comprobado con la herramienta de dominios de Shopify y por RDAP de Verisign el 26-09-2026).
- Otros .com libres de reserva: kosmilo.com, lunarce.com, orbuzo.com, vayolo.com.

## Marca (hecha: `orbiluz/marca/`)
- `generar_marca.py` genera `logo/*.svg|png` (noche, luna, blanco, negro, icono y avatar) y `hoja-de-marca.png|html`.
- Paleta:

  | Color | Código |
  |---|---|
  | Noche | #12123A |
  | Ámbar | #FFB547 |
  | Nebulosa | #7C6CF6 |
  | Luna | #FFF6E9 |
  | Coral | #FF7A59 |
  | Niebla | #A7A9C9 |

- Tipografía: **Unbounded** (titulares) y **DM Sans** (texto), de Google Fonts con licencia OFL. Están en `marca/fuentes/`.
- Tono: cercano, curioso, con humor, tuteo.

## Productos elegidos (DSers → AliExpress, `supplier_platform_id` 159831080). Envío a ES con seguimiento
| # | Producto | ID proveedor | Coste unidad | Envío ES | Plazo | Pedidos / nota | Stock | PVP propuesto |
|---|---|---|---|---|---|---|---|---|
| 1 | **Lámpara bola de cristal 3D** (Saturno, galaxia, luna, sistema solar). Esfera de 5 cm grabada por láser, base de madera de 2 cm, cable USB. Caja 13×9×6 cm, 229 g | 1005008323008233 · https://www.aliexpress.com/item/1005008323008233.html | 7,58-7,85 $ | 1,99 $ «AliExpress Selection Premium» | 6-12 días | 5.000+ / 4,6 ★ | Saturno 73, Luna 67, Sistema solar 68, Galaxia 43 (**poco**: vigilar o buscar un segundo proveedor) | 24,90 € (2 por 39,90 €) |
| 2 | **Reloj LED 3D de pared o mesa**: dígitos flotantes, hora, alarma, modo noche, 3 niveles de brillo. 16,3×6×1,65 cm, 132 g | 1005007090990814 · https://www.aliexpress.com/item/1005007090990814.html | 8,33 $ (variante «04», marco negro y luz blanca) | 1,99 $ | 8-17 días | 10.000+ / 4,3 ★ | **Variante 04: 20.634** (el resto tiene poco stock; ofrecer solo la 04 y quizá la 01, con 197) | 29,90 € |
| 3 | **Mini reloj WiFi con el tiempo** (cubo con pantalla IPS a color: hora, fecha, temperatura, humedad y tiempo de tu ciudad). 10×6×4 cm con caja, 65 g. Marca del fabricante: GeekMagic | 1005006728045097 · https://www.aliexpress.com/item/1005006728045097.html | 13,86 $ (negro o blanco) | 1,99 $ | 6-12 días | 10.000+ / 4,7 ★ | Negro 264, blanco 113 (el resto de colores tiene menos de 35) | 34,90 € |

**Descartados:**

| Producto | Motivo |
|---|---|
| Lámpara «sunset» | Diminuta (28 g), barata y saturada |
| Saturno 3D de 1688 | 47-53 $, sin envío claro a ES |
| Proyectores de galaxia | Mucha competencia |
| Colgante Saturno | 90 $ |

**Márgenes aproximados** (1 $ ≈ 0,92 €, comisión de pago aproximada 2,5 %):

| Producto | Coste | Margen bruto |
|---|---|---|
| Lámpara | ~8,9 € | ~15 € |
| Reloj 3D | ~9,5 € | ~19 € |
| Reloj WiFi | ~14,6 € | ~19 € |

**Propuesta:** envío gratis desde **39 €** (así se compran 2 lámparas o se combinan productos). Código **HOLA10** (-10 % en el primer pedido, un uso por cliente).

## Fotos del proveedor (descargadas y probadas)
- URLs en la ficha de cada producto con `get_supplier_product`.
- Se probó `rembg` (modelo isnet-general-use) para recortar el producto: funciona bien con la bola, los dos relojes y el cubo.
- **Plan:** recortar y componer en «estudio» (fondos de la marca, sombra, brillo o ambiente nocturno) con Pillow y Playwright, para que no parezcan de AliExpress. Es el producto real, sin inventar características.
- En la pantalla del reloj WiFi se puede poner «Madrid» (la ciudad es configurable).
- Kling: solo quedan 8 créditos, así que no hay IA de imagen (image_to_image cuesta 10).

## Pendiente
1. **Crear la tienda en Shopify.** Tiene que hacerlo el usuario: alta en Shopify con otro correo o con el mismo, y nombre «Orbiluz». Luego conectarla al conector de Shopify (herramienta `switch-shop`) y a DSers.
   - Sin la tienda, dejar preparado en `orbiluz/`: fichas (JSON), textos, políticas legales, tema (secciones y CSS) y fotos, listo para cargar.
2. Estudio de mercado en `orbiluz/estudio-mercado.md`, con datos de DSers (pedidos, valoraciones, stock, costes) y datos públicos de tendencia si hay acceso web.
3. Fotos de producto propias (3-5 por producto + banner principal).
4. Políticas: privacidad, devoluciones (14 días), envíos, términos, aviso legal y cookies.
   - Titular: particular (aún no es autónomo) · Granada, España · sin NIF.
   - Correo: el usuario tiene que dar uno. jarandanainfo@gmail.com es de la otra tienda.
   - Reutilizar como base `shopify/legal/politicas.json` del repo jarangana.
5. Descuento HOLA10, envío gratis desde 39 €, colecciones, menú, portada con hero, reseñas ocultas hasta tener reales, y ficha técnica.
6. Enviar al usuario los enlaces de proveedor para mapear en DSers.

## Reglas que el usuario ya pidió en la otra tienda (aplican aquí)
- No inventar datos, ni reseñas falsas, ni personas generadas por IA presentadas como clientes.
- Nunca guardar tokens en el repositorio.
- Todo en español de España, pensado para móvil y atractivo.
