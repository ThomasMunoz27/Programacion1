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
import aFunciones as funcion
phrase = input("Ingrese una frase: ").strip()
num_word = funcion.last_word_num(phrase)
print(f"La longitúd de la última palabra de la oración es: {num_word}")


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


#Ejercicio 4
import aFunciones as funcion
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
funcion.multiples(num1, num2)


#Ejercicio 5
import aFunciones as funcion
cant_days = int(input("Ingrese la cantidad de días a los que se les va a calcular la media de temperatura: "))
for i in range(0, cant_days):
    temp_max = float(input(f"Ingrese la máxima del día {i + 1}: "))
    temp_min = float(input(f"Ingrese la mínima del día {i + 1}: "))
    median = funcion.calc_median(temp_max, temp_min)
    print(f"La media del día {i + 1} es : {median}")



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


#Ejercicio 16
import aFunciones as funcion
try:
    frecuency = 0
    num = int(input("Ingrese un número entero: "))
    #separar el número
    num = funcion.separate_num(num)
    while True:
        digit = (input("Ingrese un dígito: "))
        if len(digit) > 1:
            print("Ingrese solamente un dígito")
        else:
            break
    frecuency = funcion.determ_frec(digit, frecuency, num)
    print(f"El número {digit} aparece {frecuency} veces en el número {('').join(num)}")
except ValueError:
    print("Ingrese solamente números")

