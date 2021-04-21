__________
### The Python Calculator Project
__________

This project will cover a number of topics, but our primary focus is to use control flow to
act upon the user's input, call the correct function, and return to the user their answer. We 
are given some source code as a guide with some notes, but the implementation is entirely up to 
you. There are no restrictions, as long as the program takes the user's input and prints the 
correct response it is successful. Lets take a closer look.

The source code distributed to us is pretty bare, but we are given 7 function definitions to fill
in. These represent some of the basic operators available to python, though there are others you 
may include in your calculator if you wish to challenge yourself. We also see something new, a try/except block.

#### Try/Except
__________

Try blocks are used to test if an action will perform successfully without crashing the program. A 
good general rule is to try and limit the amount of clauses within a try block so that if there is 
an error it will be easy to locate. In our program we will use a try block to get input from the user. We'll be using only numbers as inputs, so if the user puts anything else in our program will crash when we try to convert it from a string. To avoid this we'll enclose our data coercion in a try block to prevent the user from seeing an error, and to handle it cleanly.

'''python
try:
    user_choice = input("> ")
except:
    # How to handle?
'''

Do some reading on error handling and decide what would be an appropriate action to take if the user gives you bad input. The choice is up to you, but if you're stuck just exit the program.

__________
#### The Task

First we'll need to fill out the function definitions. All we need to do is fill in the operators with their respective function. Once we've done that we can begin working on main. Let's start by printing the options for the users as a numbered list(**Bonus Challenge #1**). We can then ask them to enter the number of their operation. Numbers are easier to deal with, we don't have to worry about the user misspelling or using the wrong case. Once we've printed the options we can use a try block to get the user's input. We'll also need to get to additional numbers from the user to use in the operation. Last, when we have their choice and their numbers, we can call the appropriate function and print the result(**Bonus Challenge #2**).


**Bonus Challenge #1**: Rather than hardcode the menu, try to store the options in a data structure, then loop over that object and print a formatted string with the numbered options.
**Bonus Challenge #2**: The basic task is to run one operation each time the program is run, can you make it so that the program runs continuously prompting the user for when to quit?