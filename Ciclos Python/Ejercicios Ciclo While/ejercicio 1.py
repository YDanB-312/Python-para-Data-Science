#Declaro las variables a utilizar ademas de pedir un numero entero positivo por medio del teclado
numero = int(input("Ingrese un número: "))

#Se inicializa el contador en 1
contador = 1

#Mientras contador sea menor o igual al numero ingresado el 
while contador <= numero:
    print(contador)
    contador += 1