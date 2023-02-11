import plates
from plates import is_valid

def main():
    test_char()
    test_start()
    test_zero()
    test_plate()
    test_punctuation()

def test_char():
    assert is_valid("HELLO") == True
    assert is_valid("PLATE") == True
    assert is_valid("P") == False

def test_start():
    assert is_valid("CS") == True
    assert is_valid("A2") == False
    assert is_valid("CS50") == True
    assert is_valid("2A") == False

def test_zero():
    assert is_valid("ST04") == False
    assert is_valid("AA20") == True

def test_plate():
    assert is_valid("AAA222") == True
    assert is_valid("AB122") == True
    assert is_valid("AA22A") == False

def test_punctuation():
    assert is_valid("AA.2") == False
    assert is_valid("AA 2") == False
    assert is_valid("BB!1") == False
    assert is_valid("CC:3") == False

if __name__ == "__main__":
    main()