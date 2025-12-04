#Se solicita al usuario que ingrese el total de una compra.
totalCompra = float(input("Ingrese el total de la compora: "))

#Se verifica si el total de la compra es mayor a 10,000 y si lo es se muestra un mensaje indicando que obtiene un 10% de descuento.
if totalCompra > 10000:
    print("¡Felicidades! Obtienes un 10% de descuento.")