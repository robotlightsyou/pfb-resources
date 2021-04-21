#! /usr/bin/env python3


from sys import exit


def main():
    print("Welcome to the Python Calculator")
    print("Please enter the number of an operation from the list:")
    operations_list = ["Addition", "Subtraction", "Multiplication",
                        "Division", "Truncating Division", "Remainder",
                        "Exponents"]
    for index, operation in enumerate(operations_list):
        print(f"{index + 1}) {operation}")

    try:
        user_choice = int(input("> "))
    except:
        print("You did not choose a valid option.")   
        exit() 
    try:
        print("What is your first number?")
        first_number = int(input("> "))
        print("What is your second number?")
        second_number = int(input("> "))
    except:
        print("You did not enter valid numbers.")   
        exit() 

    if user_choice == 1:
        print(add(first_number, second_number))
    elif user_choice == 2:
        print(subtract(first_number, second_number))
    elif user_choice == 3:
        print(multiply(first_number, second_number))
    elif user_choice == 4:
        print(float_divide(first_number, second_number))
    elif user_choice == 5:
        print(integer_divide(first_number, second_number))
    elif user_choice == 6:
        print(remainder(first_number, second_number))
    elif user_choice == 7:
        print(exponent(first_number, second_number))
    else:
        print("You did not choose a valid option.")


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