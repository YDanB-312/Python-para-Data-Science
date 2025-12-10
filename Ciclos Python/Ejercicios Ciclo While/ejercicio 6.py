totalVentas = 0
cantidadVentas = 0

print("Ingrese 0 para inicializar")

venta = float(input("Ingrese el monto de la venta: "))

while venta != 0:

    if venta < 0:
        print("Error: el monto no puede ser negativo.")
    else:
        totalVentas += venta
        cantidadVentas += 1
        print(f"Venta registrada. Total del día: ", totalVentas)

    venta = float(input("Ingresa el monto de la venta: $"))

print("\nResumen del día:")
print("Total de ventas:", cantidadVentas)
print(f"Dinero recaudado: $", totalVentas)