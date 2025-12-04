# Se declaran las variables a utilizar
precio = float(input("Ingrese el precio del producto: "))
tienemembresia = input("¿El cliente tiene membresía? (si/no): ")
descuento = 0
precioFinal = precio

# Se realizan los caclulos del descuento
descuento = precio * 0.15
precio_con_descuento = precio - descuento

# Se verifica si el cliente tiene membresía y se aplica el descuento si es así
if tienemembresia == "si":
    precioFinal = precio_con_descuento
    
else:
    precioFinal = precio
    
# Se muestra el precio final al cliente
print(f"El precio final a pagar es: {precioFinal}")