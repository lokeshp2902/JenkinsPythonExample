from utilities.Division import Division
import pytest

@pytest.mark.parametrize("numerator, denominator, result",[(1,2,1),(1,0,0)])
def test_div(numerator, denominator, result):
    division = Division()
    assert( division.div(numerator, denominator) == result)

