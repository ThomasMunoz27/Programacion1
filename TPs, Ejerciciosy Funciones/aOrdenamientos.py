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
def insertion_sort(to_order):
    for i in range(1, len(to_order)):
        key = to_order[i]  
        j = i - 1  

        while j >= 0 and key < to_order[j]:
            to_order[j + 1] = to_order[j]
            j -= 1

        to_order[j + 1] = key
    return to_order


#Conteo
def counting_sort(arr):
    # Encontrar el valor máximo en la lista para determinar el rango.
    max_value = max(arr)

    # Crear una lista de conteo para contar la frecuencia de cada elemento.
    count = [0] * (max_value + 1)

    # Contar la frecuencia de cada elemento en la lista de entrada.
    for num in arr:
        count[num] += 1

    # Construir la lista ordenada a partir del conteo.
    sorted_arr = []
    for i in range(max_value + 1):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr

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


def mix_sort(to_order):
    num_list = []
    string_list = []

    for i in to_order:
        if type(i) != int:
            string_list.append(i)
        else:
            num_list.append(i)
    
    num_list.sort()
    string_list.sort()

    final_list = num_list + string_list
    return final_list
