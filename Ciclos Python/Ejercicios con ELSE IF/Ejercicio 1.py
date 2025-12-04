# Se crean las variables a utilizar
nota = float(input("Ingresa tu nota: "))

# Se declara la variable que tendrá la calificación
calificacion = ""

# Se verifica en qué rango se encuentra la nota y se asigna la calificación correspondiente
if nota >= 4 and nota <= 5:
    calificacion = "A"
elif nota >= 3.5 and nota <= 3.9:
    calificacion = "B"
elif nota >= 3 and nota <= 3.4:
    calificacion = "C"
else:
    calificacion = "D"