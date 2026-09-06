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
    middle_endian_date = input("Date: ")
    try:
        if '/' in middle_endian_date:
            month, day, year = middle_endian_date.split('/')
        elif ',' in middle_endian_date:
            middle_endian_date = middle_endian_date.replace(',', '')
            month, day, year = middle_endian_date.split(' ')
            month = (months.index(month)) + 1
        month, day, year = int(month), int(day), int(year)
        if month <= 12 and day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
    except (KeyError, AttributeError, ValueError, NameError):
        pass
    except EOFError:
        break
