from datetime import date
import sys
import inflect
p = inflect.engine()


def main():
    print(to_text(minutes_alive()))


def minutes_alive():
    today = date.today()
    try:
        date_input = date.fromisoformat(input("Date of Birth: ").strip())
        if today < date_input:
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")
    return (today - date_input).days * 24 * 60


def to_text(minutes):
    word = p.number_to_words(minutes, andword='')
    return f"{word.capitalize()} minutes"


if __name__ == "__main__":
    main()
