#Ejercicio 1
edad_pc = int(input("Ingrese la edad en años de su computdora: "))
if edad_pc <= 2:
    print("El computador es nuevo")
else:
    print("El computador es viejo")


#Ejercicio 2
edad_pc = int(input("Ingrese la edad en años de su computdora: "))
if edad_pc >= 0 and edad_pc<= 2:
    print("El computador es nuevo")
elif edad_pc < 0:
    print("ERROR. No puede ingresar un número negativo")
else:
    print("El computador es viejo")


#ejercicio 3
name1 = input("Ingrese el nombre de la 1ra persona: ").lower()
name2 = input("Ingrese el nombre de la 2da persona: ").lower()
name1_inicial = name1[0]
name2_inicial = name2[0]

if name1_inicial == name2_inicial:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#Ejercicio 4
voto = input("Ingrese a que candidato va a votar: ")
voto = voto.lower()
if voto == "a":
    print("Usted a votado por el partido ROJO")
elif voto == "b":
    print("Usted a votado por el partido VERDAD")
elif voto == "C":
    print("Usted a votado por el partido AZUL")
else:
    print("Opción erronea")


    #Ejercicio 5
letra = input("ingrese una letra: ")
letra = letra.lower()
vocales = ("a", "e", "i", "o", "u")
if len(letra)<1:
    print("ERROR. Solo debe ingresarse una letra")
elif letra in vocales:
    print(f"La letra {letra} es una vocal")
else:
    print(f"La letra {letra} no es una vocal")


#Ejercicio 6
ano = int(input("Ingrese el año para saber si es bisiesto: "))
if (ano % 4==0) and (ano % 100 !=0 or (ano % 400 == 0)):
    print(f"El año {ano} es bisiesto")
else:
    print(f"El año {ano} no es bisiesto")


#Ejercicio 7
print("Ingresar tres números")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
print("El número mas grande es")
max = a
if b> max:
    max = b
if c>max:
    max=c
print(max)


#Ejercicio 8
user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if (user == "Gwenevere") and (password == "excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")


#Ejercicio 9
sex = input("Ingrese su sexo(Hombre/Mujer): ")
sex = sex.lower()
name = input("Ingrese su nombre: ").lower()
name_inicial = name[0]

if name_inicial < "m" and sex == "mujer":
    print("Usted pertenece al grupo A")
elif name_inicial > "m" and sex == "mujer":
    print("Usted pertenece al grupo B")
elif name_inicial > "n" and sex == "hombre":
    print("Usted pertenece al grupo A")
elif name_inicial < "n" and sex == "hombre":
    print("Usted pertenece al grupo B")
else:
    print("Usted no pertenece a ningún grupo")

#Ejercicio 10
print("Bienvenido a la sala de juegos!!!")
edad = int(input("Ingrese su edad: "))

if edad < 4 and edad > 0:
    print("Usted puede entrar gratis :D")
elif edad <=18:
    print("Usted debe pagar $500 para ingresar")
elif edad > 18:
    print("Usted debe pagar $1000 para ingresar")
else:
    print("Edad inválida")


#Ejercicio 11
print(f"Bienvenido a la pizzeria Bella Napoli ")

pizza_base = "mozzarella, tomate y "

tipo_pizza = input("¿Qué tipo de Pizza prefiere? \n ¿Vegetariana o Normal?: ")
tipo_pizza = tipo_pizza.lower()

if tipo_pizza == "vegetariana":
    ingrediente = input("Elija un ingrediente para su pizza vegetariana (Pimiento o Tofu): ")
    ingrediente = ingrediente.lower()
    if (ingrediente == "tofu") or (ingrediente == "pimiento"):
        print(f"Su pizza {tipo_pizza} contiene {pizza_base}{ingrediente}. \n Disfrute! :D")
    else:
        print("Ese ingrediente no está disponible")
elif tipo_pizza == "normal":
    ingrediente = input("Elija un ingrediente para su pizza normal (Peperoni, Jamón o Salmón): ")
    ingrediente = ingrediente.lower()
    if (ingrediente == "peperoni") or (ingrediente == "salmón") or (ingrediente == "jamón"):
        print(f"Su pizza {tipo_pizza} contiene {pizza_base}{ingrediente}. \n Disfrute! :D")
    else:
        print("Ese ingrediente no está disponible")



#Ejercicio 12
ano_actual, ano_cualquiera = int(input("Ingrese el año actual: ")), int(input("Ingrese un año cualquiera: "))

if ano_actual < ano_cualquiera:
    ano_diff = ano_cualquiera - ano_actual
    print(f"Faltan {ano_diff} años para llegar a {ano_cualquiera}")
else:
    ano_diff = ano_actual - ano_cualquiera
    print(f"Han pasado {ano_diff} años desde {ano_cualquiera}")



#Ejercicio 13
num1, num2 = int(input("Ingrese 2 números: ")), int(input())

mayor = num1
menor = num2
if num1 or num2 > 0:
    if mayor < num2:
        mayor = num2
        menor = num1
    print(f"El número {mayor} es mayor que {menor}")
    if mayor % menor == 0:
        print(f"{mayor} es múltiplo de {menor}")
    else:
        print(f"{mayor} no es múltiplo de {menor}")
else:
    print("Se ingresaron números negativos o nulos")



#Ejercicio 14
print("Ingresar los coeficientes de una ecuacion de primer grado ax + b = 0")
a=int(input("a="))
b=int(input("b="))


if a==0 and b!=0:
    print("No hay solución")
elif a==0 and b== 0:
    print("infinitas soluciones")
elif a!=0 :
    b=int(b)
    x=-b/a
    print("la solución es x= ", x)


#Ejercicio 15
operacion = input("Averiguar el área de un triángulo(t) o de un circulo(c)")
operacion = operacion.lower()
if operacion == "t":
    b = int(input("Ingrese la base del triángulo:"))
    h = int(input("Ingrese la altura del tiángulo:"))
    area = (b*a)/2
    print(f"El área del triángulo es {area}")
elif operacion == "c":
    r = int(input("ingrese el radio del circulo: "))
    area = 3.14 * (r**2)
    print(f"El área del circulo es de {area}")
else:
    print("El valor ingresado no es válido")



#Ejercicio 16
a, b = int(input("Ingrese 2 valores: ")), int(input(" "))
operacion = input(f"Ingrese que operación va a querer ejecutar.\n 1. Suma   2. Multiplicación   3. Resta   4. División: ")
if operacion == "1":
    print(f"El resultado es {a+b}")
elif operacion == "2":
    print(f"El resultado es {a*b}")
elif operacion == "3":
    print(f"El resultado es {a-b}")
elif operacion == "4":
    if b == 0:
        print("No se puede divir entre 0")
    else:
        print(f"El resultado es {a/b}")
else:
    print("Valor ingresado inválido")



#Ejercicio 17
dia_semana = input("Ingrese un día de la semana: ")
dia_semana = dia_semana.lower()

if dia_semana == "sábado" or dia_semana == "domingo":
    print("otro mensaje diferente")
elif dia_semana == "lunes":
    print("un mensaje")
elif dia_semana == "viernes":
    print("VIERNEEEEEEEEESSS!!!")
elif dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves":
    print("otro mensaje")
else:
    print("Ese día no existe")



#Ejercicio 18
salario_hora = int(input("Ingrese su salario por hora: "))
horas_trabajadas = int(input("Ingrese las horas trabajadas en el mes: "))
if horas_trabajadas < 48:
    print("El mínimo de horas trabajadas son 48 horas")
elif horas_trabajadas >= 48:
    sub_salario = salario_hora * 48
    horas_extra = horas_trabajadas - 48
    salario_extra = salario_hora * horas_extra + ((salario_hora * horas_extra)*0.1)
    salario_final = sub_salario + salario_extra
    print(f"Su salario de este mes es de ${salario_final}")



#Ejercicio 19
cant_lapiz = int(input("Ingrese la cantidad de lapices a comprar: "))
precio = 60 * cant_lapiz
if cant_lapiz >= 1000:
    precio_final = precio - (precio * 0.7)
else:
    precio_final = precio

print(f"Se debe pagar ${precio_final} por los {cant_lapiz} lapices")


#Ejercicio 20
nota1 = int(input("Ingrese la 1er nota: "))
nota2 = int(input("Ingrese la 2da nota: "))
nota3 = int(input("Ingrese la 3er nota: "))
nota4 = int(input("Ingrese la 4ta nota: "))
if (nota1 > 10 or nota2 > 10 or nota3 > 10 or nota4 > 10) or (nota1 < 0 or nota2 < 0 or nota3 < 0 or nota4 < 0):
    print("Alguna de las notas no es válida")
else:
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    if promedio >= 6 :
        print(f"Su promedio es de {promedio}")
        print("APROBADO")

    elif promedio < 6:
        print(f"Su promedio es de {promedio}")
        print("DESAPROBADO")
