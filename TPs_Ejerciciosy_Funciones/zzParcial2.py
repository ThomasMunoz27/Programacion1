import aFunciones as funcion
#Funciones en la linea 813 del archivo

#No Mutante
'''
no_mutant = [
    "ACTTGA",
    "CAAATA",
    "AAGATA",
    "AGGGTC",
    "TAAACC",
    "ATTAGC"
]
'''
#Mutante horizontal
'''
horizontal_mutant = [
    "ACTTGA",
    "CAAATA",
    "AAAATA",
    "AGAGTC",
    "CCGGGG",
    "ATTAGC"
]
'''
#Mutantee Vertical
'''
vertical_mutant = [
    "ATCGTA",
    "TCTTGA",
    "AAGGTC",
    "AGTGTT",
    "AATGCC",
    "ATGGGC"
]
'''
#Mutante diagonal
'''
diagonal_mutant = [
    "ATCGTA",
    "ACTTGA",
    "CACTTA",
    "ACTGTC",
    "TACACC",
    "ATGCGC"
]
'''
#Mutante de diagnoal inversa
'''
reverse_diag_mutant = [
    "AAACAG",
    "CCCTGC",
    "TTTGTT",
    "GGGATG",
    "AAATAA",
    "CCTTCC"
]
'''
#Mutante Mixto
'''
mixed_mutant =[
    "CAACAG",
    "CCCTGC",
    "CTTGTC",
    "CGGAAG",
    "AAACAA",
    "CCTTCC"
]
'''

print()
#boolean de salida
leave = True
while leave:
#Boolean para verificar si es mutante o no
    mutant = False

#matriz base
    adn = [

    ]

    #Mensaje de bievenida
    print("Bienvenido Sr. Magneto")
    #Iteración para las filas de la matriz
    for i in range(0,6):
            entry_row = funcion.check_letter(f"Ingrese la  fila {i+1} de ADN.\nRecuerde debe utilizar ('A', 'C', 'T' ó 'G'): ")
            adn.append(entry_row)

    mutant = funcion.is_mutant(adn)
#Mensaje de salida en caso de que sea o no sea Mutante
    if mutant == True: 
        print("\n ¡MUTANTE! \n  El último adn ingresado es de un mutante")
    else:
        print("\n Falsa alarma. \n   El adn ingresado no es de mutante.")



        #Pregunta si quiere seguir ingresando adn
    while True:
        hunt = input("Ingrese (1) para terminar y salir a pelear contra los X-Mens\nIngrese (0) para seguir ingresando adn\n :  ")
        if hunt == "1":
            leave = False
            break
        elif hunt == "0":
            break
#Mensaje de salida
print("Saliendo...")