from project import addition
from project import evaluation_fun

def main():
    test_function_1()
    test_function_2()


def test_function_1():
    assert addition([2, 3, 5]) == 10
    assert addition((1, 2, 5)) == 8


def test_function_2():
    assert evaluation_fun("7+3-5") == 5
    assert evaluation_fun("8-2/3") == 2


if __name__ == "__main__":
    main()
