import aFunciones as funcion
#Ejercicio 1


while True:
    try:
        dni = int(input("Ingrese su DNI: "))
        print(funcion.validDni(dni))
        break
    except ValueError:
        print("Por favor ingrese un numero de DNI válido")

#Ejercicio 2



#Ejercicio 3
import aFunciones as funcion
try:
    while True:
        vDni = False
        fullName = input("Ingrese el nombre completo del socio. \nPara finalizar y salir ingrese un epacio en blanco: ")
        fullName = fullName.split()
        if fullName == "" or fullName == " ":
            break
        if len(fullName) < 2: 
            print("Ingrese al menos 1 nombre y 1 apellido")
        else:
            while vDni == False:
                try:
                    dni = int(input("Ingrese su DNI: "))
                    vDni = funcion.validDni(dni)
                    if vDni == False:
                        print("Ingrese un DNI válido")
                except ValueError:
                    print("Ingrese carácteres válidos para la correcta ejecución")
            lastName = funcion.searchLastName(fullName)
            dniId = funcion.getDniId(dni)
            finalId = funcion.createId(fullName, lastName, dniId)

            print(f" Nombre: {' '.join(fullName)} \n DNI: {dni} \n ID: {finalId}")
    print("Adios.")
except ValueError:
    print("Ingrese carácteres válidos para la correcta ejecución")



#Ejercicio 6
import aFunciones as funcion
phrase = input("Ingrese una oración: ")
print(funcion.space_between_letters(phrase))


#Ejercicio 7
import aFunciones as funcion
num_list = []
while True:
    try:
        while True:
            entry_num = (input("Ingrese números. Para deterse y mostrar el máxumo y el mínimo ingrese 'Salir': ")).lower()
            if entry_num == "salir":
                break
            else:
                num_list.append(int(entry_num))
            min, max = funcion.calc_min_and_max(num_list)
        print(f"El número ingresado mas bajo es: {min}. \nEl número ingresado mas alto es {max}.")
        break
    except ValueError:
        print("Ingrese un num")


#Ejercicio 13
import aFunciones as funcion
vector = [

]
dimension = 3
for i in range(dimension):
    valor = int(input(f"Ingrese el valor para la componente {i + 1}: "))
    vector.append(valor)
print(vector)
vector_modul = funcion.calc_modulo_vector(vector)
print(f"El módulo del vector es: {vector_modul}")



#Ejercicio 14
import aFunciones as funcion
new_num = int(input("Ingrese un número: "))
prime_num = funcion.verify_prime_number(new_num)
if prime_num == True:
    print("El número es primo")
else: 
    print("El número no es primo")