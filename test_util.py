import pytest
from util import *


def test_is_float():
    assert is_float(1) == float(1)
    assert is_float(0) == float(0)
    assert is_float(-1) == float(-1)

    assert is_float(None) == None
    assert is_float('2.8') == float('2.8')


def test_calculate_input():
    assert calculate_input(1,2,'+') == float(3)
    assert calculate_input(-1,-2,'+') == float(-3)

    assert calculate_input(1,2,'-') == float(-1)
    assert calculate_input(-1,-2,'-') == float(1)

    assert calculate_input('1',2,'/') == float(1/2)
    assert calculate_input(-1,-2,'/') == float(-1/-2)
    assert calculate_input(3,0,'/') == "Cannot divide by zero!"

    assert calculate_input(-2,-3,'*') == float(6)
    assert calculate_input(4,5,'*') == float(20)

    assert calculate_input(None,None,'/') == "Something went wrong with the calculation!"
    assert calculate_input(None,5,'/') == "Something went wrong with the calculation!"
    assert calculate_input(None,None,None) == "Something went wrong with the calculation!"
    assert calculate_input('4.8','hello','+') == "Something went wrong with the calculation!"
