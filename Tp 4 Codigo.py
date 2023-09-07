
#Ejercicio 2

balance = 0
logbook = "\n"
operation = "."
while operation != "":
    print("\n")
    operation = input("¿Qué operacion desea realizar? \n Deposito(D) --- Retiro(R).\n Para finalizar ingrese un espacio vacío: ")
    operation = operation.upper()
    if operation == "D":
        deposit = int(input("Ingrese el monto: "))
        logbook = logbook + f"D {deposit} \n" 
        balance = balance + deposit
    elif operation == "R":
        whitdrew = int(input("Ingrese el monto: "))
        if balance - whitdrew < 0:
            print("Saldo insuficiente \n")
        else:
            logbook = logbook + f"R {whitdrew} \n" 
            balance = balance - whitdrew
    else:
        print("Operacion ingresada inválida \n")

print(f"Bitácora: \n {logbook}")

print(f"Saldo final: {balance}")



#Ejercicio 3



#Ejercicio 6
num_list = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
find_num = int(input("Ingrese el número que desea buscar: "))
for i in num_list:
    if find_num == num_list[i]:
        print(f"Se encontró el número {num_list[i]}")
        break
    else:
        print("El número no está")

print("Fin del programa")
