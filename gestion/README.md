# Gestión: pedidos, clientes y proveedores

## Registro de pedidos y clientes
Plantilla: `plantilla-registro-orbiluz.xlsx`. Se regenera con `python3 gestion/generar_registro.py`.

| Hoja | Qué contiene |
|---|---|
| Resumen | Pedidos, ingresos, beneficio, margen, ROAS, carritos recuperados y devoluciones; desglose por producto y por origen |
| Pedidos | Una fila por producto vendido. El coste, la comisión, el beneficio y el margen se calculan solos |
| Clientes | Por email: nº de pedidos, total gastado, primer y último pedido |
| Carritos abandonados | Seguimiento de los 3 emails de recuperación y si acabaron en pedido |
| Devoluciones | Comprueba solo si la devolución está dentro de los 14 días |
| Parámetros | Coste de cada producto y comisión de pago (celdas amarillas) |

**RGPD:** la plantilla vacía está en el repositorio. La copia con datos de clientes guárdala en `gestion/datos/`: esa carpeta está excluida de Git, igual que los `.csv`. Nunca subas datos personales al repositorio.

Shopify ya guarda todo esto: Pedidos, Clientes y Pedidos › Carritos abandonados, y lo puedes exportar en CSV. Esta hoja sirve para ver el beneficio real.

## Proveedores y costes de envío (DSers, 29/09/2026)
| Producto | Proveedor | Coste | Envío a España | Plazo |
|---|---|---|---|---|
| Lámpara bola de cristal 3D | Global Night Light Store (AliExpress) | 7,59-7,85 USD | 1,99 USD | 5-9 días |
| Reloj LED 3D | Neat Life Store (AliExpress) | 7,51-8,62 USD | 1,99 USD | 5-9 días |
| Proyector de ondas | YOZHIXU Smart Life Store (AliExpress) | 11,18 USD | 1,99 USD | 5-9 días |
| Globo que levita | 1688 Dropshipping | 47,43 USD | 27,58 USD (envío especial por el imán) | 10-15 días |

Todos los envíos tienen seguimiento. Margen aproximado por unidad, sin IVA, antes de publicidad y con 1 € ≈ 1,17 USD (revísalo con el cambio del día):

| Producto | Margen aprox. |
|---|---|
| Lámpara | ~11 € |
| Pack de 2 lámparas | ~16 € |
| Reloj | ~15 € |
| Proyector | ~12 € |
| Globo | ~40 € |

El globo es el de mayor coste de envío. Si algún día subes el precio, empieza por ahí.

## Mensaje a los proveedores (envío sin publicidad)
En DSers, **Settings › Order › Supplier Order Message** (https://www.dsers.com/application/settings?type=Order_Setup#order_settings_44), pega este texto. Se añadirá a cada pedido:

```
This is a dropshipping order. Please DO NOT include invoices, prices, receipts, flyers, business cards, coupons or any promotional material or logo of your store. Use neutral packaging only. Thank you!
```

Envía también este mensaje una vez por el chat de cada tienda de AliExpress:

```
Hello! I will place regular dropshipping orders for my customers in Spain. Please ship every order in neutral packaging, without invoice, price tags, flyers or any promotional material or logo of your store. Can you confirm? Thank you!
```

El pedido de 1688 Dropshipping lo gestiona el agente de DSers, que envía con embalaje neutro. Compruébalo en el primer pedido.
