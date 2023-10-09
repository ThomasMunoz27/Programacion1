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

