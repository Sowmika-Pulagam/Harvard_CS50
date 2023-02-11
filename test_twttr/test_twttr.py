
from twttr import shorten


def main():
    test_lowerstr()
    test_upperstr()
    test_punc()

def test_lowerstr():
    assert shorten("tests") == "tsts"
    assert shorten("input") == "npt"

def test_upperstr():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("OUTPUT") == "TPT"

def test_num():
    assert shorten("894") == '894'

def test_punc():
    assert shorten("?!.,+") == "?!.,+"


if __name__ == "__main__":
    main()