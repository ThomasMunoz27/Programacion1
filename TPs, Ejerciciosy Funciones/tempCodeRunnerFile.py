#Ejercicio 1 y 2
num_list = []
while True:
    try:
        entry_num = int(input("Ingrese números para ingresarlos en una lista: "))
        if entry_num == 0:
            break
        else:
            num_list.append(entry_num)


    except ValueError:
        print("Ingrese un número")
second_entry = int(input("Ingrese otro número"))
if second_entry in num_list:
    num_list.remove(second_entry)
    print(num_list)
else: 
    print("No es posible eliminar ese número de la lista")