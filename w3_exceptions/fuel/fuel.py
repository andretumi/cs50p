def main():
    # assigns the returning value of catch_errors() to x (numerator) and y (denominator)
    x, y = catch_errors()
    # first, rounds the result of x/y to only two decimals and round to the nearest integer
    # second, multiplies the result by 100 and casts it to int to get a percentage (0.23 -> 23)
    # finally, assigns the final result to the variable percentage
    percentage = int(round((x / y), 2) * 100)
    # prints the percentage in format (z%)
    if 1 < percentage < 99:
        percentage = str(percentage)
        print(percentage + '%')
    # prints E in case percentage is below 1
    elif percentage <= 1:
        print('E')
    # prints F in case percentage in above 99
    elif 99 <= percentage:
        print('F')


# function that handles ValueError and ZeroDivisionError, and reprompts in case of wrong input
def catch_errors():
    while True:
        # asking user to input a fraction (x/y)
        fraction = input("Fraction: ")
        try:
            # splitting the input (str) and assigning the respective values to numerator and denominator
            numerator, denominator = fraction.split('/')
            # casting to int, to test not int value (two/four) : ValueError
            numerator = int(numerator)
            denominator = int(denominator)
            # testing denominator : ZeroDivisionError
            if numerator <= denominator != 0:
                return numerator, denominator
        # handles errors and prints a hint message to help user
        except ValueError:
            print("Please enter valid integers for the numerator and denominator.")
            pass
        except ZeroDivisionError:
            print("The denominator cannot be zero.")
            pass


if __name__ == "__main__":
    main()
