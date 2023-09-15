
balance = 0
logbook = "\n"
entry = "."
while entry != "":
    print("\n")
    entry = input("¿Qué operación desea realizar? \n Deposito(D) --- Retiro(R), e ingrese el monto.\n Para finalizar ingrese un espacio vacío: ")
    if entry != "":
        operation = entry[0]
        entry = entry.split()
        del entry[0]
        sum = int(entry[0])
        operation = operation.upper()
    if operation == "D":
        deposit = sum
        logbook = logbook + f"D {deposit} \n" 
        balance = balance + deposit
    elif operation == "R":
        whitdrew = sum
        if balance - whitdrew < 0:
            print("Saldo insuficiente \n")
        else:
            logbook = logbook + f"R {whitdrew} \n" 
            balance = balance - whitdrew
    else:
        print("Operación ingresada inválida \n")

print(f"Bitácora: \n {logbook}")

print(f"Saldo final: {balance}")
