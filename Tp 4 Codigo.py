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

