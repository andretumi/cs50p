import random


while True:
    try:
        level = int(input("Level: "))
        secret = random.randint(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess == secret:
                print("Just right!")
                raise EOFError
            elif guess > secret:
                print("Too large!")
            elif guess < secret:
                print("Too small!")
            else:
                pass

    except ValueError:
        pass

    except EOFError:
        print()
        break
