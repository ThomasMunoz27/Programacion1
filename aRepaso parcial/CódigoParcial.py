leave_game = ""
#bucle para reiniciar cada vez que se ingrese un valor inválido que interrumpa la ejecución 
name = input("Ingrese su nombre: ")
while leave_game != "no":
    try:
        menu = None
        entry_num = None
        #variables: 1. se iran sumando números impares  2. se almacenará el número mayor   3. la cantidad de números impares ingresados
        odd, higher, cant_odd_nums = 0, 0, 0
        #variables que almacenarán la cantidad de veces que se almacene X vocal 
        a_vowel, e_vowel, i_vowel, o_vowel, u_vowel = 0, 0, 0, 0, 0
        menu = int(input(f"{name}, este es el menú. ¿A qué desea jugar? \n Juego de números(1) \n Juego de palabras(2) "))
        if menu == 1:
            print(f"Elejiste juego de números, {name}. Procederé a explicarte el funcionamiento")
            print(f"{name}, debes ingresar números enteros hasta que ingreses el cero(0). Luego se mostrarán \n El mayor número par y \n El promedio de los números impares. \n Empecemos!!! \n")
            #bucle para ingresar números hasta que se ingrese el 0
            while entry_num != 0:
                entry_num = int(input(f"Vamos, {name}. Ingresa un número: "))
                #si es impar almacena y suma el num impar/ Cuenta la cantidad de nums impares
                if entry_num % 2 == 1:
                    odd += entry_num
                    cant_odd_nums +=1
                #si es par compara si es mas grande que algún número anteriormente ingresado y lo guarda
                elif entry_num % 2 == 0:
                    if entry_num > higher:
                        higher = entry_num
                #saca el promedio de los número impares ingresados
                if cant_odd_nums == 0:
                    cant_odd_nums = 1
                    average = odd / cant_odd_nums
                else:
                    average = odd / cant_odd_nums
            print(f"Excelente {name}, veamos los resultados! \n El mayor número par ingresado fue: {higher}! \n El promedio de los números impares ingresados fue: {average}!")
            #pregunta si quiere volver al menú. Vuelve a preguntar si ingresó algún valor inválido
            while True:
                leave_game = input(f"¿{name}, deseas volver al menú? \n (Si/No): ").lower()
                if leave_game == "si" or leave_game == "no":
                    break
                else:
                    print(f"{name}, por favor ingresa un valor válido")
        #ir al juego de palabras
        elif menu == 2:
            print(f"Elejiste juego de palabras, {name}. Procederé a explicarte el funcionamiento")
            print(f"{name}, debes ingresar una frase. Luego se mostrarán la cantidad de cada vocal que contiene la frase \n Empecemos!!!")
            entry_phrase = input(f"{name}, ingresa una frase: ").lower()
            #recorre la frase en busca de vocales, cuando la encuentra la suma a su respectiva vocal
            for i in entry_phrase:
                if i == "a" or i == "á":
                    a_vowel += 1
                if i == "e" or i == "é":
                    e_vowel += 1
                if i == "i" or i == "í":
                    i_vowel += 1
                if i == "o" or i == "ó":
                    o_vowel += 1
                if i == "u" or i == "ú":
                    u_vowel += 1
            print(f"Muy bien {name}! Veamos los resultados. \n Cantidad de a: {a_vowel} \n Cantidad de e: {e_vowel} \n Cantidad de i: {i_vowel} \n Cantidad de o: {o_vowel} \n Cantidad de u: {u_vowel} \n")
            #pregunta si quiere volver al menú. Vuelve a preguntar si ingresó algún valor inválido
            while True:
                leave_game = input(f"¿{name}, deseas volver al menú? \n (Si/No): ").lower()
                if leave_game == "si" or leave_game == "no":
                    break
                else:
                    print(f"{name}, por favor ingresa un valor válido")

    except ValueError:
        print(f"Ups! Parece que ingresaste un valor inválido. Debemos reiniciar. Lamentamos las molestias, {name}")
print(f"Fin del juego, {name}. Esperamos te hayas divertido :D")