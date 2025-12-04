#Se solicita al usuario que ingrese el stock actual de un producto
stock = int(input("Ingrese el stock actual: "))

#Se verifica si el stock es menor a 5 unidades y si asi es se muestra un mensaje indicando que el stock es critico y se debe reabastecer urgente.
if stock < 5:
    print("Stock critico, reabastecer urgente.")