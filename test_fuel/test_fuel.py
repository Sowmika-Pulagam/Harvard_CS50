import fuel
import pytest
from fuel import convert, gauge

def main():
    test_input()
    test_full()
    test_Zero()
    test_value()
    test_empty()

def test_input():
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_full():
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
    assert convert("99/100") == 99
    assert convert("1/100") == 1

def test_Zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("hello/hi")


def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


if __name__ == "__main__":
    main()