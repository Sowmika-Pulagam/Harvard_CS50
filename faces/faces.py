def main():
    face = input("Please give your input: ")
    print(convert(face))


def convert(word):
    word = word.replace(":)","🙂")
    word = word.replace(":(","🙁")
    return word

main()
