#! /usr/bin/env python3
'''
Ask the user for input, modify the return
'''

#print("helloworld")

import sys

global_var = "howdy"

def main(data):
    print_some_word(data)
    data = 'test'
    print_some_word(data)
    
def print_some_word(word):
    print(word)

if __name__ == "__main__":
    someword = 'blue'
    main(someword)


    '''
    def swap_case():

    print("Please enter a string to alter. ")
    start = input(">")
    end = ""

    for letter in start:
        if letter.isupper():
            end += letter.lower()
        elif letter.islower():
            end += letter.upper()
        else:
            end += letter

    return end
    '''