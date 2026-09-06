import sys
from tabulate import tabulate
import csv


def main():
    try:
        with open(valid_input(), "r") as file:
            print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist.")


def valid_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] == ".csv":
            return sys.argv[1]
        else:
            sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
