#importar funciones
import aFunciones as funcion
import random as ran

#se elije una palabra aleatorea de una lista de palabras
chosen_word = funcion.chose_word()
#se cuenta y almacena la cantidad de letras de la palabra
num_letters = funcion.word_large(chosen_word)
#número de intentos.
attemps = 6
#se crea la palabra pero con las letras reemplazadas por (_)
see_word = funcion.write_(num_letters)
#lista de letras ingresadas que no coinciden con la palabra
incorrect_letters = []
while True:
    aux_errors = 0
    aux_correct = 0
    #si la lista de letras reemplazada es distinta de la palabra entra al condicional
    if (''.join(see_word)) != chosen_word and attemps > 0:
        print(f"La palabra tiene {num_letters} letras. Tienes {attemps} intentos. \n {(' ').join(see_word)}. \nPara ver la letras ingresadas incorrectamente ingrese '0'")
        entry_letter = input("Ingrese la letra a adivinar: ").lower()
        #verifica que se ingrese un input correcto
        if len(entry_letter) > 1:
            print("Por favor, ingrese solo una letra")
            #muestra las letras ingresadas que no coinciden
        elif entry_letter == "0":
            if len(incorrect_letters) == 0:
                print("Todavia no se ingresan letras incorrectas \n ")
            else:
                print(f"\n Las letras incorrectamente ingresadas son:")
                print(incorrect_letters)
                print()
        elif entry_letter == "" or entry_letter == " ":
            print("Por favor, ingrese algúna letra")
        else: 
                for i in range(0, len(chosen_word)):
                    if entry_letter == chosen_word[i]:
                        aux_correct += 1
                        see_word[i] = entry_letter
                    else:
                        aux_errors += 1
                        if aux_errors == len(chosen_word):
                            attemps -= 1
                            print(f"Letra incorrecta.")
                            incorrect_letters.append(entry_letter)
                funcion.timesLetterAppears(aux_correct, entry_letter)
    #Mensaje de Game Over
    elif attemps == 0:
        print(f"PERDISTE, ERES UN FRACASO. La palabra era: \n {chosen_word}")
        break
    #Mensaje de Victoria
    else:
            print(f"\n FELICIDADES!!! \n Has completado la palabra '{chosen_word}' y te sobraron {attemps} intentos. ")
            break
    
print("FIN DEL JUEGO")





