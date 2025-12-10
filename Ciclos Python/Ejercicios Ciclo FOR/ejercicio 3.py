frase = input("Ingrese una frase: ")

vocales = "aeiou"
contador = 0

for letra in frase.lower():
    if letra in vocales:
        contador += 1

print("La frase tiene ", contador, "vocales")        