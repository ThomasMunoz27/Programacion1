#Ejercicio 1
import aFunciones as funcion
digit = 1
num = int(input("Ingrese un número: "))
print(funcion.count_digits(num, digit))


#Ejercicio 2
import aFunciones as funcion
num1, num2 = 36, 6
print(funcion.find_pot(num1, num2))


#Ejercicio 3
import aFunciones as funcion
print(funcion.string_position("pablito clavó un clavito, cuantos clavitos clavó pablito", "ito"))



#Ejercicio 4
import aFunciones as funcion
num = int(input("Ingrse un número para saber si es par o impar: "))
val_par = funcion.par(num)
val_imp = funcion.impar(num)
print(f"¿El número {num} es par?: {val_par}")
print(f"¿El número {num} es impar?: {val_imp}")


#Ejercicio 5
import aFunciones as funcion
nums = [5,2,4444,7,19,4449,100,15,64,69]
big = funcion.found_bigest(nums)
print(big)



#Ejercicio 6
import aFunciones as funcion
replic_list = funcion.repli([1,3,3,7], 4)
print(replic_list)



#Ejericio 7
import aFunciones as funcion
n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))

result = funcion.period_sum(n,p)

print(f"El resultado de K({n},{p}) es: {result}")


#Ejercicio 8
import aFunciones as funcion
n = int(input("Ingrese la fila:  "))
k = int(input("Ingrese la columna: "))

num = funcion.pascal(n,k)
print(num)


#Ejercicio 9
import aFunciones as funcion
print(funcion.combinations(['a', 'b', 'c'], 3))


#Ejercicio 10
import aFunciones as funcion
size = int(input("Ingrese la medida de la hoja A(N): "))
print(f"El tamaño de la hoja A{size} es :")
final_size = funcion.calc_size(size)
print(f"{final_size[0]}mm x {final_size[1]}mm")