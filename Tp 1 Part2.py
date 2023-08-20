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

#Ejercicio 14
a=input("Ingresar el valor numérico de a: ")
b=input("Ingresar el valor numérico de b: ")
aux=a
a=b
b=aux
print("a=",a)
print("b=",b)


#Ejercicio 15
print("ingrese la hora, minutos y segundos de salida")
hora_salida= int(input(print("ingrese la hora")))
min_salida= int(input(print("ingrese los minutos")))
seg_salida= int(input(print("ingrese los segundos")))
seg_del_viaje= 5415
print("La hora de llegada va a ser:")
seg_horas= hora_salida*3600
seg_min= min_salida*60
seg_total= seg_salida+seg_horas+seg_min+seg_del_viaje

hora_tot= int(seg_total/3600)
seg_total-=(hora_tot*3600)

min_tot= int(seg_total/60)
seg_total-= (min_tot*60)
print(f"{hora_tot}:{min_tot}:{seg_total}")


#Ejercicio 16
nombre=input("Ingresar su nombre")
apellido1=input("Ingresar  primer apellido")
apellido2=input("Ingresar segundo apellido")
iniciales= nombre[0]+apellido1[0]+apellido2[0]
print(iniciales)


#Ejercicio 17
nombre = input('Ingresa tu nombre: ')
print(f'Ahora estas en la Matrix, {nombre}')


#Ejercicio 18
costo_inicial=input("Ingrese el costo de la cena:")
serv = costo_inicial * 0.62
prop = costo_inicial * 0.10
costo_final= costo_inicial + serv + prop 
print(f"El costo final de la cena es de:", {costo_final})


#Ejercicio 19
dia = input('Ingresa el dia en el que naciste: ')
print()
mes = input('Ingresa el mes en el que naciste: ')
print()
año = input('Ingresa el año en el que naciste: ')
print()
print(f'{dia}/{mes}/{año}')


#Ejercicio 20
fecha_nac=input('Ingresar su fecha de nacimiento:')
print(f'{fecha_nac[0:2]}/{fecha_nac[2:4]}/{fecha_nac[4:9]}')


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


