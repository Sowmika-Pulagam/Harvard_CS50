import re
def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        match = re.search(r"https?://(www\.)*youtube\.com/embed/([a-z_A-Z_0-9]+)", s)
        if match:
            watch_s = match.groups()
            return "https://youtu.be/" + watch_s[1]

if __name__ == "__main__":
    main()