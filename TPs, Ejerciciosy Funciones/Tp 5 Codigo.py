#Ejercicio 1
def validDni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False


while True:
    try:
        dni = int(input("Ingrese su DNI: "))
        print(validDni(dni))
        break
    except ValueError:
        print("Por favor ingrese un numero de DNI válido")

#Ejercicio 2



#Ejercicio 3
while True:
    fullName = input("Ingrese su nombre completo. Para detenerse no ingrese nada: ")
    fullName = fullName.split()
    if len(fullName) == 3:
        apellido = fullName[2]
    elif len(fullName) == 2:
        apellido = fullName[1]
