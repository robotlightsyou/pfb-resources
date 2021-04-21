__________
### String Methods Project
__________

In this tutorial we'll write a program that changes the case of strings. We'll start by working with individual strings, and work up to a function that takes a string of any length. In this tutorial we'll be discussing strings, string methods, functions, and function arguments. Let's take a look at the code.

__________
#### Basic

```python
#! /usr/bin/env python3
```
We start with a shebang, this just lets your computer know which python to use. The next thing we'll do is take input from the user, in this case we'll ask for a single letter to change the case:

```python
print("Please enter the letter you want altered.")
start_text = input("> ")
```

Once we have the letter we can use string methods and if/elifs to swap the case of the user's input.

```python
if letter.isalpha():
    if letter.isupper():
        print(letter.lower())
    else letter.islower():
        print(letter.upper())
else:
    print("You did not enter a letter.")
```

But we don't actually need all this. Our nested if/else statements run an implicit test on the user's input. If the character they entered is not uppercase and is not lowercase, then it is not a letter and so we don't need the isalpha() test.

```python
if letter.isupper():
    print(letter.lower())
elif letter.islower():
    print(letter.upper())
else:
    print("You did not enter a letter.")
```

Now we can run our file from the command line. Navigate to the directory where your file is saved. You run a python file by typing `python3` and the name of your file. My file is called `swap_case.py`, so I call it in terminal like this:

```shell
/pfb $ python3 swap_case.py
Please ent the letter you want altered.
> h
H
```

__________
#### Adding Complexity

Changing a single character, but wouldn't it be neat if we could do it for whole strings? The answer is a loop. Since we know how long the loop will last(the length of the string), let's use a for loop. Recall that in python for loops might be better named `for each loops`, so we can start a simple for loop to look at each character in our string. This time we'll still ask the user for input, but next we'll declare a variable as an empty string to hold our output. We can then loop over the string and store the modified letters in the output variable to print back to the user at the end. Let's see what that might look like:

```python
#! /usr/bin/env python3


def main():
    print("Please enter a string to alter.")
    start_text = input("> ")
    print(swap_case(start_text))
    
    
def swap_case(string):
    output = ""

    for character in string:
        if character.isupper():
            output += character.lower()
        elif character.islower():
            output += character.upper()
        else:
            output += character

    print output


if __name__ == "__main__":
    main()


```

In this implementation we have moved our steps into a function to make them more easily repeatable. We've also added a main() mostly as form practice, for a script this simple it's not really necessary. In our main function we query the user for input, then pass that string in the function call. Notice the change in variable name: `start_text` holds the user data in the enclosing scope, but `string` will hold any argument that is passed into swap_case(which is only `start_text` in our simple example).

__________
#### Additional Challenges

Since this was a code-along, it's probably wise to push ourselves a little further with some individual practice. Where needed do some extra research and see if you can't achieve this bonus functionality.

* Write a new function that uses the builtin string method that performs the same action

* Write a new function that returns the user's string with case alternating based on whether the character is an even or odd digit index of the string, non-alphabetical characters should remain unaffected(ex: ToO EdGy.)

* Explore the builitn methods and write 3 new functions that implement previously unmentioned methods. 
    examples - if the user's string has more than one word, capitalize the first letter of the second word.
             - if the user's string has more than 5 'y's, return "That's too many Ys."
    You may only use one of these examples. please implement at least 2 that are wholly your own creation. The goal is less about the code, and more about exploring the docs.