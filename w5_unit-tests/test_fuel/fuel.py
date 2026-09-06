def main():
    while True:
        try:
            result = convert(input("Fraction: "))
            print(gauge(result))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    numerator, denominator = fraction.split('/')
    numerator = int(numerator)
    denominator = int(denominator)
    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator:
        raise ValueError
    return int(round((numerator / denominator), 2) * 100)


def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return 'E'
    elif 99 <= percentage:
        return 'F'


if __name__ == "__main__":
    main()
