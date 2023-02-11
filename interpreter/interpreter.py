def main():
    expression = input("Enter an input: ")
    x, y, z = expression.split(" ")
    print("output",interpret(x,y,z))


def interpret(in1,in2,in3):
    if in2 == "+":
        output = float(in1) + float(in3)
    elif in2 == "-":
        output = float(in1) - float(in3)
    elif in2 == "*":
        output = float(in1) * float(in3)
    elif in2 == "/":
        output = float(in1) / float(in3)
    return output


main()


