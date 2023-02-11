from seasons import birthdate

def main():
    test_birthdate()

def test_birthdate():
    assert birthdate('1998-07-03') == ('1998','07','03')
    assert birthdate('2000-07-13') == ('2000','07','13')


if __name__ == "__main__":
    main()