### Funciones de Ordenamiento y Busqueda ###

#Burbuja
def bubble_sort(to_order):
    large = len(to_order)
    for i in range(0,large):
        for j in range(0,large):
            if to_order[j] > to_order[i]:
                to_order[i], to_order[j] = to_order[j], to_order[i]
    return to_order


#seleccion
def selection_sort(to_order):
    large = len(to_order)
    for i in range(0, large):
        menor = to_order[i]
        pos = i
        for j in range(i, large):
            if to_order[j] < menor:
                menor = to_order[j]
                pos = j
        if pos != i:
                    to_order[i], to_order[pos] = to_order[pos], to_order[i]
    return to_order


#Insercion
def insert_sort(to_order):
    large = len(to_order)
    for i in range(0, large):
        menor = to_order[i]
        pos = i
        for j in range(pos, large):
            if to_order[j] < menor:
                to_order[i], to_order[j] = to_order[j], to_order[i]
    return to_order


#Merge
def merge_sort(to_order):
    if len(to_order) > 1:
        mid = len(to_order) // 2
        left_half = to_order[:mid]
        right_half = to_order[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
    
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                to_order[k] = left_half[i]
                i += 1
            else:
                to_order[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            to_order[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            to_order[k] = right_half[j]
            j += 1
            k += 1
    return to_order


