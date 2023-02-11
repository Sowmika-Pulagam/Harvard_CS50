
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    out = gauge(percentage)
    print(out)

def convert(fraction):
    while True:
        try:
            X1,Y1 = fraction.split("/")
            X = int(X1)
            Y = int(Y1)
            result = 0
            if X/Y <= 1:
                result = int(round( X/Y * 100))
                return result
            else:
                fraction = input("Fraction: ")

        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()