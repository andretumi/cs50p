def main():
    # asking user to input time (str)
    time_input = input("What time is it? ")
    # calling convert function
    daytime = convert(time_input)
    # conditionals to define the respective meal time
    if 7 <= daytime <= 8:
        print("breakfast time")
    elif 12 <= daytime <= 13:
        print("lunch time")
    elif 18 <= daytime <= 19:
        print("dinner time")


def convert(time):
    # conditional to execute in case time is in 12h format (ends whit m.)
    if time.endswith('m.'):
        # in case is a.m.
        if "a.m." in time:
            # removing a.m. from time string
            time = time.replace("a.m.", '')
            # splits the input and assigns the value to the corresponding hours and minutes
            hours, minutes = time.split(':')
        # in case is p.m.
        elif "p.m." in time:
            # removing p.m. from time string
            time = time.replace("p.m.", '')
            # splits the input and assigns the value to the corresponding hours and minutes
            hours, minutes = time.split(':')
            # adding 12 to change to 24h format, because it is p.m.
            hours = int(hours)
            hours += 12

    # conditional default to execute in case time is in 24h format
    else:
        # splits the input and assigns the value to the corresponding hours and minutes
        hours, minutes = time.split(":")

    # casting hours to float
    hours = float(hours)
    # casting minutes to float.
    minutes = float(minutes)
    # dividing minutes by 60 to get the decimal hours and rounding it to 2 decimals
    decimal_hours = round((minutes / 60), 2)
    # adding the whole number to the decimals to get the total number of hours(float)
    hours = hours + decimal_hours
    return hours


if __name__ == "__main__":
    main()
