#Ejercicio 7
import aFunciones as funcion
phrase_list = []
for i in range(3, 0, -1):
    phrase = input(f"Ingrese {i} oraciones: ")
    phrase_list.append(phrase)
funcion.count_characters(phrase_list)


#Ejercicio 9
import aFunciones as funcion
print("Bienvenid@ al Juego de memoria. ")
cards = funcion.posicionate_characters()
#se le mostrará al usuario para saber visualmente cuanto ha avanzado en el juego
enigm_cards = [["?", "?", "?", "?", "?", "?"], 
                ["?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?"]
                ]

to_adivinate = [[1,2,3,4,5,6],
                [7,8,9,10,11,12],
                [13,14,15,16,17,18]
                ]
#lista de los números ya adivinados correctamente
list_of_correct_nums = []

#mientras todavia no haya adivinado todos los elementos el código se ejecutará
while "?" in [item for row in enigm_cards for item in row]:
    print()
    funcion.prin_cards(to_adivinate)
    while True:
        try:
            coincidence = False

            #el usuario ingresa una posicion a adivinar
            user_try = funcion.comprb_valid_num("Ingrese un número para ver la figura: ", list_of_correct_nums)

            funcion.prin_cards(funcion.find_card1(user_try, enigm_cards, cards))

            print()

            user_compare = funcion.comprb_valid_num("Ingrese un número para comparar la figura: ", list_of_correct_nums)

            funcion.prin_cards(funcion.find_card1(user_compare, enigm_cards, cards))

            print()

            #compara los simbolos de las posiciones, si son iguales se guardan
            enigm_cards, to_adivinate, coincidence = funcion.compare_cards(user_try, user_compare, enigm_cards, cards, to_adivinate, coincidence)
            if coincidence == True:
                list_of_correct_nums.append(user_try)
                list_of_correct_nums.append(user_compare)
            break
        except ValueError:
            print("Ingrese un número del 1 al 18")
        
print("Felicidades has adivinado todos los símbolos!")