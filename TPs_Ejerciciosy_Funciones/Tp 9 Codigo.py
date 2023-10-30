import sys
import aFunciones as funcion
### Direccion archivo laptop
#sys.path.append("C:/Users/sonic/OneDrive/Escritorio/GitHub/Programacion1/TPs_Ejerciciosy_Funciones/aClases")

### Direccion archivo PC
sys.path.append("C:/Users/Thomy/Desktop/GitHub/Programacion1/TPs_Ejerciciosy_Funciones/aClases")

#from Persona import Person
#from Cuenta import Count
#from Triangulo import Triangle
from Contactos import Contacts
#Ejercicio 1
'''
p1 = Person("Thomas", 17, 94219667)
p2 = Person()
p2.set_name("Paula")
p2.set_dni(44593085)
p2.set_age(20)
p2.set_blood_type("o+")

p1.show_info()
print()
p2.show_info()
p1.adult()
p2.adult()
'''
#Ejercicio 2
'''
c1 = Count("Thomas Muñoz", 38522.59)

c1.show_info()
c1.set_amount(2000.0)
c1.show_info()
c1.set_amount(-5000.0)
c1.show_info()
c1.entry_money(5)
c1.entry_money(-5)
c1.withdraw(6)
c1.withdraw(-6)
'''

#Ejercicio 3
'''
t1 = Triangle("a", 10, 5, 6)
t1.tria_type = "equilátero"
t1.show_larger_side()
t1.show_info()
t1.tria_type = "a"
t1.show_info()

'''
#Ejercicio 4

c1 = Contacts([["Thomas Muñoz", 2616978762, "aaa@gmail.com"]])

option = 1
while option != 0:
    print(f"\n¿Que desea ralizar? \nAñadir Contacto(1) \nVer lista de contactos(2) \nBuscar contacto(3) \nEditar Contacto(4) \nCerrar agenda(0)")

    option = funcion.valid_int("Ingrese una opcion: ")
    #Menú
    if option == 1:
        c1.contact_list.append(funcion.new_contact())
    if option == 2:
        for i in range(0, len(c1.contact_list)):
            print(f"Contacto {i+1}:\n  Nombre:{c1.contact_list[i][0]}.\n  Número de teléfono: {c1.contact_list[i][1]}.\n  Email: {c1.contact_list[i][2]}")
    if option == 3:
        print("Busqueda por nombre")
        search = input("Ingrese el nombre del contacto: ").title()
        coincidence = 0
        contact = 0
        for i in range(0, len(c1.contact_list)):

            if search == c1.contact_list[i][0]:
                coincidence += 1
                contact = i + 1


        if coincidence == 1:
            print(f"Se encontró el contacto. Es el número {contact}")
        else:
            print("No se encontró el contacto")
    if option == 4:
        edit = funcion.valid_int("Ingrese el contacto a editar: ")-1
        if edit < len(c1.contact_list):
            print("Que desea editar? \n Nombre(1) \n Número(2) \n Email(3)")
            edit_option = funcion.valid_int("Ingrese una opción: ")
            if edit_option == 1:
                c1.contact_list[edit][0] = input("Ingrese el Nombre: ")
                
            elif edit_option == 2:
                c1.contact_list[edit][1] = funcion.valid_int("Ingrese el Nombre: ")
                
            elif edit_option == 3:
                while True:
                    email = input("Ingrese el email: ")
                    if "@" in email and "." in email:
                        c1.contact_list[edit][3] = email
                        break
                    else:
                        print("Ingrese una direccion de email válida")
            else:
                print("Opción inválida")
print("Saliendo...")