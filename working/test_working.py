import pytest
from working import convert

def main():
    test_time()
    test_format()
    test_1()
    test_2()

def test_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_format():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

def test_1():
    with pytest.raises(ValueError):
        convert("9 AM - 7 PM")

def test_2():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")

if __name__ == "__main__":
    main()

