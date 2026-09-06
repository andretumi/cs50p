def main():
    camel_case = input("camelCase: ")
    to_snake_case(camel_case)


def to_snake_case(camel):
    print("snake_case: ", end="")
    for c in camel:
        if c.isupper():
            c = c.lower()
            print('_' + c, end="")
        else:
            print(c, end="")

    print()


if __name__ == "__main__":
    main()
