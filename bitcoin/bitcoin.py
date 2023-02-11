import requests
import sys
def main():
    bitcoin()

def bitcoin():
    if len(sys.argv)== 2:
        print("Missing command-line argument")
        try:
            n = float(sys.argv[1])
        except IndexError:
            print("Command-line argument is not a number")
            sys.exit(1)


#
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        result1 = result["bpi"]["USD"]["rate_float"]
        amount = result1 * n
        print(f"${amount:,.4f}")

    except requests.RequestException:
        sys.exit(1)

main()
