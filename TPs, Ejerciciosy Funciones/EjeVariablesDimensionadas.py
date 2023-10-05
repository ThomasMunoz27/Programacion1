import aFunciones as funcion

passengers = []
cities = []
country_cities = [("Buenos Aires", "Argentina"), ("Mendoza", "Argentina")]
#Menu
try:
    while True:
        option = int(input("Ingrese una opcion de menú \n (1) Para agregar pajajeros. \n (2) Agregar ciudades. \n (3) Ver viaje por N°DNI. \n (4) Ver cuántos pasajeros viajan a X ciudad. \n (5) Ver cuántos pasajeros viajan a X país \n (0) Salir \n :"))
        if option == 1:
            passenger, city = funcion.add_passengers()
            passengers.append(passenger)
            print(passengers)
        elif option == 2:
            print
        elif option == 3:
            print
        elif option == 4:
            print
        elif option == 5:
            print
        elif option == 0:
            print("Saliendo...")
            break
        else:
            print("Ingrese una de la opciones específicadas")
    print("Gracias por utilizar nuestros servivios.")
except ValueError:
    print("Ingrese una de la opciones específicadas")


