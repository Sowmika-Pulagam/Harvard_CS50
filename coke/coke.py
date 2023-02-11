def main():
    AmountDue = 50
    print("Amount Due:",AmountDue)
    charge(AmountDue)

def charge(AmountDue):
    while AmountDue > 0:
        coin = int(input("Insert Coin: "))
        if coin in [25,10,5]:
            AmountDue = AmountDue - coin
            if AmountDue < 0 :
                print("Change Owed:",abs(AmountDue))
            else:
                print("Amount Due:",AmountDue)
        else:
            print("Amount Due:",AmountDue)


if __name__ == "__main__":
    main()


