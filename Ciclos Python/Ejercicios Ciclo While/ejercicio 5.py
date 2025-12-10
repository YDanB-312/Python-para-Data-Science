"""Se declara lo necesario a utilizar"""
suma = 0
contador = 0
promedio = 0

#Se muestra un mensaje que le dice al usuario como inicializar el prmedio de los numeros ingresados
print("Ingrese 0 para mostrar el promedio de los numeros ingresados")

#Se le pide al usuario que ingrese un numero
numero = float(input("Ingrese un numero: "))

"""Mientras el numero ingresado sea diferente de 0 continuara agregando los numeros ingresados
a la varibale 'suma' mientras cuenta cuantos numeros se ingresaron con contador, se repite una y otra vez
hasta que el usuario ingrese 0 """
while numero != 0:
    suma += numero
    contador += 1
    numero = float(input("Ingrese otro numero: "))

if contador > 0:
    promedio = suma / contador
    print("El promedio de los numeros ingresados es: ", promedio)

else:
    print("No se ingresaron numeros: ")