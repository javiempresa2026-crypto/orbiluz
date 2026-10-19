#!/usr/bin/env python3
"""Calculadora de margen y CPA de equilibrio para Orbiluz.

Margen neto = PVP sin IVA (con descuento) − coste del producto − envío del proveedor − comisión de pago.
CPA de equilibrio = margen neto (por encima, cada venta pierde dinero).
CPA objetivo = 70 % del margen. ROAS de equilibrio = PVP cobrado ÷ margen.

Uso:
  python3 margen.py --todos [--descuento 15] [--cambio 1.17]
  python3 margen.py --pvp 24.90 --coste-usd 7.72 --envio-usd 1.99 [--unidades 2 --pvp-total 39.90]
"""
import argparse

# Costes de proveedor (DSers/AliExpress, 29-09-2026). Revisar si cambian.
PRODUCTOS = {
    "Lámpara bola de cristal": dict(pvp=24.90, coste_usd=7.72, envio_usd=1.99),
    "Proyector de ondas": dict(pvp=29.90, coste_usd=11.18, envio_usd=1.99),
    "Reloj LED 3D": dict(pvp=29.90, coste_usd=8.07, envio_usd=1.99),
    "Globo que levita": dict(pvp=129.00, coste_usd=47.43, envio_usd=27.58),
}
IVA = 0.21


def calcula(pvp, coste_usd, envio_usd, cambio, comision, descuento=0.0, unidades=1, pvp_total=None):
    cobrado = pvp_total if pvp_total is not None else pvp * unidades * (1 - descuento / 100)
    sin_iva = cobrado / (1 + IVA)
    coste = (coste_usd + envio_usd) * unidades / cambio
    margen = sin_iva - coste - cobrado * comision / 100
    return dict(cobrado=cobrado, sin_iva=sin_iva, coste=coste, margen=margen,
                cpa_obj=margen * 0.7, roas_eq=(cobrado / margen) if margen > 0 else float("inf"))


def fila(nombre, r):
    aviso = "  ⚠ margen negativo" if r["margen"] <= 0 else ("  ⚠ poco margen para anuncios" if r["cpa_obj"] < 8 else "")
    print(f"{nombre:<28} cobrado {r['cobrado']:7.2f} € | sin IVA {r['sin_iva']:7.2f} € | coste {r['coste']:6.2f} € | "
          f"margen {r['margen']:6.2f} € | CPA obj. {r['cpa_obj']:6.2f} € | ROAS eq. {r['roas_eq']:4.1f}{aviso}")


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--todos", action="store_true", help="calcula los productos actuales de la tienda")
    a.add_argument("--pvp", type=float)
    a.add_argument("--coste-usd", type=float)
    a.add_argument("--envio-usd", type=float, default=0.0)
    a.add_argument("--unidades", type=int, default=1)
    a.add_argument("--pvp-total", type=float, help="precio total cobrado si es un pack (p. ej. 39.90 por 2)")
    a.add_argument("--descuento", type=float, default=0.0, help="porcentaje de descuento (15 = −15 %%)")
    a.add_argument("--cambio", type=float, default=1.17, help="dólares por euro (revisa el del día)")
    a.add_argument("--comision", type=float, default=2.5, help="comisión de pago en %% (estimación)")
    o = a.parse_args()
    print(f"Supuestos: IVA 21 % incluido en el PVP · 1 € = {o.cambio} $ · comisión {o.comision} % · descuento {o.descuento} %\n")
    if o.todos:
        for n, d in PRODUCTOS.items():
            fila(n, calcula(d["pvp"], d["coste_usd"], d["envio_usd"], o.cambio, o.comision, o.descuento))
        l = PRODUCTOS["Lámpara bola de cristal"]
        fila("2 lámparas por 39,90 €", calcula(l["pvp"], l["coste_usd"], l["envio_usd"], o.cambio, o.comision, unidades=2, pvp_total=39.90))
    elif o.pvp and o.coste_usd is not None:
        fila("Producto", calcula(o.pvp, o.coste_usd, o.envio_usd, o.cambio, o.comision, o.descuento, o.unidades, o.pvp_total))
    else:
        a.print_help()


if __name__ == "__main__":
    main()
