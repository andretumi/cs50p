def main():
    inputted_text = input("Input: ")
    no_vowels_text = shorten(inputted_text)
    print(f"Output: {no_vowels_text}")


def shorten(word):
    no_vowels = ''
    for c in str(word):
        if c.lower() in "aeiou":
            continue
        no_vowels += c
    return no_vowels


if __name__ == "__main__":
    main()
