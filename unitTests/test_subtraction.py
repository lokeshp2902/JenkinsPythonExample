from utilities.Subtraction import Subtraction
import pytest


@pytest.mark.parametrize("operand1, operand2, result",[(1, 2, 1),(1,1,0)])
def test_sub(operand1, operand2, result):
    subtraction = Subtraction()
    assert (subtraction.sub(operand1, operand2) == result)
