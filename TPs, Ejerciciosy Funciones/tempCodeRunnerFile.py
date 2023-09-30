import aFunciones as funcion
cant_days = int(input("Ingrese la cantidad de días a los que se les va a calcular la media de temperatura: "))
for i in range(0, cant_days):
    temp_max = float(input(f"Ingrese la máxima del día {i + 1}: "))
    temp_min = float(input(f"Ingrese la mínima del día {i + 1}"))
    median = funcion.calc_median(temp_max, temp_min)
    print(f"La media del día {i + 1} es : {median}")
