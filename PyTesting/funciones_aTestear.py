# Funciones

#Funcion ahorcado
def word_large(word):
    cant_letters = len(word)
    return cant_letters


#Funcion tp 5 eje 7

def calc_min_and_max(num_list):
    n_min = 100000000000000000
    n_max = -1000000000000
    for i in range(len(num_list)):
        if num_list[i] < n_min:
            n_min = num_list[i]
        elif num_list[i] > n_max:
            n_max = num_list[i]
    return n_min, n_max


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
    
#Funcion tp5 Eje 15
def calc_factorial(num):
    fact = 1
    if num == 0:
        fact = 1
    else:
        for i in range(1, num + 1):
            fact *= i
    return fact


#Funcion tp 5 Eje 16
def separate_num(num):
    aux = list(str(num))
    return aux


#Funcion tp5 Eje 1
def validDni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False
    
#Funciones Tp5 Eje 3
def search_last_name(entryName):
    if len(entryName) >= 3:
        return  entryName[2]
    elif len(entryName) == 2:
        return entryName[1]
    
def get_dni_id(dni):
    if len(str(dni)) == 8:
        return dni // 100000
    else:
        return dni // 10000
    
def create_id(name, last_name, num_id):
    prev_id = ""
    prev_id += name[0] + str(len(last_name)) + str(num_id)
    return prev_id


#Funcion tp5 Eje 8
import math
def calc_area(rad):
    pre_area = 3.14 * (rad**2)
    return pre_area