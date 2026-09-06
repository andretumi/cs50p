import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(url):
    if url.startswith("<iframe"):
        if matches := re.search(r'youtube\.com/embed/(\w+)', url, re.IGNORECASE):
            return f"https://youtu.be/{matches.group(1)}"

    else:
        return None


if __name__ == "__main__":
    main()
