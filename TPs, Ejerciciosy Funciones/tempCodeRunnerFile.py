import aFunciones as funcion
print("Bienvenid@ al Juego de memoria. ")
cards = funcion.posicionate_characters()
enigm_cards = [["?", "?", "?", "?", "?", "?"], 
                ["?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?"]
                ]

to_adivinate = [[1,2,3,4,5,6],
                [7,8,9,10,11,12],
                [13,14,15,16,17,18]
                ]

list_of_correct_nums = []

while "?" in [item for row in enigm_cards for item in row]:
    print()
    funcion.prin_cards(to_adivinate)
    while True:
        try:
            coincidence = False
            while True:
                user_try = int(input("Ingrese un número para ver la figura: "))
                if user_try in list_of_correct_nums:
                    print("Ya se adivinó ese número")
                else:
                    break
            funcion.prin_cards(funcion.find_card1(user_try, enigm_cards, cards))
            print()
            while True:
                user_compare = int(input("Ingrese un número para comparar la figura: "))
                if user_compare in list_of_correct_nums:
                    print("Ya se adivinó ese número")
                else:
                    break
            funcion.prin_cards(funcion.find_card1(user_compare, enigm_cards, cards))
            print()
            enigm_cards, to_adivinate, coincidence = funcion.compare_cards(user_try, user_compare, enigm_cards, cards, to_adivinate, coincidence)
            if coincidence == True:
                list_of_correct_nums.append(user_try)
                list_of_correct_nums.append(user_compare)
            break
        except ValueError:
            print("Ingrese un número del 1 al 18")
        
print("Felicidades has adivinado todos los símbolos!")