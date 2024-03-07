import pytest
import pytest
from my_tiny_service.api.routers.maths import exponentiation, ExponentiationInput

def test_exponentiation():
    # Test positive base and exponent
    input_data = ExponentiationInput(base=2, exponent=3)
    result = exponentiation(input_data)
    assert result.result == 8

    # Test negative exponent
    input_data = ExponentiationInput(base=2, exponent=-2)
    result = exponentiation(input_data)
    assert result.result == 0.25

    # Test zero exponent
    input_data = ExponentiationInput(base=2, exponent=0)
    result = exponentiation(input_data)
    assert result.result == 1

    # Test zero base
    input_data = ExponentiationInput(base=0, exponent=3)
    result = exponentiation(input_data)
    assert result.result == 0
