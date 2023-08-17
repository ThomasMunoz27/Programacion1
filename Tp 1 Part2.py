#1
base = 3
altura = 6
area = base * altura
print(area)

#2
c1= 16
c2 = 7
h = (c1**2 + c2**2)**(1/2)
print(h)

#10
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


#11
dist1 = float(input("Ingrese 2 números para saber su distancia entre ellos"))
dist2 = float(input())
val_abs = abs(dist1 - dist2)

print(f"La distancia entre los 2 números es de: {val_abs}")

#21
print("Antes de su viaje debemos saber lo siguiente: ")

dist_1lit= int(input("Ingrese cuantos km puede recorrer con 1 litro de combustible: "))
print()

tank_cap = int(input("Ingrese la capacidad, en litros, de su tanque d combustible: "))
print()

viaje_dist = int(input("Ingrese la cantidad de km total de su viaje: "))

tank = dist_1lit * tank_cap

tank_nec = viaje_dist / tank

print(f"La cantidad de tanques de combustible necesarios para su viaje es/son: {tank_nec}")


