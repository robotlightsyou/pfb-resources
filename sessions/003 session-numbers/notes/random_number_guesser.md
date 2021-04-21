__________
### Random Number Project
__________

In this project we'll be using the Random module to generate random numbers and then have our user guess them. We'll look at a couple different levels of difficulty, starting with a very basic implementation, but advancing to a more robust version complete with input validation and feedback. Lets take a closer look at the problem.

__________
#### Importing

In order to use the Random module we'll first have to import it. We have to options, we can import the entire module, or we can just import the specific functions we need. There is no correct method of these two, the circumstance will govern which is a better fit. Here is how you import an entire module:

```python
import random

my_random_number = random.randint(1,100)
```

When you import in this manner you keep a clean `namespace`, but you are required to type the module name every time you want to use one of the module's functions. This is useful is you have functions with similar names, or if you are importing a function that overwrites another function that shares the same name. By always using the module name you avoid conflicts in the namespace.

On the other hand, you can also directly import parts of a module when you are not concerned about name conflicts, or when you don't want to import a large portion of the module. For our purposes today we'll only be using the randint() function, so we'll import it directly like so:

```python
from random import randint

my_random_number = randint(1,100)
```

Both of these blocks of code will result in the variable `my_random_number` having a value between 1, and 100, but behind the scenes they do function slightly differently. As we progress we'll see more examples of both of these methods, for now it's more important that we're aware they exist.

__________
The Task

Using the random module, first generate a random number. Then ask the user for input, and repeat until the guess matches the random number. Once this is achieved, add an additional check to give the user feedback if their guess is higher or lower than the random number.

```python
#! /usr/bin/env python3


from random import randint


def main():
    print("Running Basic")
    basic()
    print("Running Advanced")
    advanced()


def basic():
    # create random number
    # take user's guess
    # compare
    # break if match, else take new guess
    pass


def advanced():
    # create random number
    # take user's guess
    # compare
    # if incorrect, tell user "high/low"
    # break if match, else take new guess
    pass


if __name__ == "__main__":
    main()
```

**Bonus Challenge #1**: Use a try block to verify the user is entering integers

**Bonus Challenge #2**: Look into the absolute value function(abs), if the user's guess is off by more than 50% of the range possible, tell them they are `cold`.
