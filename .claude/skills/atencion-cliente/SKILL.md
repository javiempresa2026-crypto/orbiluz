---
name: atencion-cliente
description: "Ayuda con la atención al cliente de Orbiluz: redactar respuestas a clientes (¿dónde está mi pedido?, devoluciones, producto roto o distinto, cobros), revisar si un pedido o cobro existe en Shopify y detectar correos sospechosos o estafas («me habéis cobrado y no tengo pedido», falsos avisos de pago o de Shopify). Úsala cuando el usuario reciba un mensaje o correo de un cliente o de un supuesto proveedor o plataforma, cuando pregunte «¿qué le contesto?» o «¿puede ser una estafa?», o cuando haya que gestionar una devolución o incidencia."
---

# Atención al cliente · Orbiluz

Una respuesta rápida, amable y con datos reales salva la venta y la reputación. **Primero se comprueba en Shopify y después se responde.**

## 1. Comprobar antes de responder

- **¿Existe el pedido o el cobro?** Busca en Shopify con `orders(query: "email:...")` o por nombre y número. Mira las transacciones (`transactions { kind status gateway }`) y los `abandonedCheckouts`.
  - **Shopify no cobra sin crear el pedido.** Si no hay pedido, no hubo cobro por la tienda.
  - Lo que el cliente ve puede ser una **retención temporal** de su banco tras un pago que no se completó. Se libera sola en unos días.
- **Seguimiento:** el pedido trae el seguimiento cuando DSers lo sincroniza. Si no aparece, pide al usuario que lo mire en DSers (el conector necesita el plan Advance).
- **Plazos reales:** preparación 1-3 días laborables más envío de 6-17 días laborables según el producto (el globo, 10-15). No prometas menos.

## 2. Señales de estafa (avisa al usuario antes de nada)

- **«Me habéis cobrado pero no tengo pedido»** y no hay ningún rastro en Shopify, sobre todo si pide **devolución por Bizum o transferencia**, fuera de Shopify.
- **Avisos «de Shopify», «de Meta» o «del banco»** que piden entrar en un enlace, descargar un archivo o «verificar» la cuenta. Comprueba el remitente real y el dominio de los enlaces. Los avisos de verdad aparecen también dentro del panel de Shopify o de Meta.
- **Prisa, amenazas** («te denuncio», «cierro tu cuenta hoy») o archivos adjuntos con «justificantes».

**Qué hacer:** no devolver dinero fuera de Shopify, no abrir enlaces ni adjuntos, y pedir datos concretos (fecha, importe, últimos 4 dígitos de la tarjeta y una captura del cargo donde se vea el comercio). Si al final es real, se gestiona desde el pedido en Shopify.

Si el usuario tiene Gmail conectado, puedes buscar el correo (ToolSearch «Gmail») para leerlo. **No respondas ni reenvíes nada sin su permiso.**

## 3. Devoluciones e incidencias

- **Desistimiento:** 14 días naturales desde que el cliente lo recibe, según la política de la tienda (`legal/` y la página de políticas de Shopify).
- **Producto roto o distinto:** pide una foto, y con la foto se reclama al proveedor en AliExpress o DSers. Al cliente se le ofrece reenvío o reembolso. Que no tenga que mandar el producto a China.
- **Reembolsos:** los hace el usuario desde el pedido en Shopify. El conector bloquea los reembolsos, y es mejor así.
- **Registro:** apúntalo en la hoja «Devoluciones» de `gestion/plantilla-registro-orbiluz.xlsx`. La copia con datos va en `gestion/datos/`, fuera de Git.

## 4. Cómo escribir la respuesta

- **Tono:** español de España, de tú, cercano y breve, con 3-6 frases.
- **Contenido:** dato concreto (estado, número de seguimiento o plazo), siguiente paso claro y firma «Equipo Orbiluz».
- **Sin promesas que no dependan de nosotros.** Sin excusas largas ni culpar al proveedor.
- **Entrega:** prepara el borrador para que lo envíe el usuario. Si pide que lo envíes tú, confírmalo antes.

**Plantilla de «¿dónde está mi pedido?»:**

> ¡Hola, [nombre]! Tu pedido [#número] salió el [fecha] y va con seguimiento: [enlace]. El plazo habitual es de [x-y] días laborables, así que debería llegarte entre el [fecha] y el [fecha]. Si ves cualquier cosa rara en el seguimiento, escríbenos y lo miramos al momento. ¡Gracias por tu paciencia! Equipo Orbiluz
