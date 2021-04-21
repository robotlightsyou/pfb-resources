#! /usr/bin/env python3


"""
This program is a basic calculator providing the user addition,
subtraction, multiplication, float division, integer division,
and the modulo operation.
"""


def main():
    """ 
    ask user what function to perform, take input, use control flow to 
    print return of desired function, ask if user wants to continue. If 
    yes, repeat all steps, otherwise exit.
    """
    keep_calculating = True
    while keep_calculating:
        options = {
            "1": add,
            "2": subtract,
            "3": multiply,
            "4": float_divide,
            "5": integer_divide,
            "6": remainder,
            "7": exponent,
        }
        print("Please enter the number of the operation you would like to perform:")
        for key, value in options.items():
            print(f"\t{key}) {value.__name__.capitalize()}")
        # print("\t1) Addition\n\t2) Subtraction\n\t3) Multiplication\n\t4) Division\
        #         \n\t5) Truncating Division\n\t6) Remainder(modulo)\n\t7) Exponents")
        calc_func = input("> ")
        # if calc_func not in [str(i) for i in range(8)]:
        if calc_func not in options:
            print("That was not a valid option, please try again.")
            continue

        print("What is your first number?")
        first_number = input("> ")
        print("What is your second number?")
        second_number = input("> ")
        choice = options[calc_func]
        print(f"The result of {first_number} {choice.__name__} {second_number} is:")

        try:
            first_number, second_number = int(first_number), int(second_number)
        except:
            print("You did not enter valid numbers.")
            continue

        answer = choice(first_number, second_number)
        print(answer)
        print("Would you like to keep calculating?")
        answer = input("> ")
        if answer[0].lower() != "y":
            print("Thank you for using the Python Calculator.")
            keep_calculating = False


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def float_divide(a, b):
    return a / b


def integer_divide(a, b):
    return a // b


def remainder(a, b):
    return a % b

def exponent(a, b):
    return a ** b

if __name__ == "__main__":
    main()