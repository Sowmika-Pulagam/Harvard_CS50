def main():
    out = input("Date: ")
    mon = ["January","February",
    "March","April",
    "May","June",
    "July","August",
    "September","October",
    "November","December" ]
    d(out)

def d(out):
    while True:
        if "/" in out:
            try:
                month,day,year = out.split("/")
                if (int(month) >= 1 and int(month)) <= 12 and (int(day) >=1 and int(day)<= 31):
                    break

            except:
                pass
        else:
            try:
                out = out.replace(",","")
                month1,day1,year1 = out.split(" ")
                if month1 in mon:
                    month1 = mon.index(month1) + 1
                elif int(month1) >= 1 and int(month1) <= 12:
                    break
                elif int(day1) >=1 and int(day1)<= 31:
                    break

            except ValueError:
                print()
                pass

print(f"{int(month):02}-{int(day):0.2}")

main()