#Ejercicio 1

word = input("Ingrese una palabra para repetirla: ")

for i in range(11):
    print(word)


#Ejercicio 2
age = int(input("Ingrese su edad: "))

for i in range(age):
    print(f"Viviste tu año {i +1}")


#Ejercicio 3
num = int(input("Ingrese un número positivo"))

if num < 0:
    input("Número ingresado inválido")
else:
    for i in range(1, num, 2):
        print(i)


#Ejercicios 4
num = int(input("Ingrese un número entero positivo: "))
list = []
if num <= 0:
    print("El número ingressado es inválido")
else:
    for i in range(num, 0, -1):
        list.append(i)
print(list)


#Ejercicio 5 
to_invert = int(input("Ingrese la cantidad de dinero a invertir: "))
anual_int = int(input("Ingrese el interés anual: "))
total_years = int(input("Ingrese la cantidad de años: "))

years = 1
gains = 0

while years <= total_years:
    gains = gains + (to_invert * (anual_int / 100))
    print(f"Las ganacias del año {years} son: ${gains}")
    years = years + 1


#Ejercicio 6



#Ejercicio 23 y 24
leave = 1
f_amount = 0
while leave != 0:
    price = int(input("Ingrese el monto del producto : "))
    if price < 0:
        print("Monto inválido. \n Ingrese un nuevo monto")
    else:
        f_amount = f_amount + price
        if price == 0:
            leave = 0
        if price > 1000:
            f_amount = f_amount - (f_amount * 0.1)

print(f"El monto final de su compra es: {f_amount}")

