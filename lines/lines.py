import sys

if len(sys.argv) == 2:
    if ".py" in sys.argv[1]:
        try:
            with open(sys.argv[1],"r") as file:
                lines = 0
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != "":
                        lines = lines + 1
            print(lines)

        except FileNotFoundError:
            sys.exit("Not a python file")


    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
