import csv
import sys
from tabulate import tabulate

 #print(tabulate(table, headers, tablefmt="grid"))


if len(sys.argv) == 2:
    if ".csv" in sys.argv[1]:
        try:
            with open(sys.argv[1],"r") as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("Not a CSV file")

    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")