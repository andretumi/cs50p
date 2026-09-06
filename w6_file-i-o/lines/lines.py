import sys


def main():
    print(count_lines())


def valid_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] == ".py":
            return sys.argv[1]
        else:
            sys.exit("Not a Python file")


def count_lines():
    try:
        file = valid_input()
        counter = 0
        with open(file, "r") as f:
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    counter = counter + 1
        return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
