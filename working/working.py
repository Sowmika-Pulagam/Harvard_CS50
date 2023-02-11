import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])* ([A-P]M)) to (([0-9][0-2]*):*([0-5][0-9])* ([A-P]M))$", s)
    if match:
        work = match.groups()
        if int(work[1]) > 12 or int(work[5]) > 12:
            raise ValueError
        first_hour = new(work[1], work[2], work[3])
        second_hour = new(work[5], work[6], work[7])
        return first_hour + ' to ' + second_hour
    else:
        raise ValueError
def new(hours,minutes, ap_m):
    if ap_m == "PM":
        if int(hours) == 12:
            new_hours = 12
        else:
            new_hours = int(hours) + 12
    else:
        if int(hours) == 12:
            new_hours = 0
        else:
            new_hours = int(hours)
    if minutes == None:
        new_minutes = ':00'
        new_time = f"{new_hours:02}" + new_minutes
    else:
        new_time = f"{new_hours:02}" + ":" + minutes
    return new_time

if __name__ == "__main__":
    main()