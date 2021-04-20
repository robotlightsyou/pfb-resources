#! /usr/bin/env python3

'''
# start with getting a string from the user
start = input("Please enter the text you want altered: ")

# you have to declare your variable before you can add to it in the loop
output = ""

for letter in start:
    # check the case of the character and return opposite if alphabetical
    # isupper/islower are implicit isalpha checks as not letters aren't cased.
    if letter.isupper():
        output += letter.lower()
    elif letter.islower():
        output += letter.upper()
    else:
        output += letter

print(output)
'''
#Now lets try putting that into a function so you can call it multiple times

def swap_case(string):

    output = ""
    for letter in string:
        if letter.isupper():
            output += letter.lower()
        elif letter.islower():
            output += letter.upper()
        else:
            output += letter
    return output

print(swap_case(input("Please enter the text you want altered: ")))


'''
Next Steps:
- rewrite function with the built in string.method that produces the same output
- write a new function that returns alternating letters based on even/odd index, or to return the reverse of a string(hint:indexing and slicing)
- Create a function, it should use if/elif/else statements to do at least 3 different outputs based on the user's input. Some examples:
    if the user's string has more than one word, capitalize the first letter of the second word.
    if the user's string has more than 5 'y's return "That's too many 'y's."
- The goal here is less to write a useful program and more to explore the different methods and get a little experience with control flow.
'''