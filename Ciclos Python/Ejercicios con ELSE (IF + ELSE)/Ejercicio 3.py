#Le pide al usuario que ingrese si es un usuario premium
tipo_usuario = str(input("¿Usted es premium? (si/no): "))

#Verifica si el usuario es premium o no
if tipo_usuario.lower()=="si":
    print("acceso concecido")
else:
    print("acceso denegado")
    
    
    