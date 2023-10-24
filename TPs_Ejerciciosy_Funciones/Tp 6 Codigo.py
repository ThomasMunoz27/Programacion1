#Ejercicio 1, 2, 3, 4 y 5
import aFunciones as funcion
num_list = []
plus = 0
try:
    while True:
        entry_num = int(input("Ingrese números para ingresarlos en una lista (0 para Salir): "))
        if entry_num == 0:
            break
        else:
            num_list.append(entry_num)


        
    second_entry = int(input("Ingrese otro número para eliminarlo de la lista: "))
    if second_entry in num_list:
        num_list.remove(second_entry)
        for i in num_list:
            plus += i

        print(f"La suma de los números ingresados es: {plus}")
    else: 
        print("No es posible eliminar ese número de la lista")

    new_num = int(input("Ingrese un número para crear una lista con los números de la lista anterior menores a este número: "))
    new_list = []
    for i in num_list:
        if i < new_num:
            new_list.append(i)
    print(new_list)

    new_tuple_list = []
    for i in num_list:
        new_tuple: ()
        frecuency = funcion.determ_frec(i, num_list)
        if (i, frecuency) not in new_tuple_list:
            new_tuple_list.append((i, frecuency))
    print(new_tuple_list)


except ValueError:
    print("Ingrese números solamente")



#Ejericio 6
names_of_prim = funcion.capture_names("Ingrese el nombre de pila de los alumnos de primaria (Ingrese 'x' para finalizar): ")

names_of_sec = funcion.capture_names("Ingrese el nombre de pila de los alumnos de secundaria (Ingrese 'x' para finalizar): ")

if len(names_of_sec) < len(names_of_prim):
    lower = len(names_of_sec)
else:
    lower = len(names_of_prim)

rep_names = []
for i in range(0, lower):
    if names_of_sec[i] in names_of_prim:
        rep_names.append(names_of_sec[i])

print("\nNombres de primaria: ")
for name in names_of_prim:
    if name not in rep_names:
        print(name)

print("\nNombres de secundaria: ")
for names in names_of_sec:
    if names not in rep_names:
        print(names)

print("\nNombres que se repiten: ")
print(rep_names)


#Ejercicio 7
import aFunciones as funcion
phrase_list = []
for i in range(3, 0, -1):
    phrase = input(f"Ingrese {i} oraciones: ")
    phrase_list.append(phrase)
funcion.count_characters(phrase_list)


#Ejercicio 8
#lista de listas de goles de cada equipo:
goal_list=[(0,4,2,1,2,3,1,2,3,0),(5,0,3,2,2,0,0,3,1,2),(0,2,0,1,3,0,1,2,4,2),(1,0,2,0,1,2,3,1,1,0),(1,1,2,1,0,2,1,3,0,3),(1,2,3,1,0,0,2,4,3,1),(4,5,0,0,2,4,0,1,2,1),(2,2,1,0,3,1,3,0,1,1),(0,2,1,0,3,4,5,1,0,2),(0,2,3,3,1,0,0,3,1,0)]


#"Goles de cada equipo:"
print("Goles de cada equipo:")
i=1
for team in goal_list:
    print(f"Equipo {i}: {team}")
    i+=1


# Cantidad de triunfos por equipo
# Total de goles realizados y recividos por equipos
print("-----------------------------")
for i in range(10):
    victory=0
    defeat=0
    tie=0
    goals_scored=0
    goals_against=0
    print(f"partidos del equipo: {i+1}")
    for j in range(10):
        #Total de goles realizados y recividos por equipos
        goals_scored+=goal_list[i][j]
        goals_against+=goal_list[j][i]
        # Cantidad de triunfos por equipo
        if(i!=j):
            if(goal_list[i][j]>goal_list[j][i]):
                victory+=1
            elif(goal_list[i][j]<goal_list[j][i]):
                defeat+=1
            else:
                tie+=1
    print(f"Victorias: {victory}\nDerrotas:{defeat}\nEmpates: {tie}")
    print(f"Total de goles marcados: {goals_scored}\nTotal de goles recibidos: {goals_against}\nPuntos: {victory*3 + tie}\n-----------------------------")


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
            #No permite ingresar un número ya adivinado correctamente
            if coincidence == True:
                list_of_correct_nums.append(user_try)
                list_of_correct_nums.append(user_compare)
            break
        except ValueError:
            print("Ingrese un número del 1 al 18")
        
print("Felicidades has adivinado todos los símbolos!")


#Ejercicio 10
import aFunciones as funcion
first_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diagonal = funcion.calc_diagonal(first_matrix)
print(diagonal)

inv_diagonal = funcion.calc_inv_diagonal(first_matrix)
print(inv_diagonal)


#Ejercicio 11
coin_dictionary = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input("Ingrese el nombre de una divisa: ").title()
if currency in coin_dictionary:
    print(coin_dictionary[currency])
else:
    print("La divisa no está registrada")


#Ejercicio 12
data_user = {"name":None, "age":None, "adress":None, "phone":None}
for key in data_user:
    data_user[key] = input(f"Ingrese su {key}: ")

print(f"{data_user['name']} tiene {data_user['age']} años, vive en {data_user['adress']} y su número de telefono es {data_user['phone']}")


#Ejercicio 13
fruit_dict = {"manzana":15, "Banana":25, "sandia":50, "frutilla":33, "naranja":22}

fruit = input("Ingrese el nombre de una fruta: ").lower()
if fruit not in fruit_dict:
    print("La fruta no se encuentra")
else: 
    kg = float(input("Ingrese la cantidad de kilos a llevar: "))

    final_price = fruit_dict[fruit] * kg
    print(f"El precio de {kg} kilos de {fruit} es {final_price}")
