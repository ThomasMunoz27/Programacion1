import aFunciones as funcion

passengers = [("Thomas Muñoz", 94219667, "Buenos Aires")]
cities = []
country_cities = [("Buenos Aires", "Argentina"),
    ("Córdoba", "Argentina"),
]
#Menu
while True:
    try:
            #opciones de menú
            option = int(input("Ingrese una opcion de menú \n (1) Para agregar pajajeros. \n (2) Agregar ciudades. \n (3) Ver viaje por N°DNI. \n (4) Ver cuántos pasajeros viajan a X ciudad. \n (5) Ver cuántos pasajeros viajan a X país \n (0) Salir \n :"))

            if option == 1:
                passenger, city = funcion.add_passengers()
                #se agrega el pasajero a la lista de pasajeros
                passengers.append(passenger)

                not_here = 0
                #se busca si la ciudad de destino está en la lista de ciudades.
                for i in country_cities:
                    if city not in i:
                        not_here += 1
                #Sino se debe agregar a que país pertenece
                if not_here == len(country_cities):
                    country_cities.append(funcion.verify_city(city))
                print(country_cities)

            elif option == 2:

                new_city = funcion.add_city()
                #verifica que la ciudad-pais no esté registrada para registrarla
                if new_city not in country_cities :
                    country_cities.append(new_city)
                    print("Ciudad agregada")
                    print(country_cities)
                else:
                    print(f"La ciudad ya está registrada")
            elif option == 3:
                funcion.travel_search(passengers)
            elif option == 4:
                print
            elif option == 5:
                print
            elif option == 0:
                print("Saliendo...")
                print("Gracias por utilizar nuestros servivios.")
                break
            else:
                print("Ingrese una de la opciones específicadas")
    except ValueError:
        print("Ingrese una de la opciones específicadas")


