import random
def main():
    score = 0
    error = 0
    counter = 0
    level = get_level()
    while counter < 10:
        try:
            if error == 0 or error >=3:
                #New problem generation
                GenVal = generate_integer(level)
                error = 0
            answer = int(input(str(GenVal[0]) + ' + ' + str(GenVal[1]) + ' = '))

            if GenVal[0] + GenVal[1] == answer:
                score += 1
                counter += 1
            else:
                error += 1
                print('EEE')

            if error >= 3:
               print( str(GenVal[0]) + ' + ' +  str(GenVal[1]) + ' = ' + str(GenVal[0] + GenVal[1]))
               counter += 1

        except ValueError:
            error += 1
            print('EEE')
            if error >= 3:
               print( str(GenVal[0]) + ' + ' +  str(GenVal[1]) + ' = ' + str(GenVal[0] + GenVal[1]))


    print('Score:',score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except ValueError:
            continue
    return level


def generate_integer(level):
    if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
    elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
    else:
            x = random.randint(100,999)
            y = random.randint(100,999)

    return x,y

if __name__ == "__main__":
    main()

