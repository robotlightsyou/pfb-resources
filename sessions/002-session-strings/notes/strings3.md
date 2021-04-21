More on strings


----------


#### String Methods



Methods are functions that are built into an object.

----------

#### Immutability


Many data types in python can be modified, but strings can't, and are know as 'immutable' because of this. This is a little tricky though, because while you can't reassign values within a string, you can reassign your vaiable to a new string created by modifying your original string.

```python
>>> my_string = "hello world"
>>> my_string = my_string[:5] + "Z" + my_string[6:]
>>> my_string
'helloZworld'
```

----------
#### Strings

anything in quotes
single or double quotes work
recommend always using double quotes

immutable
string indexing
string concatenation
string methods
isupper, upper, islower, lower, startswith, endswith

----------
##### Exercises

1. **swap case** - write a script that accepts flags for options, and returns a string with the text modified based on the options specified by the user.
2. **website multi search** - using the webbrowser module, write a script that will take input from the user<br>and then open pages in the default browser searching for that input among predetermined sites. Recommended to engineer this tool towards searching for programming concepts, and continuing to refine it throughout your study.
3. **basic "diary"** - storing data in a variable is probably the simplest method of data retrieval available to python. Write a script that will prompt the user to input a variable and a value, then save those in proper python format to a file. Bonus challenge - repeat with shell scripting.