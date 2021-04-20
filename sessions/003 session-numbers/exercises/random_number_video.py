#! /usr/bin/env python3

from random import randint

# random.randint(1,10) -> return a random from an inclusive range of the arguments
def main():
    print("running basic")
    basic()
    print("running advanced")
    advanced()
    print("running more advanced")
    more_advanced()

def basic():
    number = randint(1, 10)
    guess = ''
    while guess != number:
        print("Please enter a number.")
        guess = int(input("> "))
    print(f"Congrats! {guess} was the number.")

def advanced():
    number = randint(1, 10)
    guess = ''
    while guess != number:
        print("Please enter a number.")
        guess = int(input("> "))
        if guess > number:
            print("High")
        elif guess < number:
            print("Low")
    print(f"Congrats! {guess} was the number.")

def more_advanced():
    number = randint(1, 100)
    guess = ''
    while guess != number:
        print("Please enter a number.")
        try:
            guess = int(input("> "))
        except:
            print("That was not a valid number. Try again.")
            continue
        if abs(number - guess) > 50:
            print("off")
        elif guess > number:
            print("High")
        elif guess < number:
            print("Low")
    print(f"Congrats! {guess} was the number.")

if __name__ == "__main__":
    main()