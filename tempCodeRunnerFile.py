num = int(input("Ingrese un número positivo"))

if num < 0:
    input("Número ingresado inválido")
else:
    for i in range(1, num, 2):
        print(i)