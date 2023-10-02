import aFunciones as funcion
try:
    cant_entries = 0
    while True:
        num_fact = int(input("Ingrese un número para saber su factorial. \nIngrese un número negativo para parar: "))
        if num_fact < 0:
            break
        else:
            factorial = funcion.calc_factorial(num_fact)
            cant_entries += funcion.calc_entries(factorial)
            print(f"el factorial del número {num_fact} es: {factorial}")
    print(f"Usted ha calculado los factoriales de {cant_entries} números")
except ValueError:
    print("Ingrese un número")
