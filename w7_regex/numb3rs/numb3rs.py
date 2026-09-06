import re
import sys


def main():
    # print(validate(input("IPv4 Address: ").strip()))
    print(validate(sys.argv[1].strip()))


def validate(ip):
    if re.search(r'^(\d+\.){3}\d+$', ip):
        list_of_numbers = list(ip.split('.'))
        for number in list_of_numbers:
            if not 0 <= int(number) <= 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
