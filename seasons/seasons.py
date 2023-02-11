from datetime import date
import re
import sys
import inflect
p = inflect.engine()


def main():
    s= input("Date of Birth: ")
    birth(s)

def birth(s):
    try:
        year, month, day = birthdate(s)
    except:
        sys.exit("Invalid date1")

    DOB = date(int(year), int(month), int(day))
    #print(DOB)
    #todaydate = date.fromisoformat("2000-01-01")
    todaydate =date.today()
    difference = todaydate - DOB
    cal_minutes = difference.days * 24 * 60
    result = p.number_to_words(cal_minutes, andword="") + " minutes"
    print(result.capitalize())


def birthdate(s):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", s):
        year, month, day = s.split("-")
        return year,month,day


if __name__ == "__main__":
    main()