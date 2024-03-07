import pytest
from my_tiny_service.api.routers.maths import exponentiation, ExponentiationInput


def test_exponentiation():
    # Test positive numbers
    input_data = ExponentiationInput(base=2, exponent=3)
    result = exponentiation(input_data)
    assert result.result == 8, "Exponentiation of positive numbers failed"

    # Test negative exponent
    input_data = ExponentiationInput(base=2, exponent=-1)
    result = exponentiation(input_data)
    assert result.result == 0.5, "Exponentiation with negative exponent failed"

    # Test zero exponent
    input_data = ExponentiationInput(base=2, exponent=0)
    result = exponentiation(input_data)
    assert result.result == 1, "Exponentiation with zero exponent failed"

    # Test zero base
    input_data = ExponentiationInput(base=0, exponent=2)
    result = exponentiation(input_data)
    assert result.result == 0, "Exponentiation with zero base failed"
