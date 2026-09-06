import os
import sys
from PIL import Image, ImageOps


def main():
    try:
        user_input, user_output = valid_input()
        shirt = Image.open("shirt.png")
        person = Image.open(user_input)
        size = shirt.size
        photo = ImageOps.fit(person, size)
        photo.paste(shirt, shirt)
        photo.save(user_output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def valid_input():
    # if  user does not specify exactly two command-line arguments,
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    _, ext1 = os.path.splitext(sys.argv[1])
    _, ext2 = os.path.splitext(sys.argv[2])
    image_extensions = ['.jpg', '.jpeg', '.png']
    if ext1.lower() not in image_extensions:
        sys.exit("Invalid input")
    elif ext2.lower() not in image_extensions:
        sys.exit("Invalid output")

    # if the input’s name does not have the same extension as the output’s name, or
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()
