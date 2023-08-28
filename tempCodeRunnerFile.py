nota1 = int(input("Ingrese la 1er nota: "))
nota2 = int(input("Ingrese la 2da nota: "))
nota3 = int(input("Ingrese la 3er nota: "))
nota4 = int(input("Ingrese la 4ta nota: "))
if (nota1 > 10 or nota2 > 10 or nota3 > 10 or nota4 > 10) or (nota1 < 0 or nota2 < 0 or nota3 < 0 or nota4 < 0):
    print("Alguna de las notas no es válida")
else:
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    if promedio >= 6 :
        print(f"Su promedio es de {promedio}")
        print("APROBADO")

    elif promedio < 6:
        print(f"Su promedio es de {promedio}")
        print("DESAPROBADO")