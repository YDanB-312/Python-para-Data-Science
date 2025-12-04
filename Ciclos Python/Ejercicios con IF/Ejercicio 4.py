"""¿Para que siorve Length?: Length es una función en Python
que se utiliza para obtener la longitud (el número de elementos) de un objeto, como una cadena de texto, una lista, una tupla, un diccionario, entre otros.
Se utiliza comúnmente para contar cuántos caracteres hay en una cadena o cuántos elementos hay en una colección."""
#Se solicita al usuario que ingrese una contraseña.
constraseña = input("Ingresa la contrsaseña: ")

#Se verifica si la longitud de la contraseña es mayor o igual a 8 caracteres y si lo es se muestra un mensaje indicando que la contraseña es segura.
if len(constraseña) >= 8:
    print("Contraseña segura.")