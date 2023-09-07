#Ejercicio 1

word = input("Ingrese una palabra para repetirla: ")

for i in range(10):
    print(word)


#Ejercicio 2
age = int(input("Ingrese su edad: "))

for i in range(age):
    print(f"Viviste tu año {i +1}")


#Ejercicio 3
num = int(input("Ingrese un número positivo: "))
odd_list = []
if num < 0:
    input("Número ingresado inválido")
else:
    for i in range(1, num + 1, 2):
        odd_list.append(i)
print(odd_list)


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
    to_invert += gains
    print(f"Las ganacias del año {years} son: ${gains}")
    print(f"Este año, en total tiene: ${to_invert}\n")
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
num_quant = int(input("Ingrese la cantidad de números a introducir: "))
negative_nums = 0
for i in range(0,num_quant):
    num = int(input(f"Ingrese números: "))
    if num < 0:
        negative_nums += 1

print(f"Se ingresaron {negative_nums} números negativos")


#Ejercicio 17
vowels = "aeiou"
phrase = input("Ingrese una frase: ")
vowel_list = []

for i in phrase:
    if i in vowels and i not in vowel_list:
                vowel_list.append(i)
print(f"Las vocales usadas en la frase fueron {vowel_list}")


#Ejercicio 18
fibo = [0, 1]
for i in range(0, 10):
    aux = fibo[len(fibo) - 1] + fibo[len(fibo) - 2]
    fibo.append(aux)
print(fibo)


#Ejercicio 19
wish_saving = int(input("Ingrese el monto de dinero que quiere llegar a ahorrar: "))
piggy_box = 0
while piggy_box < wish_saving:
    money = int(input("Ingrese el dinero a ahorrar: "))
    if money > 0:
        piggy_box += money
    else:
        print("No se puede ingresar esa cantidad de dinero")

print("Felicidades!!!. Alcanzaste tu meta de ahorro :D")



#Ejercicio 20
sum_nums = 0
entry_nums = 1
while entry_nums!= 0:
    entry_nums = int(input("Ingrese números para sumarlos. \n Para detenerse ingrese 0: "))
    sum_nums = sum_nums + entry_nums
print(f"La suma de los números es {sum_nums}")



#Ejercicio 21
higher_num = 0
entry_nums = 1
while entry_nums!= 0:
    entry_nums = int(input("Ingrese números. \n Para detenerse ingrese 0: "))
    if entry_nums > higher_num:
        higher_num = entry_nums
print(f"El mayor número ingresado fue {higher_num}")



#Ejercicio 22

entry_nums = 1
even = 0
while entry_nums!= -1:
    sum_digits = 0
    entry_nums = int(input("Ingrese números. \n Para detenerse ingrese -1: "))
    if entry_nums % 2 == 0:
        even += 1
    if entry_nums == -1:
        break

    for i in range(1, len(str(entry_nums)) + 1):
        entry_nums = str(entry_nums)
        sum_digits += int(entry_nums[i-1])
        entry_nums = int(entry_nums)
    print(f"La suma de los dígitos de {entry_nums} es: {sum_digits}")
print("Fin programa")



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


#Ejercicio 25
fact_num = int(input("ingrese el número que desea saber su factoriaL: "))
factorial = 1
if fact_num < 0:
    print("Número ingresado inválido")
else:
    for i in range(1, fact_num + 1):
        factorial *= i 
print(f"El factorial de {fact_num} es: {factorial}")


#Profe si ve esto podria cambiar mi direccion de Email a thomasnm2004@gmail.com por favor. Muchas gracias <3