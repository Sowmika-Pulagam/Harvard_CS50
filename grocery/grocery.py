
list = {}
while True:
    try:
        x = input()
        if x.upper() in list:
           list[x.upper()] = list[x.upper()] + 1
        else:
            list[x.upper()] = 1

    except EOFError:
        print()
        break


for x in sorted(list.keys()):
    print(list[x],x)
