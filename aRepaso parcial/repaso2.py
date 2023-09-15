
#Ejercicio 1
phrase = input("Ingrese una frase o palabra: ")
if len(phrase) == 4:
    print(f"{phrase}!")
else:
    print(f"{phrase}?")


#Ejercicio 2
import random as r
word_list = ["sexo", "manzana", "mouse", "baile", "oreja", "rojo", "pierna", "pelo", "gato", "perro", "ciervo", "mora", "girasol", "mate", "eclipse", "piano", "silla", "rata", "pera", "escalvo", "judío", "salchicha", "comida", "zapato", "ñandu", "ñoqui", "queso", "timbre", "tornillo", "invierno", "azucar", "sal", "amanecer", "espía", "iglesia", "operador", "uva", "utensilio", "unicornio", "arco"]
attemps = 15
#elejir una palabra de la lista
chosen_word = word_list[r.randrange(0, len(word_list))]
#variable para ver como se completala palabra letra a letra
see_word = ""
#contador para veriicar la letra correcta
see_letter = 0

print(f"Usted tiene 10 intentos para adivinar una palabra letra a letra.")
while attemps != 0:
    print(f"\n Tus intentos restantes son: {attemps}")
    #elije la letra a adivinar de la vuelta del while
    current_letter = chosen_word[see_letter]
    attemp = input("Ingrese una letra: ").lower()
    #verificar que se ingrese 1 solo carácter
    if len(attemp) > 1:
        print("Por favor, ingrese solamente 1 caracter. \n")
    elif attemp == current_letter:
        #agrega la letra de la palabra para verla
        see_word += current_letter
        #cambia la letra a verificar
        see_letter += 1
        #verifica que no busque una letra fuera del rango de la palabra
        if see_letter > len(chosen_word)-1:
            print(f"Felicidades!!!. La palabra es: {see_word} \n Te sobraron {attemps} intentos")
            break
        else:
            print(f"Correcto! La palabra incompleta es: \n {see_word}")
    elif attemp != current_letter:
        
        attemps -= 1
        print("INCORRECTO")
        if attemps == 0:
            print("PERDISTE.TU MAMÁ MUERE")

print("Fin del juego")

#Ejercicio 3
phrase2 = input("Ingrese una frase: ").split()
cant_words = len(phrase2)
print(f"Usted ingresó {cant_words} palabras")


#Ejercicio 4
salary = 20000
aux = 0
conf_asist = input("¿Asistió todo el més? \n (Si/No): ").lower
if conf_asist == "si":
    while aux == 0:
        extra_hours = int(input("¿Cuantas horas trabajó los domingos? (min:3 Max:10)"))
        if extra_hours < 3 or extra_hours > 10: 
            print("Cantidad de horas extra ingresadas inválido. Ingrese de vuelta. \n")
        elif extra_hours >=3 or extra_hours <= 5:
            salary += salary * 0.03
            break
        elif extra_hours >=6 or extra_hours <= 10:
            salary += salary * 0.1
            break

elif conf_asist == "no":
    while aux == 0:
        extra_hours = int(input("¿Cuantas   horas trabajó los domingos?(Min:3 Max:10)"))
        if extra_hours < 3 or extra_hours > 10: 
                print("Cantidad de horas extra ingresadas inválido. Ingrese de vuelta. \n")
        else:
            salary += salary * 0.02
            break


print(f"Su salario final es de {salary}")
