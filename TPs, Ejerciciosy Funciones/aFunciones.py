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
    word_list = ["sexo", "manzana", "mouse", "baile", "oreja", "rojo", "pierna", "pelo", "gato", "perro", "ciervo", "mora", "girasol", "mate", "eclipse", "piano", "silla", "rata", "pera", "esclavo", "judío", "salchicha", "comida", "zapato", "ñandu", "ñoqui", "queso", "timbre", "tornillo", "invierno", "azucar", "sal", "amanecer", "espía", "iglesia", "operador", "uva", "utensilio", "unicornio", "arco", "margarita", "esternocleidomastoideo", "bailar", "fumar", "alcaucíl", "llovizna"]
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

#mostar la cantidad de veces que aparece la letra ingresada
def timesLetterAppears(aux, letter):
    if aux == 1:
        print(f"\n Correcto!. La palabra lleva una '{letter}'")
    elif aux == 2:
        print(f"\n Correcto!. La palabra lleva dos '{letter}'")
    elif aux == 3:
        print(f"\n Correcto!. La palabra lleva tres '{letter}'")




