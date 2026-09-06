def main():
    inputted_text = input("Input: ")
    no_vowels(inputted_text)


def no_vowels(text):
    print("Output: ", end="")

    for c in text:
        if c.lower() in "aeiou":
            continue
        print(c, end="")
    print()


if __name__ == "__main__":
    main()
