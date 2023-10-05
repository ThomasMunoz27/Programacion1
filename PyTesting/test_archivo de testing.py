import pytest
from funciones_aTestear import *
import random as ran
#Funcion ahorcado
@pytest.mark.parametrize("palabra, resp",[
    ("Ruth", 4),
    ("Paula", 5),
    ("Rodrigo", 7),
])
def test_word_large(palabra, resp):
    assert word_large(palabra) == resp


#Funcion tp 5 eje 7
@pytest.mark.parametrize("lista_numeros, resp, resp2",[
    ([1, 5, 8, 10, 7, 9, -2], -2, 10),
    ([10, 55, 4444, -86, 99], -86, 4444)
])
def test_calc_min_and_max(lista_numeros, resp, resp2):
    assert calc_min_and_max(lista_numeros) == (resp, resp2)


#funcion tp5 eje 14
@pytest.mark.parametrize("primo, respu",[
    (2, True),
    (4, False),
    (11, True),
    (22, False),
])
def test_verify_prime_number(primo, respu):
        assert verify_prime_number(primo) == respu


#Funcion tp 5 Eje 16
@pytest.mark.parametrize("num, resp",[
    (12, ["1", "2"]),
    (159, ["1", "5", "9"])

])
def test_separate_num(num, resp):
    assert separate_num(num) == resp


#Funcion tp5 Eje 15
@pytest.mark.parametrize("num, resp",[
    (5, 120),
    (6, 720),
    (7, 5040)
])
def test_calc_factorial(num, resp):
    assert calc_factorial(num) == resp


#Funcion tp5 Eje 1
@pytest.mark.parametrize("num, resp",[
    (94219667, True),
    (9, False),
    (41417055, True),
])
def test_validDni(num, resp):
    assert validDni(num) == resp


#Funcion Tp5 Eje 3
@pytest.mark.parametrize("name, resp",[
    (["Ruth", "Condorí"], "Condorí"),
    (["Thomas", "Nicolas", "Muñoz"], "Muñoz")
])
def test_search_last_name(name, resp):
    assert search_last_name(name) == resp


@pytest.mark.parametrize("dni, resp",[
    (94219667, 942),
    (9421966, 942),
])
def test_get_dni_id(dni, resp):
    assert get_dni_id(dni) == resp


@pytest.mark.parametrize("name, last_name, num_id, resp",[
    (["Paula", "Geier"], "Geier", 445, "Paula5445"),
    (["Thomas", "Nicolas", "Muñoz"], "Muñoz", 942, "Thomas5942")
])
def test_create_id(name, last_name, num_id, resp):
    assert create_id(name, last_name, num_id) == resp



#Funcion tp5 Eje 8
@pytest.mark.parametrize("rad, resp",[
    (5, 78.5),
    (3, 28.26)

])
def test_calc_area(rad, resp):
    assert calc_area(rad) == resp