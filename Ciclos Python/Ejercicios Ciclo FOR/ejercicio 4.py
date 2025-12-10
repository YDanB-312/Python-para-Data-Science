inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))


for i in range(inicio, fin + 1):
    if i % 2 != 0:
        print(i)