from utilities.Multiplication import Multiplication
import pytest

@pytest.mark.parametrize("operand1, operand2, result",[(1, 2, 2),(2, 2, 4)])
def test_mul(operand1, operand2, result):
    multiplication = Multiplication()
    assert( multiplication.mul(operand1, operand2) == result)


@pytest.mark.parametrize("numbers, result",[([1, 2, 3], 6)])
def test_mulNum(numbers, result):
    multiplication = Multiplication()
    assert ( multiplication.mulNum(numbers) == result)