import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            return guess
        except ValueError:
            pass


def check(random_number):
    while True:
        guess = get_guess()
        if guess == random_number:
            print("Just right!")
            break
        elif guess > random_number:
            print("Too Large!")
        else:
            print("Too Small!")


level = get_level()
random_number = random.randint(1, level)
check(random_number)
