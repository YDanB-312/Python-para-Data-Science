#Se declaran las variables a utilizar
talla = int(input("Ingresa tu talla (S, M, L, XL): "))
resultado = ""

#Se verifica la talla ingresada y se asigna el resultado correspondiente
if talla == 'S':
    resultado = "Talla pequeña(36-48)"
elif talla == 'M':
    resultado = "Talla mediana(40-42)"
elif talla == 'L':
    resultado = "Talla grande(44-46)"
elif talla == 'XL':
    resultado = "Talla extra grande(48-50)"
else:
    resultado = "Talla no valida"