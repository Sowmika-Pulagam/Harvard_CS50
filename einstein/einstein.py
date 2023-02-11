def main():
    mass = int(input("m: "))
    print("E:", einstein(mass))


def einstein(mass):
    c = 300000000
    return mass * (c**2)

main()