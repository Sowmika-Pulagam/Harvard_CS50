from validator_collection import validators, checkers, errors
import validators

def main():
    s = input("What's your email address? ")
    response(s)


def response(s):
    email_add = validators.email(s)
    if email_add:
        print("Valid")
    else:
        print("InValid")

if __name__ == "__main__":
    main()