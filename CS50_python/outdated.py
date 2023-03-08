months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        m, d, y = date.split("/", maxsplit = 3)
        m = int(m)
        d= int(d)
        break
    except ValueError:
        try:
            m, d, y = date.split()
            if m in months:
                m = 1 + months.index(m)
            d = int(d.rstrip(","))
            break
        except ValueError:
            pass
print(y, end="-")
print(f"{m:02}", end='-')
print(f"{d:02}")