numero = 0
suma = 0

print("Ingrese un numero negativo para iniciar la suma.....")
numero = int(input("Ingrese un numero entero positivo: "))

while numero >= 0:
    suma += numero
    numero = int(input("Ingrese otro número: "))

print("La suma de los números ingresados es:", suma)