import aFunciones as funcion
new_num = int(input("Ingrese un número: "))
prime_num = funcion.verify_prime_number(new_num)
if prime_num == True:
    print("El número es primo")
else: 
    print("El número no es primo")