#! /usr/bin/env python3

import random
from random import randint

def main():
    print("basic")
    basic()
    print("advanced")
    advanced()
    print("more advanced")
    more_advanced()

def basic():
    number = randint(1,10)
    guess = ''
    while guess != number:
        print("Please enter a number.")
        guess = int(input("> "))
    
    print(f"{guess} was the correct number.")

def advanced():
    number = randint(1,10)
    guess = ''
    while guess != number:
        print("Please enter a number.")
        guess = int(input("> "))
        if guess > number:
            print(f"{guess} is too high.")
        elif guess < number:
            print(f"{guess} is too low.")
    print(f"{guess} was a match")

def more_advanced():
    number = randint(1,10)
    guess = ''
    while guess != number:
        print("Please enter a number.")
        try:
            guess = int(input("> "))
        except:
            continue
        if abs(number - guess) > 50:
            print(f"{guess} is off.")
        elif guess > number:
            print(f"{guess} is too high.")
        elif guess < number:
            print(f"{guess} is too low.")
    print(f"{guess} was a match.")



if __name__ == "__main__":
    main()