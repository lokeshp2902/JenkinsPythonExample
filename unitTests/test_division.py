from utilities.Division import Division
import pytest

@pytest.mark.parametrize("numerator, denominator, result",[(1,2,0),(1,1,1)])
def test_div(numerator, denominator, result):
    division = Division()
    assert( division.div(numerator, denominator) == result)

