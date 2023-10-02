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
def validDni(num):
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
def searchLastName(entryName):
    if len(entryName) >= 3:
        return  entryName[2]
    elif len(entryName) == 2:
        return entryName[1]
    
#Obtener los primero 3 números del dni
def getDniId(dni):
    if len(str(dni)) == 8:
        return dni // 100000
    else:
        return dni // 10000

def createId(name, lastName, numId):
    prevId = ""
    prevId += name[0] + str(len(lastName)) + str(numId)
    return prevId


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


#Funcion Eje 16
def separate_num(num):
    aux = list(str(num))
    return aux

def determ_frec(dig, frec, separate_num):
    for i in separate_num:
        if dig == i:
            frec +=1
    return frec