def convert(emoji_text):
    emoji_text = emoji_text.replace(":(", "🙁")
    emoji_text = emoji_text.replace(":)", "🙂")
    return emoji_text


def main():
    text = input("please, enter the text: ")
    text = convert(text)
    print(text)

if __name__ == "__main__":
    main()
