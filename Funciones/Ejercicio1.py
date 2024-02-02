def total_factura(cantidad_sin_iva, porcentaje_iva=21):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total = cantidad_sin_iva + iva
    return total

def main():
    cantidad_sin_iva = float(input("cantidad sin IVA: "))
    porcentaje_iva = float(input("porcentaje de IVA (opcional, Enter para aplicar el 21%): ") or 21)
    total = total_factura(cantidad_sin_iva, porcentaje_iva)
    print(f"El total de la factura es: {total}")

main()
