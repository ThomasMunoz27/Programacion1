
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
chosen_word = word_list[r.randrange(0, len(word_list))]
see_word = ""
see_letter = 0

print(f"Usted tiene 10 intentos para adivinar una palabra letra a letra.")
while attemps != 0:
    print(f"\n Tus intentos restantes son: {attemps}")
    current_letter = chosen_word[see_letter]
    attemp = input("Ingrese una letra: ").lower()
    if len(attemp) > 1:
        print("Por favor, ingrese solamente 1 caracter. \n")
    elif attemp == current_letter:
        see_word += current_letter
        see_letter += 1
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
phrase2 = input("Ingrese una frase: ")