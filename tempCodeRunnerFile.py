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