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
    temp_max = float(input(f"Ingrese la máxima en °C del día {i + 1}: "))
    temp_min = float(input(f"Ingrese la mínima en °C del día {i + 1}: "))
    median = funcion.calc_median(temp_max, temp_min)
    print(f"La media del día {i + 1} es : {median}°C")



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


#Ejercicio 8
import aFunciones as funcion
radio = float(input("Ingrese el radio de la circunferencia: "))
area = funcion.calc_area(radio)
perimeter = funcion.calc_perimeter(radio)

print(f"El área de la circunferencia es: {area}.\nEl perimetro de una circunferencia es: {perimeter}")


#Ejercicio 9
import aFunciones as funcion
attemps = 3
validation = None
while True:
    if attemps == 0 and validation == 0:
        print("\nSe ha quedado sin intentos para iniciar sesión")
        break
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    validation = funcion.login(user, password)
    if validation == True:
        print("Inicio de sesion exitoso")
        break
    elif validation == 0:
        attemps -= 1
        print("\nNombre de usuario o contraseña incorrectos intente otra vez\n")


#Ejercicio 10
import aFunciones as funcion
prices_percentages={
    2500:0.15,
    3000:0.20,
    1500:0.05,
    2600:0.30,
    6740:0.25,
    2000:0.10
}
print(f"El total de la compra con los respectivos descuentos es de: {funcion.purchase_total(prices_percentages)}")


#Ejercicio 11
import aFunciones as funcion
names = ["JuAn ", "AMeLia ", "AnToNellA "]

for i in range(3):
    print("Elemento de la lista antes de la funcion: ", names[i])
    print("Llamamos la funcion. ")
    names[i] = funcion.call_other_f(names[i])
    print("Elemento de la lista después de la funcion: ", names[i])

#Ejercicio 12
import aFunciones as funcion
phrase = input("Ingrese una frase: ")
dict_phrase = funcion.phrase_to_dict(phrase)
print(f"La frase en diccionario es: {dict_phrase}")


#Ejercicio 13
import aFunciones as funcion
vector = [

]
dimension = int(input("Ingrese la magnitud del vector: "))
for i in range(dimension):
    valor = int(input(f"Ingrese el valor para la componente {i + 1}: "))
    vector.append(valor)
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


#Ejercicio 15
import aFunciones as funcion
cant_entries = 0
while True:
        try:
            num_fact = int(input("Ingrese un número para saber su factorial. \nIngrese un número negativo para parar: "))
            if num_fact < 0:
                break
            else:
                factorial = funcion.calc_factorial(num_fact)
                cant_entries += funcion.calc_entries(factorial)
                print(f"el factorial del número {num_fact} es: {factorial}")
        except ValueError:
            print("Ingrese un número")
print(f"Usted ha calculado los factoriales de {cant_entries} números")



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

#Ejercicio 17
import aFunciones as funcion
funcion.entering_prime_numbers()