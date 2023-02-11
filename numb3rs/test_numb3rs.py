from numb3rs import validate

def main():
    test_Truenumber()
    test_Falsenumber()
    test_rangenumber()

def test_Truenumber():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"1.2.3.4") == True
    assert validate(r"255.255.255.0") == True

def test_Falsenumber():
    assert validate(r"275.3.6.28") == False
    assert validate(r"1.2") == False
    assert validate(r"1.2.3") == False
    assert validate("cat") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"512.512.512.512") == False
    assert validate(r"1") == False
    assert validate(r"1.1000") == False

def test_rangenumber():
    assert validate(r"500.255.255.255") == False
    assert validate(r"255.500.255.255") == False
    assert validate(r"255.255.500.255") == False
    assert validate(r"255.255.255.500") == False



if __name__ == "__main__":
    main()