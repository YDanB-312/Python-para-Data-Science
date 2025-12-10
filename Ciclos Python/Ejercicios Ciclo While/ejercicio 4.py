contador = 0
resultado = 0

numero = int(input("Ingrese un numero: "))

while contador <= 10:
    resultado = numero * contador
    print(numero, "*", contador, "=", resultado)
    contador += 1
    
    
print("El resultado de la tabla de multiplicar es: ", resultado)

