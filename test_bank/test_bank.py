import bank
from bank import value

def main():
    test_hello()
    test_withh()
    test_othercase()

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_withh():
    assert value("harry") == 20
    assert value("h") == 20
    assert value("habit") == 20

def test_othercase():
    assert value("car") == 100
    assert value("cat") == 100
    assert value("dog") == 100

if __name__ == "__main__":
    main()
