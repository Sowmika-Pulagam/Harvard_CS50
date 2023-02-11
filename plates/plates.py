def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    charStr = ''
    numStr =''
    charIndex = 0
    numIndex = 0
    #maximum of 6 and minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False
    #plates must start with at least two letters
    if s[0:1].isalpha() == False:
        return False

    #No periods, spaces, or punctuation marks are allowed
    for c in s:
            if c in ['.',':',' ','!','?']:
                return False
            elif c.isalpha():
                charStr += c
                charIndex = s.index(c)
            else:
                numStr += c
                if(numIndex == 0):
                    numIndex = s.index(c)


    if len(numStr) > 0 and int(numStr[0]) == 0:
        return False
    elif charIndex > numIndex and len(numStr) > 0:
        return False

    return True

if __name__ == "__main__":
    main()