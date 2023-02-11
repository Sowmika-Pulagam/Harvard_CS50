def main():
    word = str(input("Input: "))
    result = shorten(word)
    print("Output:",result)

def shorten(word):
    result = ''
    for letter in word:
        if not letter.lower() in ['a','e','i','o','u']:
            result = result + letter
    return result


if __name__ == "__main__":
    main()