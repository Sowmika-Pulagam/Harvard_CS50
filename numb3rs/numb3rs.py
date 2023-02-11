import re
import sys


def main():
     ip = input("IPv4 Address: ").strip()
     print(validate(ip))

def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        split_ip = ip.split(".")
        for i in split_ip:
            if int(i) > 255:
                return False
        return True

    else:
        return False



    #if matches:
        #if int(matches.group(1)) <=255 and int(matches.group(2)) <=255 and int(matches.group(3)) <= 255 and int(matches.group(4)) <=255:
            #return True
        #else:
            #return False
    #else:
        #return False


if __name__ == "__main__":
    main()
