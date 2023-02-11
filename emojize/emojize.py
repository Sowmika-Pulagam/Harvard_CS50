from emoji import emojize

def main():
    name = input("Input: ")
    emo(name)

def emo(name):
    result = emojize(name)
    print("Output:",result)

main()