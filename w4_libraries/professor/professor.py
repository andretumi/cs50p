import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        chances = 3
        while chances != 0:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    chances -= 1
                    if chances == 0:
                        print(f"{x} + {y} = {correct_answer}")
                    else:
                        raise ValueError
            except ValueError:
                print("EEE")
            except EOFError:
                print()
                exit()
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            selected_level = int(input("Level: "))
            if 1 <= selected_level <= 3:
                return selected_level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
