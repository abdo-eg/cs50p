from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    # Test valid fractions
    assert convert("3/4") == 75
    assert convert("1/4") == 25

    # Test invalid fractions (should raise ValueError)
    with pytest.raises(ValueError):
        convert("three/four")

    # Test zero denominator (should raise ZeroDivisionError)
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    # Test valid percentage ranges
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"