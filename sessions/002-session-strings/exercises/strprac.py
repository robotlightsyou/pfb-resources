#! /usr/bin/env python3

from sys import argv

# start = input("Please enter a string")


def swapif(string):
    output = ""
    for letter in string:
        if letter.isupper():
            output += letter.lower()
        elif letter.islower():
            output += letter.upper()
        else:
            output += letter
    return output


def swapcase(string):
    output = ""
    for letter in string:
        output += letter.swapcase()
    return output


def alternate(string):
    output = ""
    for index, letter in enumerate(string):
        if index % 2 == 0 and letter.isalpha():
            output += letter.upper()
        elif index % 2 != 0 and letter.isalpha():
            output += letter.lower()
        else:
            output += letter
    return output


def ireverse(string):
    output = ""
    for i in range(len(string)):
        output += string[-i-1]
    return output


def greverse(string):
    return string[::-1]

# print(swapif('This Is a sTring to AlterNate.'))
# print(swapcase('This Is a sTring to AlterNate.'))
# print(alternate('This Is a sTring to AlterNate.'))


if __name__ == "__main__":
    if argv[1] == "-a":
        print(alternate(input(">")))
    elif argv[1] == "-s":
        print(swapcase(input(">")))
    elif argv[1] == "-i":
        print(ireverse(input(">")))
    elif argv[1] == "-g":
        print(greverse(input(">")))
