import random as ran
#Ejercicio de ejemplos de sumar dígitos
def sum_digits(num1):
    add = 0
    while num1 != 0:
        digit = num1 % 10
        add += digit
        num1 //= 10
    return add



##Funciones Ahorcado
#Funcion elejir palabra
def chose_word():
    word_list = ["sexo", "manzana", "mouse", "baile", "oreja", "rojo", "pierna", "pelo", "gato", "perro", "ciervo", "mora", "girasol", "mate", "eclipse", "piano", "silla", "rata", "pera", "esclavo", "judío", "salchicha", "comida", "zapato", "ñandu", "ñoqui", "queso", "timbre", "tornillo", "invierno", "azucar", "sal", "amanecer", "espía", "iglesia", "operador", "uva", "utensilio", "unicornio", "arco", "margarita", "esternocleidomastoideo", "bailar", "fumar", "alcaucíl", "llovizna", "porro", "lelo", "lol", "medialuna", "fernanfloo"]
    return  word_list[ran.randrange(0, len(word_list))]

#longitud de palabra
def word_large(word):
    cant_letters = len(word)
    return cant_letters

#escribir _
def write_(cant):
    g_word = []
    for i in range(0,cant):
        g_word.append("_")
    return g_word

#mostar la cantidad de veces que aparece la letra ingresada en la palabra
def timesLetterAppears(aux, letter):
    if aux == 1:
        print(f"\n Correcto!. La palabra lleva una '{letter}'")
    elif aux == 2:
        print(f"\n Correcto!. La palabra lleva dos '{letter}'")
    elif aux == 3:
        print(f"\n Correcto!. La palabra lleva tres '{letter}'")

##Funciones TP 5
#Funion Eje 1
#validar DNI
def valid_dni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False


#Funcion Eje 2
def last_word_num(sentence):
    phrase_list = sentence.split()
    cant_letters = len(phrase_list[-1])
    return cant_letters

#Funcion Eje 3
#Buscar apellido
def search_last_name(entryName):
    if len(entryName) >= 3:
        return  entryName[2]
    elif len(entryName) == 2:
        return entryName[1]

#Obtener los primero 3 números del dni
def get_dni_id(dni):
    if len(str(dni)) == 8:
        return dni // 100000
    else:
        return dni // 10000

def create_id(name, last_name, num_id):
    prev_id = ""
    prev_id += name[0] + str(len(last_name)) + str(num_id)
    return prev_id


#Funcion Eje 4
def multiples(num_a, num_b):
    if num_a % num_b == 0:
        print(f"{num_a} es múltiplo de {num_b} ")
    if num_b % num_a == 0:
        print(f"{num_b} es múltiplo de {num_a} ")


#Funcion eje 5
def calc_median(max, min):
    median = (max + min) / 2
    return median

#Funcion Eje 6
def space_between_letters(word):
    # Use compresion de listas para hacer este código.
    spaced_word = ''.join([c + ' ' for c in word if c != ' '])
    return spaced_word


#Funcion Eje 7
def calc_min_and_max(num_list):
    n_min = 100000000000000000
    n_max = 0
    for i in range(len(num_list)):
        if num_list[i] < n_min:
            n_min = num_list[i]
        elif num_list[i] > n_max:
            n_max = num_list[i]
    return n_min, n_max


#Funciones Eje 8
import math
def calc_area(rad):
    pre_area = math.pi * (rad**2)
    return pre_area


def calc_perimeter(rad):
    pre_perimeter = (rad*2) * math.pi
    return pre_perimeter


#Funciones Eje 9
def login(user, passw):
    if user == "usuario1" and passw == "asdasd":
        return True
    else:
        return 0
    

#Funcion Eje 10
def purchase_total(prices_percentages):
    prices=list(prices_percentages.keys())
    percentages=list(prices_percentages.values())
    total=0
    for n in range(len(prices)):
        calculation=prices[n]*(1-percentages[n])
        total+=calculation
    return total


#Funcion Eje 11
def swap(names):
    apply_change = ""
    apply_change = names.swapcase()
    return apply_change


def call_other_f(names):
    change_name = ""
    change_name = swap(names)
    return change_name

#Funcion Eje 12
def phrase_to_dict(phrase):
    new_dict = {}
    temporal_array = phrase.split(" ")
    for word in temporal_array:
        new_dict[word] = len(word)
    return new_dict


#Funcion Eje 13
import math
def calc_modulo_vector(array):
    aux_sum = 0
    for i in array:
        aux_sum += i**2
    modul = math.sqrt(aux_sum)
    return modul


#Funcion Eje 14
def verify_prime_number(num):
    divisors = 0
    for i in range(num, 0, -1):
        if num % i == 0:
            divisors += 1
    if divisors <= 2:
        return True
    else:
        return False


#Funcion Eje 15
def calc_factorial(num):
    fact = 1
    if num == 0:
        fact = 1
    else:
        for i in range(1, num + 1):
            fact *= i
    return fact

def calc_entries(aux_num):
    if aux_num >= 0:
        return 1


#Funcion Eje 16
def separate_num(num):
    aux = list(str(num))
    return aux

def determ_frec(dig, separate_num):
    frec = 0
    for i in separate_num:
        if dig == i:
            frec +=1
    return frec

#Funciones Eje 17
import math
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True




def entering_prime_numbers():
    most_number = 0
    while True:
        num = int(input('Ingresa un numero primo, la lectura finalizara cuando ingreses un numero no primo:\n'))
        if is_prime(num):
            prime_sum = 0
            digit_frecuence = 0
            for digit in str(num):
                prime_sum += int(digit)
            print(f'La suma de los digitos del numero primo ingresado es: {prime_sum}')
            opt_frecuence = input('Ingresa un digito del cual quieres saber la frecuencia en el numero ingresado:\n')
            for digit in str(num):
                if digit == opt_frecuence:
                    digit_frecuence += 1
            if num > most_number:
                most_number = num
            print(f'La frecuencia del digito "{opt_frecuence}" en "{num}" es: {digit_frecuence}')
        else:
            print(f'El numero ingresado no es primo, el mayor numero que ingresaste en esta sesion fue "{most_number}"  y su factorial es: {math.factorial(most_number)}\n Saliendo...')
            break


##Funciones Ejercicios Variables dimensionadas

#Eje 1
#Agregar pasajeros
def add_passengers():
    while True:
        #Ingreso de datos
        person = input("Ingrese su nombre y apellido, DNI y destino: ").title().split(",")
        #Se verifica que no hayan datos faltantes o sobrantes
        if len(person) > 3:
            print(f"Sobran datos \n")
        elif len(person) < 3:
            print("Faltan datos \n ")
        else:
            #se separan los datos en cada variable
            fullname = person[0]
            dni = int(person[1])
            destiny = person[2].strip()
            #se comprueba que los datos ingresados estan correctos
            if valid_dni(dni) == True and len(fullname.split()) == 2:
                break
            else:
                print("Ingrese los datos correctamente. \n")
    #se crea la tupla a retornar con los datos ingresados y verificados
    person_tuple = (fullname, dni, destiny)
    #se retorna la tupla y el destino
    return person_tuple, destiny


#Verificar si existe la ciudad en el registro
def verify_city(city):
        country = input("Ingrese el pais al que pertenece la ciudad: ").title()
        return (city, country)



#agregar ciudades - pais
def add_city():
    while True:
        #Se ingresa una ciudad y un país para registrarlos
        new_entry = input("Ingrese ciudad y país: ").title().split(",")
        #verifica que no se ingresen datos de sobra o que falten
        if len(new_entry) == 2:
            new_entry[1] = new_entry[1].strip()
            new_entry = tuple(new_entry)
            return new_entry
        else:
            print("Ingrese una ciudad/pais válida/o")



#Ver viaje por DNI
def travel_search(persons):
    while True:
        try:
            #Ingresa el DNI a buscar
            search_dni = int(input("Ingrese el DNI de la persona para buscar su destino: "))
            not_found = 0
            #recorre la lista de pasajeros verificando si el DNI coincide
            for i in range(0, len(persons)):
                if persons[i][1] != search_dni:
                    not_found += 1
                elif persons[i][1] == search_dni:
                    found = i
            #si no coincide muestra un msj
            if len(persons) == not_found:
                print("El DNI no está registrado")
                break
            #Si coincide devuelve la persona del DNI y su destino
            else:
                person_travel = persons[found][0]
                travel = persons[found][2]
            print(f"La persona {person_travel}, viaja a {travel}")
            break
        except ValueError:
            print("Ingrese un DNI válido\n")


#Ver cuántos pasajeros viajan a X ciudad.
def cant_passengers_travel(people):
    #se pide la ciudad a buscar
    search_city = input("Ingrese la ciudad a buscar: ").title()
    cant_people = 0
    #Busca en el registro de los pasajeros si alguno viaja a la ciudad
    for i in range(0, len(people)):
        if people[i][2] == search_city:
            #Si hay coincidencias se agrega 1 añ contador de personas
            cant_people += 1
    if cant_people == 0:
        print("No hay pasajeros que viajan a esa ciudad")
    else:
        print(f"{cant_people} pasajeros viajan a esa ciudad")


#Ver cuántos pasajeros viajan a X país
def cant_country_tavel(country_list, people):
    #se pide el país a buscar
    search_country = input("Ingrese el país a buscar: ").title()
    cant_people = 0
    #iterador para la lista de paises-ciudades
    for country in range(0, len(country_list)):
        #iterador para la lista de pasajeros
        for person in range(0, len(people)):
            #Si el pais ingresado es igual a el pais iterado Y la ciudad del pais es igual a el destino de el pasajero se suma 1 al contador de personas
            if country_list[country][0] == people[person][2] and country_list[country][1] == search_country:
                cant_people += 1
    if cant_people == 0:
        print("No hay pasajeros que viajan a ese país \n")
    else:
        print(f"{cant_people} pasajeros viajan a ese país\n")



#Funciones Eje 2
def fact(people):
    adress = set()
    person_position = 0
    j = 0
    while True:
        if j == len(people):
            break
        person = people[j][person_position]
        j += 1
        while j <= len(people):
            
            adress.add((person, people[j-1][3]))
            break
    adress = list(adress)
    return adress


#Funciones Eje 3
#Pagar cuotas
def pay_fee(members):
    while True:
        try:
            member_num = int(input(f"\n Ingrese el N° del socio: "))
            if member_num > len(members):
                print("Ese N° de socio no existe.\n")
                break
            else:
                if members[member_num][2] == "s":
                    print("El socio ya estba al día.\n")
                else:
                    members[member_num][2] = "s"
                    print("Ahora el socio está al día.\n")
                break
        except ValueError:
            print("Ingrese un N° de socio válido")


#Corregir fechas
def fix_date(members):
    dates_to_fix = 0
    for key in members:
        if members[key][1] == "13/03/2018":
            members[key][1] = "14/03/2018"
            dates_to_fix += 1
    if dates_to_fix > 0:
        print("Fechas Corregidas.\n")
    else:
        print("No habian fechas a corregir.\n")


def delete_member(members):
    member_name = input("Ingrese el Nombre y Apellido del socio: ").title()
    succes = 0
    for key in members:
        if members[key][0] == member_name:
            del members[key]
            print(f"El socio {member_name} se ha dado de baja")
            succes += 1
    if succes == 0:
        print(f"No se encontró al socio {member_name}")


def show_members(members):
    for key in members:
        name = members[key][0]
        join_date = members[key][1]
        if members[key][2] == "s":
            fee = "Cuota al día"
        else:
            fee = "Adeuda cuotas"
        print(f"Socio N°{key}, {name}, ingresó: {join_date}, {fee}")


###  Tp N°6   ### 

#Funciones Eje 6 TP6
def capture_names(prompt):
    names = []
    while True:
        name = input(prompt).title
        if name == "X":
            break
        elif len(name.split()) > 1:
            print("Ingrese solamente el nombre de pila")
        else:
            names.append(name)
    return names

#Funcion Eje 7 TP6
def count_characters(phrase_list):
    dic_letters = {}
    for sentence1 in phrase_list:
        for letter1 in sentence1:
            dic_letters[letter1] = 0

    for sentence2 in phrase_list:
        for letter2 in sentence2:
            if letter2 in dic_letters:
                dic_letters[letter2] += 1
    for clave, value in dic_letters.items():
        print(f"El carácter {clave} aparece: {value} veces.")

#Funcion Eje 9 TP6
#Imprime las filas y columnas de una forma mas bonita visualmente
def prin_cards(cards):
    for i in range(len(cards)):
        print(f"{cards[i][0]} {cards[i][1]} {cards[i][2]} {cards[i][3]} {cards[i][4]} {cards[i][5]}   ")


#Coloca los símbolos en posiciones aleatoreas cada vezz que se inicia el juego
import random as ran
def posicionate_characters():
    #lista de símbolos
    char = ["♥", "♠", "♣", "♦", "♫", "۞", "§", "Ŧ", "Ʃ", "♥", "♠", "♣", "♦", "♫", "۞", "§", "Ŧ", "Ʃ"]
    #Mezcla los elementos de la lista de forma aleatoria
    ran.shuffle(char)
    cards = [[], 
        [],
        []
        ]
    #Distribuye los elementos de carácteres en una matriz de 3x3
    for i, select_char in enumerate(char):
        cards[i % 3].append(select_char)
    #Devuelve la matriz 3x3 con los elementos en ella
    return cards


#comprueba que el número ingresado no esté adivinado
def comprb_valid_num(msg, numeros_correctos):
    while True:
        numero = int(input(msg))
        if numero in numeros_correctos:
            print("Ya se adivinó ese número")
        else:
            return numero


#encuentra el símbolo en la posicion pasada por el usuarioy devuelve la lista de "?" con el símbolo en su respectiva posicion
def find_card1(position, enigm, card):
    row = (position -1) // 6
    column = (position - 1) % 6
    enigm[row][column] = card[row][column]
    return enigm


#compara las posiciones ingresadas por el usuario y si son iguales muestra un mensaje y las parejas de cartas adivinadas se mostrarán el resto del juego.
def compare_cards(u_try, u_compare, enimg, card, to_convert, correct):
    row1 = (u_try -1) // 6
    column1 = (u_try - 1) % 6
    row2 = (u_compare -1) // 6
    column2 = (u_compare - 1) % 6
    if card[row1][column1] == card[row2][column2] and u_try != u_compare:
        print("\nCoincidencia!\n")
        enimg[row1][column1] = card[row1][column1]
        enimg[row2][column2] = card[row2][column2]
        to_convert[row2][column2] = "√"
        to_convert[row1][column1] = "√"
        correct = True
    else:
        print("\nNo hay coincidencia :(\n")
        enimg[row1][column1] = "?"
        enimg[row2][column2] = "?"
        correct = False
    return (enimg, to_convert, correct)



#Funciones eje 10 TP6
#Pone en una lista la diagonal de una matriz
def calc_diagonal(matriz):
    matriz_rows = len(matriz)
    diag = []
    i = 0
    while i < matriz_rows:
        diag.append(matriz[i][i])
        i += 1
    return diag

#Pone en una lista la diagonal inversa de una matriz
def calc_inv_diagonal(matriz):
    inv_position = len(matriz) - 1
    i = 0
    inv_diag = []
    while inv_position > i-1:
        inv_diag.append(matriz[inv_position][inv_position])
        inv_position -= 1
    return inv_diag


### Funciones Ejercicio Reursion ###
#funciones Eje 1
import random as ran
def chose_way():
    prob = ran.randint(1,3)
    return prob


def lab_rat(time_rat):
    way = chose_way()
    if way == 3:
        time_rat += 7
        print("La rata escogió el camino 3")
        return time_rat
    elif way == 1:
        time_rat +=3
        print("La rata escogió el camino 1")
        return lab_rat(time_rat)
    elif way == 2: 
        time_rat += 5
        print("La rata escogió el camino 2")
        return lab_rat(time_rat)


#Funcion Eje 2
def f(n):
    s=str(n)
    if len(s) <=1:
        return s
    return s[-1] + f(int(s[:-1]))


### Funciones TP N°8 ###
def count_digits(n):
    s = str(n)
    if len(s) <= 1:
        return 1
    else:
    print()    
    