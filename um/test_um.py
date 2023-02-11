from um import count

def main():
    test_count0()
    test_count1()
    test_count2()

def test_count0():
    assert count("yum") == 0
    assert count("yummy") == 0

def test_count1():
    assert count("um...") == 1
    assert count("Um, Thanks for the album.") == 1

def test_count2():
    assert count("Um, thanks, um...") == 2
    assert count("um, hello, um, world") == 2
    assert count("um, how are you um doing?") == 2

if __name__ == "__main__":
    main()