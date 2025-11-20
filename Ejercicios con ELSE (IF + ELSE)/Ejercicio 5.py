#Se declaran las variables a utilizar.
edad = int(input("Ingresa tu edad: "))
tieneLicencia = input("¿Tienes licencia de conducir? (si/no): ")

#Se declara la variable que tendráel resultado.
puedeConducir = ""

#Se verifica si la edad es mayor o igual a 18 y si tiene licencia de conducir.
if edad >= 18 and tieneLicencia == "si":
    puedeConducir = "Puedes conducir."
else:
    puedeConducir = "No puedes conducir."
    
print(puedeConducir)