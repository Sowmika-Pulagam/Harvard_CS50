import random
def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                Levelval = random.randint(1,level)
                Guess(Levelval)
                break
        except ValueError:
            continue


def Guess(Levelval):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < Levelval:
                    print("Too small!")
                elif guess > Levelval:
                    print("Too large!")
                else:
                    sys.exit("Just right!")
                    break
        except ValueError:
            continue

main()






