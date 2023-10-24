import aFunciones as funcion


#Ejercicio 1
passengers = [("Thomas Muñoz", 94219667, "Buenos Aires"), ("Denis Rojas", 45682453, "Córdoba")]
country_cities = [("Buenos Aires", "Argentina"),
    ("Córdoba", "Argentina"),
    ("Santa Fe", "Argentina"),
    ("Mendoza", "Argentina"),
    ("Tucumán", "Argentina"),
    ("Entre Ríos", "Argentina"),
    ("Salta", "Argentina"),
    ("Misiones", "Argentina"),
    ("Chaco", "Argentina"),
    ("Corrientes", "Argentina"),
    ("San Juan", "Argentina"),
    ("Jujuy", "Argentina"),
    ("Río Negro", "Argentina"),
    ("Formosa", "Argentina"),
    ("Neuquén", "Argentina"),
    ("San Luis", "Argentina"),
    ("La Pampa", "Argentina"),
    ("Catamarca", "Argentina"),
    ("La Rioja", "Argentina"),
    ("Santa Cruz", "Argentina"),
    ("Tierra del Fuego", "Argentina")
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

            elif option == 2:

                new_city = funcion.add_city()
                #verifica que la ciudad-pais no esté registrada para registrarla
                if new_city not in country_cities :
                    country_cities.append(new_city)
                    print("Ciudad agregada")
                else:
                    print(f"La ciudad ya está registrada")
            elif option == 3:
                funcion.travel_search(passengers)
            elif option == 4:
                funcion.cant_passengers_travel(passengers)
            elif option == 5:
                funcion.cant_country_tavel(country_cities, passengers)
            elif option == 0:
                print("Saliendo...")
                print("Gracias por utilizar nuestros servivios.")
                break
            else:
                print("Ingrese una de la opciones específicadas")
    except ValueError:
        print("Ingrese una de la opciones específicadas")



#Ejercicio 2
import aFunciones as funcion
customers = [("Denis Rojas", 7, 120, "Pinamar 803"), 
            ("Kevin Puentes", 6, 242, "Calle 33"), 
            ("Thomas Muñoz", 5, 1500, "Bernardo Ortiz 1345"), 
            ("Thomas Muñoz", 8, 2500, "Bernardo Ortiz 1345"), 
            ("Thomas Muñoz", 16, 6000, "Bernardo Ortiz 1345"), 
            ("Kevin Puentes", 22, 4623, "Calle 33"), 
            ("Denis Rojas", 25, 10000, "Pinamar 803"),  ]
adresses = (funcion.fact(customers))
for i in range(0, len(adresses)):
    print(adresses[i])



#Ejercicio 3
import aFunciones as funcion
members = {1 : ["Armanda núñez", "17/03/2009", "s"], 
            2 : ["Bárbara Molina", "17/03/2009", "s"], 
            3 : ["Lautaro Campos", "17/03/2009", "s"], 
            4 : ["Thomas Muñoz", "13/03/2018", "n"], 
            5 : ["Denis Rojas", "13/03/2018", "s"], 
            6 : ["Tomas Pérez", "25/06/2020", "n"]}
print(members[1][1])

while True:
    try:
        select = int(input("Ingrese una opción:\n (1) Informar la cantidad de socios del Club.\n (2) Ingrese el número de un socio para pagar todas las cuotas adeudadas.\n (3) Corregir fechas de ingreso.\n (4) Ingrese nombre y apellido de un socio para darlo de baja.\n (5) Imprimir la lista completa de socios.\n (0) Salir.\n : "))

        if select == 1:
            print(f"La cantidad de socios registrados es: {len(members)}")
        elif select == 2:
            funcion.pay_fee(members)
        elif select == 3:
            funcion.fix_date(members)
        elif select == 4:
            funcion.delete_member(members)
        elif select == 5:
            funcion.show_members(members)
        elif select == 0:
            print("Saliendo...")
            print("Gracias por utilizar nuestros servivios.")
            break

    except ValueError:
        print("Ingrese una de la opciones específicadas")

