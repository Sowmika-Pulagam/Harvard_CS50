def main():
    x = input("Provide the input? ").strip().lower()
    sub(x)

def sub(x):
    match x:
        case "42"|"forty two"|"forty-two":
            print("Yes")
        case _:
            print("No")

main()