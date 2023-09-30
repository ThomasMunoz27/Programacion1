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