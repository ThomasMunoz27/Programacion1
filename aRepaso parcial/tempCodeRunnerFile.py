import aFunciones as funcion
print("Bienvenid@ al Juego de memoria. ")
cards = funcion.posicionate_characters()
cards2 = funcion.posicionate_characters()
enigm_cards = [["?", "?", "?"], 
                ["?", "?", "?"],
                ["?", "?", "?"]
                ]
enigm_cards2 = [["?", "?", "?"], 
                ["?", "?", "?"],
                ["?", "?", "?"]
                ]

to_adivinate = [[1,2,3],
                [4,5,6],
                [7,8,9]
                ]
to_adivinate2 = [[1,2,3],
                [4,5,6],
                [7,8,9]
                ]
while True:
    print()
    funcion.prin_cards(to_adivinate)
    while True:
        try:
            user_try = int(input("Ingrese un número para ver la figura: "))
            break
        except ValueError:
            print("Ingrese un número del 1 al 9")
    funcion.prin_cards(funcion.find_card1(user_try, enigm_cards, cards))
    print()


    funcion.prin_cards(to_adivinate2)
    while True:
        try:
            user_compare = int(input("Ingrese un número para comparar la figura: "))
            break
        except ValueError:
            print("Ingrese un número del 1 al 9")
    funcion.prin_cards(funcion.find_card1(user_compare, enigm_cards2, cards2))
    print()

    enigm_cards, enigm_cards2 = funcion.compare_cards(user_try, user_compare, enigm_cards, enigm_cards2, cards, cards2)

    funcion.prin_cards(enigm_cards)
    print("-------")
    funcion.prin_cards(enigm_cards2)