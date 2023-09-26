#Ejercicio 1
def validDni(num):
    if len(num) == 7 or len(num) == 8:
        return True
    else:
        return False

dni = input("Ingrese su DNI: ")
print(validDni(dni))
