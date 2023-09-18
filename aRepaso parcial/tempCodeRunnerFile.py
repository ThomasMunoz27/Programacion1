            name = "thomy"
            print(f"Elejiste juego de palabras, {name}. Procederé a explicarte el funcionamiento")
            print(f"{name}, debes ingresar una frase. Luego se mostrarán la cantidad de cada vocal que contiene la frase \n Empecemos!!!")
            entry_phrase = input(f"{name}, ingresa una frase: ")

            for i in entry_phrase:
                if entry_phrase[i] == "a":
                    a_vowel += 1
                if entry_phrase[i] == "e":
                    e_vowel += 1
                if entry_phrase[i] == "i":
                    i_vowel += 1
                if entry_phrase[i] == "o":
                    o_vowel += 1
                if entry_phrase[i] == "u":
                    u_vowel += 1
            print(f"Muy bien {name}! Veamos los resultados. \n Cantidad de a: {a_vowel} \n Cantidad de e: {e_vowel} \n Cantidad de i: {i_vowel} \n Cantidad de o: {o_vowel} \n Cantidad de u: {u_vowel} \n")