num1 = int(input("Ingrese un número entero mayor que cero para conocer sus divisores: "))
divisors = []
if num1 > 0:
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisors.append(i)

print(f"Los divisores de {num1} son: {divisors}")