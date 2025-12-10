numeros = []
suma = 0

for i in range(5):
    numero = float(input("Ingrese un numero: "))
    numeros.append(numero)

for n in numeros:
    suma += n

print("La suma de los numeros es: ", suma)