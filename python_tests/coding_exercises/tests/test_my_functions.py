import pytest

from src.my_functions import *

def test_add():
    result = add(number_one=1, number_two=4)
    # pytest checks whether this statement is True
    # if not it returns tha test fail
    assert result == 5


def test_divide():
    result = divide(number_one=10, number_two=5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(number_one=10, number_two=0)


def test_add_strings():
    result = add(number_one="i like", number_two=" burgers")
    assert result == "i like burgers"