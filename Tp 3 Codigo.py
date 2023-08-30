#Ejercicio 1

palabra = input("Ingrese una palabra para repetirla: ")

for i in range(11):
    print(palabra)


#Ejercicio 2
edad = int(input("Ingrese su edad: "))

for i in range(edad):
    print(f"Viviste tu año {i +1}")


#Ejercicio 3
num = int(input("Ingrese un número positivo"))

if num < 0:
    input("Número ingresado inválido")
else:
    for i in range(1, num, 2):
        print(i)