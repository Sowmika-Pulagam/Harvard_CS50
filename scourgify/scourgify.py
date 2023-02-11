import csv
import sys

students = []
if len(sys.argv) == 3:
    if ".csv" in sys.argv[1]:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    names_split = row["name"].lstrip().split(",")
                    students.append({"last": names_split[0], "first": names_split[1], "house": row["house"]})


        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


with open(sys.argv[2],"w") as afterfile:
    writer = csv.DictWriter(afterfile, fieldnames=["first","last","house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in students:
        writer.writerow({"first": row["first"].strip(), "last": row["last"].strip(), "house": row["house"].strip()})


if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")
elif ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")
elif len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
