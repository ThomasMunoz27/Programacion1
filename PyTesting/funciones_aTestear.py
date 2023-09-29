# Funciones

#Funcion ahorcado
def word_large(word):
    cant_letters = len(word)
    return cant_letters


#Funcion tp 5 eje 7
'''
def calc_min_and_max(num_list):
    n_min = 100000000000000000
    n_max = 0
    for i in range(len(num_list)):
        if num_list[i] < n_min:
            n_min = num_list[i]
        elif num_list[i] > n_max:
            n_max = num_list[i]
    return n_min, n_max
'''

#funcion tp5 eje 14
def verify_prime_number(num):
    divisors = 0
    for i in range(num, 0, -1):
        if num % i == 0:
            divisors += 1
    if divisors <= 2:
        return True
    else:
        return False