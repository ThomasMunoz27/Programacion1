
#Ejercicio 2

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



#Ejercicio 3
#indefinited_nums = []
leave = 1
prime_numers = 0

while leave != 0:
    entry_nums = int(input("\nIngrese números mayores a 1. Para detenerse presione 0: "))
    if entry_nums > 1:
        #indefinited_nums.append(entry_nums)
        divisors = 0
        for i in range(1, entry_nums+1):
            
            if entry_nums % i == 0:
                divisors += 1
        if divisors > 2:
            pass
        else:
            prime_numers += 1
    elif entry_nums == 0:
        leave = 0
    else:
        print("Número inválido. Intente otra vez:\n")
#print(f"Los números ingresados fueron {indefinited_nums}")
print(f"Se ingresaron un total de {prime_numers} números primos")



#Ejercicio 4
year1 = int(input("Ingrese el primer año: "))
year2 = int(input("Ingrese el segundo año: "))
year_list = []


for i in range(year1, year2 + 1):
    if (i % 4 == 0) and i % 100 != 0 or i % 400 == 0:
        year_list.append(i)
    elif i % 10 == 0:
        year_list.append(i)

print(f"Los años bisiestos entre los ingresados son: {year_list} ")


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


#Ejercicio 7
option = 0
strawberry = 0
peach = 0
avocado = 0
while option != 4444:
    option = int(input("Elija una opción. \n Frutilla(1) \n Durazno(2) \n Palta(3) \n Para salir ingrese cero(0)"))
    if option == 1:
        strawberry +=1
        print(f"Tienes {strawberry} frutillas")
    elif option == 2:
        peach += 1
        print(f"Tienes {peach} duraznos")
    elif option == 3:
        avocado += 1
        print(f"Tienes {avocado} paltas")
    elif option == 0:
        break
    else:
        print("Elección inválida. Intente otra vez")
print("Saliste")