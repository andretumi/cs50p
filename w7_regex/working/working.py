import re


def main():
    print(convert(input("Hours:").strip()))


def convert(time_input):
    if matches := re.fullmatch(r'(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)', time_input, re.IGNORECASE):
        str_hour, str_min, str_per, end_hour, end_min, end_per = matches.groups()
        if str_min is None and end_min is None:
            str_min, end_min = 0, 0
        str_hour, str_min, end_hour, end_min = map(int, [str_hour, str_min, end_hour, end_min])

        if str_per == 'PM' and str_hour != 12:
            str_hour += 12
        elif str_per == 'AM' and str_hour == 12:
            str_hour = 0
        if end_per == 'PM' and end_hour != 12:
            end_hour += 12
        elif end_per == 'AM' and end_hour == 12:
            end_hour = 0

        if not 0 <= str_hour <= 23 or not 0 <= end_hour <= 23 or not 0 <= str_min <= 59 or not 0 <= end_min <= 59:
            raise ValueError("Invalid arguments")

        return f"{str_hour:02d}:{str_min:02d} to {end_hour:02d}:{end_min:02d}"

    else:
        raise ValueError("Invalid format")


if __name__ == "__main__":
    main()
