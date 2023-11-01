import random
import aFunciones as funcion


turns = 0

cardboard = [
    [],
    [],
    [],
    [],
    []
]

old_nums = []
outside_nums = []
print("¡Bienvenido al Bingo!")
print("Ingrese 25 números del 1 al 75 para llenar su cartón de Bingo")
#comentario temporal

for i in range(0, 5):
    for j in range(0,5):
        entry_num = funcion.num_check(old_nums, i+1, j+1)
        cardboard[i].append(entry_num)
        old_nums.append(entry_num)
    
print("Iniciando Juego de Bingo\n")
bingo = False
while bingo == False:
    turns += 1
    start = input("Ingrese cualquier tecla para ver que número salió: ")
    if start != "fivhj7baeohyv56bi0pv9ns7vo6ih3svo3":
        while True:
            rand_num = random.randrange(1, 76)
            if rand_num not in outside_nums:
                print(f"Salió el Número {rand_num}!!!")
                break
        outside_nums.append(rand_num)

        cardboard = funcion.fill_board(rand_num, cardboard)

    bingo = funcion.check_bingo(cardboard)
    print(funcion.prin_array(cardboard))

print(f"Felicidades!!! \nLograste hacer Bingo en {turns} turnos")





#"√"