Python comes with a some standard objects.

----------
### Built In Data Types
----------

Some of these tools are the built in data types. The basic of these which we'll be covering you have already seen in the Lessons list, but they are again

* String
* Integer
* Float
* List
* Dictionary
* Classes

Classes strictly speaking aren't built in types, it's a functionality of python. Given the scope of this course it makes the most sense to mention them here. We'll be covering them in the middle, they're either the last beginner item or the first intermediate. Additionally, you may also see references to these data types in your googling - we'll be covering some in the advanced topics lesson, but we won't be getting in depth with all of the following

* Set
* Tuple
* Array

----------
### Strings
----------
Strings are one of the built in datatypes in python(and nearly all programming languages). They represent stored collections of text. That's sounds a little jargon-y, but they're really not too difficult. I just phrased as such to keep you open to the idea that 'text' is not just alphanumeric characters and punctuation, it's any character the computer has a code for(such as emoji or other uncommon symbols).
Strings are signified by quotation marks. In some other languages there is a difference between single quotes and double quotes, but python doesn't care. Python is only interested that they match.

> 'This is a valid string.'
> "This is also a valid string"
> 'This is nor a valid string"

One thing to note, if you ever need to use an apostrophe in your string, pay attention to the quotations used. The easy solution is to always use double quotes around strings with apostrophes. However, you can also use and escape character to prevent the interpreter from treating the apostrophe as the end of the quote. 

> 'You might think this won't cause a problem, but you'd be wrong'
> "This won't cause trouble."
> 'This also won\'t cause trouble, because of the \.

The first string above will error at won't. The interpreter will think the string is "You might think this won" and come back saying 't' is not defined, thinking that 't' is a variable. The second string works fine because there is no conflict in the style of quotes. The last string also works due to the escape character. The escape character will tell the interpreter that the following character should be treated differently. 

----------
### Indexing
__________

Indexing is a wonderful feature of python allowing you to reach into an object and pull out a portion of it's data. String indexing can be used to return a portion of a string. Indexing is written in object[index] format where object represents your variable and index represents where the data you want is. For example, if I wanted to select h from the word hello I would put a 0 in the brackets. That's a little weird right? Python is a 0 indexed language, meaning we start counting at 0 and go to 9 instead of starting at 1 and going to 10.

----------
#### Slicing

Indexing can also be used to return a slice from your object using [x:y] where the first entry is where to start your slice, and the second entry is the first item NOT included. In most cases python is lower-bounds inclusive, but not upper-bounds inclusive. There is an underlying computer science thing that is a little over my head that explains why each language has to pick one of those two options, but that's beyond the scope of this lesson. Take a look at some example of slicing in action:

```python
>>> my_string = "hello world"
>>> my_string[0]
'h'
>>> my_string[8]
'r'
>>> my_string[0:5]    # get a range of indices.
'hello'
>>> my_string[:5]    # if you don't pass a starting index it will start with 0.
'hello'
>>> my_string[6:11]
'world'
>>> my_string[6:]    # if you don't pass an ending index it will default
                        with the last index.
'world'
>>> my_string[:]    # if you omit both indices you will get your whole object.
'hello world'
>>> my_string[-1]    # you can also use negative indexing to start from the
                        end of your object.
'd'
>>> my_string[6:-1]
'worl'
>>> my_string[-5:]    # get the last 5 letters, the same rules apply
                        for leaving out indices.
'world'
>>> my_string[:-4]    # get up to the final x number of letters.
'hello w'
>>> my_string[::2]    # you can add a third argument for step size.
'hlowrd'
>>> my_string[::3]
'hlwl'
>>> my_string[1:8:2]    # take every other character for only a portion of
                            the string.
'el o'
>>> my_string[::-1]    # reverse the string, this is a handy trick.
'dlrow olleh'
```

As you can see, indexing and slicing provide you a lot of options. You might also have noticed that I've been using the word object instead of string, that's because this functionality is not limited to strings, you can use it to return slices of (almost) any ordered data type(such as lists).

----------
### Interpreter
----------
Hey, what's with the ">>>"? That's from the interpreter, a way to directly interact with python instead of writing programs. To start the interpreter, navigate to the command line and type "python3", you should see something similar to the following:

```python
Python 3.9.1 (default, Feb  3 2021, 07:38:02)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Notice it starts with the version of python. I'm using 3.9 but it's okay you are not. However, if you have 3.5 or earlier, we may get to go over how to upgrade python. NOTE: Python2 is different than Python3. If you're interpreter shows version 2.7 or earlier you've entered the wrong command. Exit out and make sure to include the three in python3. There's a lot of resources out there for python2, but it was deprecated recently, so until you have a reason to learn don't bother. 

```python
>>> help("modules")
>>> exit()
>>> quit()
```

Typing help("modules") will get you a list of all the modules(libraries) that are installed. To quit the interpreter you can type quit() or exit(). Notice the parenthesis() after commands in the python interpreter, the parenthesis let python know something is a function to be executed.

Earlier in my examples you saw me use the assignment operator("=") to give the variable my_string different values. Then when I entered the name of my variable into the interpreter it was printed back to me. In order to this this in a program we would need to write a function like print(). Since that one already exists, lets see how you would call it. Type the following into the interpreter:

```>>> my_string = "hello world"```
"=" is called the assignment operator because it is different than the equivalence operator("=="), which is used to test if two objects have the same value. "x = 2" means x gets the value 2, "x ==2" means x already has the value 2.

```python
>>> print(my_string)   
hello world
```

This is a function call, first you type the function name, then in parenthesis any arguments it takes.For print the argument is the object to be printed. You can add complex logic into your arguments, but keep in mind readability is important.

```python
>>> print(my_string[:5] + "computer")    # oops, forgot a space 
hellocomputer
>>> print(my_string[:5] + " computer")
hello computer
```

Spaces are easy to forget, so by default comma separated arguments will be print with a space as below:

```python
>>> a = "hello"
>>> b = "world"
>>> print(a + b)
helloworld
>>> print(a, b)
hello world
```

You can also concatenate string using some of the mathematical operators. Using + will add two strings together(mind the gap). Using the * operator you will get your string repeated x number of times.

```
>>> print((my_string[:5] + " computer") * 5)
hello computerhello computerhello computerhello computerhello computer
>>> print((my_string[:5] + " computer ") * 5)
hello computer hello computer hello computer hello computer hello computer
```

Something to note: while we are printing something different than what is stored in my_string, we are not actually modifying that data. This is something that we will pay attention to next time when we discuss string methods.

```python
>>> print(my_string[:5] + " computer")
hello computer
>>> print(my_string)
hello world
```

The last thing for this section is to write our first function. It's a little cumbersome, but you can type functions directly into the interpreter and then call them back to test. What's nice is they take the same syntax and formatting as if they were in a file, so you can always copy and paste if you need to test a small piece of code. Now we'll write our first hello world, as is tradition. In the interpreter type the following:

```python
>>> def hello_world():
...     print("hello world")
...                          # Notice 2 returns to tell the interpreter
                             # the function is done
>>> hello_world()
hello world
>>> def hello_with_args(amount):
...     print("hello world" * amount)
...
>>> hello_with_args(5)
hello worldhello worldhello worldhello worldhello world
```

To close it off, let's commemorate the milestone by storing our first two functions in a file. Enter the following command in terminal:

```shell
touch hello_world.py
code ./hello_world.py
```

Then in the editor re enter our previous commands:

```python
# first we define the functions using the "def" keyword
# on the first line we type the function name followed by ():
# after the : we start a new indented line to let the interpreter know this code   
# is connected to the previous

def hello_world():
    print("hello world")
def hello_with_args(amount):
    print("hello world" * amount)

# next we have to actually call the functions
hello_world()
hello_world(5)
```

Save this and return to your terminal. You can execute the file with

```shell
$ python3 hello_world.py
hello world
hello worldhello worldhello worldhello worldhello world
```

And that's our first functions and our first file. We'll pick up with some more features of strings next time.