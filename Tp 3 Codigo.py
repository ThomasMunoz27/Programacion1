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
height = int(input("Ingrese la altura del tiángulo: "))
row = ""
for i in range(0, height):
    row += "*"
    print(row)



#Ejercicio 7
num = int(input("Ingrese un número para saber sus Tablas: "))
print(f"Tabla del {num}")
for i in range(1, 11):
    print(f"{num}: {i} * {num} = {num * i}")



#Ejercicio 8
heigth_num = int(input("Ingrese un número entero: "))
num_row = ""
for i in range(0, heigth_num+1):
    if i % 2 != 0:
        num_row += " " +str(i)
        print(num_row)


#Ejercicio 9
password = input("Establezca una contraseña: ")
passw_try = ""
while passw_try != password:
    passw_try = input("Ingrese la contraseña: ")
print("Contraseña correcta! :D")



#Ejercicio 10
num = int(input("Ingrese un número: "))
divisors = 0
for i in range(num, 0, -1):
    if num % i == 0:
        divisors += 1 

if divisors <= 2:
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")



#Ejercicio 11
word = input("ingrese una palabra: ")

#for i in range(len(word) - 1, 0 - 1, -1):
#    print(word[i])

for i in reversed(word):
    print(i)


#Ejercicio 12
phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
letter_frequency = 0
for i in phrase:
    if i in letter:
        letter_frequency += 1
print(f"Se encontró la letra {letter}, {letter_frequency} veces")


#Ejercicio 13
echo = ""
while echo != "salir":
    echo = input("... ")
    echo = echo.lower()
    if echo != "salir":
        print(echo)
print("saliste")


#Ejercicio 14
num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
even = []
odd = []
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Los números pares son {even} y los impares {odd}")



#Ejercicio 15
num1 = int(input("Ingrese un número entero mayor que cero para conocer sus divisores: "))
divisors = []
if num1 > 0:
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisors.append(i)

print(f"Los divisores de {num1} son: {divisors}")


#Ejercicio 16




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

