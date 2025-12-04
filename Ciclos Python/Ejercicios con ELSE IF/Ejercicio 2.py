#Se declaran las variables a utilizar
compra = float(input("Ingrese el valor de la compra: "))
descuento = 0
precioFinal = 0

#Se verifica en qué rango se encuentra el valor de la compra y se asigna el descuento correspondiente
if compra < 100000:
    descuento = 0
elif compra >= 100000 and compra < 500000:
    descuento = compra * 0.10
elif compra >= 500000:
    descuento = compra * 0.20