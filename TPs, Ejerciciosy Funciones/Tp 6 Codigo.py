#Ejercicio 7

phrase_list = []
for i in range(3, 0, -1):
    phrase = input(f"Ingrese {i} oraciones: ")
    phrase_list.append(phrase)
    dic_letters = {}
for sentence1 in phrase_list:
    for letter1 in sentence1:
        dic_letters[letter1] = 0
        selec_letter = letter1
        frec = 0

for sentence2 in phrase_list:
    for letter2 in sentence2:
        if letter2 in dic_letters:
            dic_letters[letter2] += 1
for clave, valor in dic_letters
print(f"{clave}: {}")

