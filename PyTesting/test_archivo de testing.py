import pytest
from PyTesting.funciones_aTestear import *
import random as ran

@pytest.mark.parametrize("palabra, resp",[
    ("Ruth", 4),
    ("Paula", 5),
    ("Rodrigo", 7),
])
def test_word_large(palabra, resp):
    cant_letters = len(palabra)
    assert word_large(palabra) == resp