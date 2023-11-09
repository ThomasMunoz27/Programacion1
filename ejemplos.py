def is_mutant(adn):
# Buscar en las filas y columnas
    for i in range(6):
        # Verificar las filas
        if any(sequence in adn[i] for sequence in ["AAAA", "CCCC", "TTTT", "GGGG"]):
            return True

        # Verificar las columnas
        column = "".join(row[i] for row in adn)
        if any(sequence in column for sequence in ["AAAA", "CCCC", "TTTT", "GGGG"]):
            return True
    # Verificar diagonales (izquierda a derecha, arriba a abajo)
    diagonal_lr = "".join(adn[j][j] for j in range(6))
    print(diagonal_lr)
    if any(sequence in diagonal_lr for sequence in ["AAAA", "CCCC", "TTTT", "GGGG"]):
        return True

    # Verificar diagonales (derecha a izquierda, arriba a abajo)
    diagonal_rl = "".join(adn[k][5 - k] for k in range(6))
    if any(sequence in diagonal_rl for sequence in ["AAAA", "CCCC", "TTTT", "GGGG"]):
        return True

    # Si no se encontraron secuencias mutantes
    return False



'''
#Busca en las columnas si los primeros 4 carácteres son iguales
        elif sum1_columns[i] == a or sum1_columns[i] == c or sum1_columns[i] == t or sum1_columns[i] == g:
            return True

#Busca en las columnas si los 4 cáracteres del medio son iguales
        elif sum2_columns[i] == a or sum2_columns[i] == c or sum2_columns[i] == t or sum2_columns[i] == g:
            return True

#Busca en las columnas si los 4 cáracteres del final son iguales
        elif sum3_columns[i] == a or sum3_columns[i] == c or sum3_columns[i] == t or sum3_columns[i] == g:
            return True
'''
