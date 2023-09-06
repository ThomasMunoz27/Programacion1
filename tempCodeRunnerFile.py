fact_num = int(input("ingrese el número que desea saber su factoriaL: "))
factorial = 1
if fact_num < 0:
    print("Número ingresado inválido")
else:
    for i in range(1, fact_num + 1):
        factorial *= i 
print(f"El factorial de {fact_num} es: {factorial}")