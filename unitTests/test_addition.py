from utilities.Addition import Addition
import pytest



@pytest.mark.parametrize("operand1, operand2, result",[(1, 2, 3),(2,2,4),(1,1,2)])
def test_add(operand1, operand2, result):
    addition = Addition()
    print("abcdef")
    assert( addition.add(operand1, operand2) == result )

@pytest.mark.parametrize("numbers, result",[([1, 2, 3], 6)])
def test_addAll(numbers, result):
    addition = Addition()
    assert( addition.addAll(numbers)== result)
