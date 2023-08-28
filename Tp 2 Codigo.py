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
name1 = input("Ingrese el nombre de la 1ra persona: ")
name2 = input("Ingrese el nombre de la 2da persona: ")
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
name = input("Ingrese su nombre: ")
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


#Ejercicio 19
cant_lapiz = int(input("Ingrese la cantidad de lapices a comprar: "))
precio = 60 * cant_lapiz
if cant_lapiz >= 1000:
    precio_final = precio - (precio * 0.7)
else:
    precio_final = precio

print(f"Se debe pagar ${precio_final} por los {cant_lapiz} lapices")
