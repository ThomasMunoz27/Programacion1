import pytest
from funciones_aTestear import *
import random as ran

@pytest.mark.parametrize("palabra, resp",[
    ("Ruth", 4),
    ("Paula", 5),
    ("Rodrigo", 7),
])
def test_word_large(palabra, resp):
    cant_letters = len(palabra)
    assert word_large(palabra) == resp

'''
@pytest.mark.parametrize("lista_numeros, resp, resp2",[
    ([1, 5, 8, 10, 7, 9, -2], 10, -2)
])
def test_calc_min_and_max(lista_numeros, resp, resp2):
    n_min = 100000000000000000
    n_max = 0
    for i in range(len(lista_numeros)):
        if lista_numeros[i] < n_min:
            n_min = lista_numeros[i]
        elif lista_numeros[i] > n_max:
            n_max = lista_numeros[i]
    assert calc_min_and_max(lista_numeros) == resp, resp2
'''

@pytest.mark.parametrize("primo, respu",[
    (2, True),
    (4, False),
    (11, True),
    (22, False),
])
def test_verify_prime_number(primo, respu):
    divisors = 0
    for i in range(primo, 1, -1):
        if primo % i == 0:
            divisors += 1
    if divisors <= 2:
        assert verify_prime_number(primo) == respu
    else:
        assert verify_prime_number(primo) == respu