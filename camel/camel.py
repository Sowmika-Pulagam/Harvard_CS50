def main():
    word = input("camelCase: " )
    print("snake_case:",case(word))

def case(word):
    result =''
    for letter in word:
        if letter == letter.upper():
            letter = '_' + letter.lower()
        result += letter
    return result



if __name__ == "__main__":
    main()
