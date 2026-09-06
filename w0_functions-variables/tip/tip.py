def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.replace('$', ''))
    return d


def percent_to_float(p):
    # converting the value of p to float and removing the % character
    p = float(p.replace('%', ''))
    # converting p into a usefully mathematical value
    p = p / 100
    return p


if __name__ == "__main__":
    main()
