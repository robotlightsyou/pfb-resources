#! /usr/bin/env python3
''' 
The above line is called the shebang, it lets your computer know which python to use. We'll
cover the shebang in greater detail later, but for now know that this is the default shebang
for python3 on macs, for the time being we'll start all our files with it.
'''

'''
Next comes imports. In python libraries are sometimes called libraries, sometimes called packages,
but are most commonly called modules. By convention we place module imports at the top of the file
after the shebang, but that's not a rule, and occasionally you will see something imported in
the text of a file(though not commonly, I think this is well accepted as bad style).
'''
from sys import argv

'''
We're only using one function, so I'm importing it directly. We could have imported the 
whole module using:

import sys
'''

# @ TODOS 
# Write a function that takes in a string and returns that string with the case 
# swapped for each letter. Non alphabetical characters remain unaffected

# Write a function that takes in a string and returns all of the even characters in
# uppercase, with the odd indexed characters in lowercase, irrespective of starting
# case. Non alphabetical characters should remain unaffected.

# Write a function that takes in a string and returns the reverse of that string, 
# character case should remain unaffected.

'''
argv is a list of command line arguments that is generated when you run the program.
If python ran the shell, then when you displayed the contents of a directory using
'ls -la', argv == '-la', because that was the argument passed into the command ls.
Alternatively, if we separated the arguments like this 'ls -l -a' where each had a 
space between them, the argv[1] == '-l', and argv[2] == '-a'. argv[0] in python will
always be the name of the file being run(by convention this is true in most programming
languages).

In python we can check the contents of argv using list indexing, the way we might
search for a character using string indexing. In this script we'll be checking the 
value of argv[1], and depending on what the user enters we'll return a different
one of the functions from above. Using the framework below, add the function call 
to print the different returns. To get the string for your functions you should ask
user for input.
'''

# like the shebang, this is a python convention we'll dig into later, but for now
# just get it into your muscle memory.
if __name__ == "__main__":
    # return alternating indexes
    if argv[1] == "-a":
        # your code
    # return swapped case
    elif argv[1] == "-s":
        # your code    
    # return reversed string
    elif argv[1] == "-r":
        # your code       