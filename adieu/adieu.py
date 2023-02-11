import inflect
p = inflect.engine()

emptylist = []
while True:
    try:
        greet = input("Name: ")
        emptylist.append(greet)

    except EOFError:
        print()
        break

output = p.join(emptylist)
print("Adieu, adieu, to " + output)



