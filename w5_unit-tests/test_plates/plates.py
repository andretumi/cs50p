def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    status = starts_with_two_letters(plate) and valid_length(plate) and end_numbers(plate) \
        and valid_characters(plate) and first_num_non_0(plate)
    return status


# All vanity plates must start with at least two letters.
def starts_with_two_letters(plate):
    return plate[:2].isalpha()


# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters(letters).
def valid_length(plate):
    return 2 <= len(plate) <= 6


# Numbers cannot be used in the middle of a plate(AAA22A); they must come at the end (AAA222).
def end_numbers(plate):
    half = len(plate) // 2
    return not plate[:half].isdigit()


# The first number used cannot be a ‘0’.
def first_num_non_0(plate):
    numbers = ''
    for i in plate:
        if i.isdigit():
            numbers += i
    if len(numbers) > 0 and numbers[0] == '0':
        return False
    else:
        return True


# No periods, spaces, or punctuation marks are allowed.
def valid_characters(plate):
    return plate.isalnum()


if __name__ == "__main__":
    main()
