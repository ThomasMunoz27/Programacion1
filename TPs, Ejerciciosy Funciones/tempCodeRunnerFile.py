import aFunciones as funcion
#Ejercicio 1


while True:
    try:
        dni = int(input("Ingrese su DNI: "))
        print(funcion.validDni(dni))
        break
    except ValueError:
        print("Por favor ingrese un numero de DNI válido")