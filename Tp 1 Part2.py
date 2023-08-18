#Ejercicio 1
base = 3
altura = 6
area = base * altura
print(area)


#Ejercicio 2
c1= 16
c2 = 7
h = (c1**2 + c2**2)**(1/2)
print(h)


#Ejercicio 3
num1 = 46
num2 = 8
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"suma: {suma}, resta: {resta}, multiplicación: {multiplicacion}, división: {division}")


#Ejercicio 4
fahr = int(input("Ingrese la temperatura en fahrenheit: "))
celc = (fahr-32)*5/9
print(f"La temperatura en C° es de: {celc}")


#Ejercicio 5
    #a)
"""la variable "nombre" no está definida. Yo pondría "nombre" donde está la "A" """

    #b)
""" La variable "precio" termina siendo un string. Hay que agregarle un int(), antes del input() """

    #c)
""" "Tu edad es", no está entre comillas. hay que ponerle comillas """

    #d) INCOMPLETO  
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad=18)

p = 15
print(p + 1)


#Ejercicio 6
num1 = int(input("Ingrese 3 números para saber su meedia: "))
num2 = int(input())
num3 = int(input())

media = int((num1 + num2 + num3) / 3)

print(f"La media de los números es: {media}")


#Ejercicio 7
minutos = int(input("Ingrese una cantidad de minutos: "))

horas = 0 + int(minutos / 60)
min_final = 0 + int(minutos%60)

print(f" {minutos} minutos son: {horas} horas y {min_final} minutos.")


#Ejercicio 8
sueldo = int(input("Ingrese el sueldo base: "))
comision = 0 + ((sueldo * 0.10)*3)

sueldo_final = sueldo + comision

print(f"En concepto de comisiones ganaste {comision}$.")
print(f"Su sueldo total será de {sueldo_final}")


#Ejercicio 9
compra_total = int(input("ingrese el monto total de su compra: "))
desc = 0.15
monto_final = compra_total - (compra_total * desc)

print(f"El monto final de su compra es de: ${monto_final}")


#Ejercicio 10
nota1 = 8
nota2 = 9
nota3 = 8
examen_final = 9
trabajo_final = 8
cincuenta_y_cinco=(nota1+nota2+nota3)*55/30
treinta = examen_final*30/10
quince = trabajo_final*15/10
promedio_final = cincuenta_y_cinco + treinta + quince
print("el promedio final es de: ",promedio_final)


#Ejercicio 11
dist1 = float(input("Ingrese 2 números para saber su distancia entre ellos"))
dist2 = float(input())
val_abs = abs(dist1 - dist2)

print(f"La distancia entre los 2 números es de: {val_abs}")


#Ejercicio 12
num1 = int(input("Ingrese un número para saber su raíz cuadrada y cúbica: "))

raiz_2 = num1 ** (1/2)
raiz_3 = num1 ** (1/3)

print(f"La raiz Cuadrada es: {raiz_2}. Y la cúbica: {raiz_3}")


#Ejercicio 13
num = input("Ingrese un número para invertirlo ")
a = num[0]
b = num[1]
num_inv = b + a

print(f"El número invertido es: {num_inv}")


#Ejercicio 21
print("Antes de su viaje debemos saber lo siguiente: ")

dist_1lit= int(input("Ingrese cuantos km puede recorrer con 1 litro de combustible: "))
print()

tank_cap = int(input("Ingrese la capacidad, en litros, de su tanque d combustible: "))
print()

viaje_dist = int(input("Ingrese la cantidad de km total de su viaje: "))

tank = dist_1lit * tank_cap

tank_nec = viaje_dist / tank

print(f"La cantidad de tanques de combustible necesarios para su viaje es/son: {tank_nec}")


