#Se declaran las variables a utilizar
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = 0
clasificacion = ""

#Se calcula el IMC y se clasifica según el valor obtenido
imc = peso / (altura * altura)

#Se verifica en qué rango se encuentra el IMC y se asigna la clasificación correspondiente
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc >= 18.5 and imc < 24.9:
    clasificacion = "Peso normal"
elif imc >= 25 and imc < 29.9:
    clasificacion = "Sobrepeso"
elif imc >= 30:
    clasificacion = "Obesidad"