import aFunciones as fun

sum_nums = 0
while True:
    num = int(input("Ingrese un número para sumar sus dígitos(Ingrese 0 para salir): "))
    print(f"Suma de dígitos {fun.sum_digits(num)}")
    sum_nums += num
    if num == 0:
        break

print(f"La suma de todos los números ingresados anteriormente es: {sum_nums}")
print(f"La suma de los dígitos de {sum_nums} es: {fun.sum_digits(sum_nums)}")

#Ejercicio de funciones
#DEFINICION DE FUNCIONES
def most(a, b):
    if (a > b):
        return a
    else:
        return b
    
def least(a, b):
    if (a < b):
        return a
    else:
        return b
    
#PROGRAMA PRIMCIPAL

x = int(input("Un número: "))
y = int(input("Otro número: "))

print(most(x-3, least(x+2, y-5)))