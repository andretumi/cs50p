from validator_collection import validators, errors


def main():
    print(validate(input("What's your email address? ").strip()))


def validate(user_input):

    try:
        if validators.email(user_input):
            return "Valid"

    except (errors.EmptyValueError, errors.InvalidEmailError):
        return "Invalid"


if __name__ == "__main__":
    main()
