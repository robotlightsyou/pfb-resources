More on strings

----------
### Control Flow
----------
#### Loops
Loops are one of the most commonly used mechanisms for control flow, that is what order you program will take the steps provided. In python we have while loops and for loops. You can do mostly the same things with each, but they are engineered to work better in different scenarios. Generally speaking, you want to use a while loop when you want to repeat an action until a condition is met, you want to use a for loop when you want to repeat an action a predetermined number of times.

----------
#### while loop
The basic syntax for a while loop is as follows

```
while condition:
    action()
```

What this means is that while the condition stored in the variable 'condition' evaluates to True python will continue executing the function 'action()'. WARNING: it is pretty easy to use a while loop to trigger an infinite loop, freezing your computer from taking new input. If this happens use the keyboard shortcut Control+C to stop the execution. Depending on what your program was doing it may take a moment for you computer to catch up. Let's take a look at some examples

```python
response = ""
while response == '':
    response = input(">")
print("Hello", response)
```

----------
### Booleans
----------

Booleans are a handy data type we'll be touching on as we go through other topics. They are a way to store and either/or value, typically True/False. Note: in python we capitalize True and False, this is something I commonly overlooked in the beginning. Booleans can also be represented as 0 and 1 where 0 is equivalent to False and 1 is equivalent to True. (BONUS TOPIC: Truthy v. Falsey)

If you ever want to trigger an infinite loop(say, if you wanted your program to run continuously), you can start it with "while True." True will always evaluate to True, so your loop will continue until you tell it to stop. To force your program to exit a loop you can insert a break statement. This will cease any repetition and resume the code at the instruction following the while loop

```
while True:
        break
print("I broke out of the loop")
```

There's more to loops, but we're going to take a look at if statements for a moment so we can add some greater complexity to our program.

----------
#### If statements

Along withloops, if/else statements are the bread and butter of control flow. An if statement checks a condition, if true it proceeds to execute its block of code, if false it will skip to the next step. You can also have else statements, or as many elif("else if") statements as you want. The basic structure is

```pyton
if condition_a:
    function_a()
elif condition_b:
    function_b()
else:
    print("Your data did not pass any conditions")
```

Let's take a look at using if statement's to determine a proper greeting

```python
friend = "Yoda"
foe = "Sidd"
# prompt user for their name
while True:
    name = input("What is your name")
    if name != '':
        break
# say hello appropriately
if name == friend:
    print("Hello", friend)
elif name == foe:
    print("I choose treason.")
else:
    print("May the force be with you,", name)
```

A note on if statements - there is a phenomenon known as a "dangling else." This is when you have a really long if statement followed by a short else. Typically it is better style to deal with the shorter branch first. This way you don't get to the end of a code block, see an "else", and have no idea where it came from.

```python
# worse style
if foo == True:
    function_a()
    function_b()
    function_c()
    function_d()
else:
bar()
# better style
if not foo:  # this is an alternative to "if foo == False" we'll discuss later
    bar()
else:
    function_a()
    function_b()
    function_c()
    function_d()
```

----------
#### for loop

For loop are used when you want to repeat an action a predetermined number of times, say for each letter in a string. The basic syntax for a for loop is

```python
for item in iterable_object:
    action()
```

Hold up, more jargon, what is an iterable object? Well, that's any item whose components you can look at individually, like a string, list, or dictionary. Let's look at how we would do that with our earlier example of each letter in a string. To demonstrate, let's print them all individually
```python
my_string = "hello world"
for letter in my_string:
    print(letter)
```

As usual we can add more logic into our program though. Let's print every letter twice on a line.

```pyton
my_string = "hello world"
for letter in my_string:
    print(letter * 2)
```

Or we can modify our iterable object at the beginning. This is how you can use indexing to print every other letter

```python
my_string = "hello world"
# remember the syntax for slicing -> [start : stop : step]
for letter in my_string[::2}: 
    print(letter)
```
----------
#### enumerate

Sometimes you want more than the letter in a word, sometimes you also want to know the index as well. Python has you covered with the built in function enumerate(). Enumerate takes an iterable object and return a list of pairs where the first item in the pair is the index of the item and the second is the item itself. Let's see it in action

```python
my_string = "hello world"
for index, value in enumerate(my_string):
    print(index, value)
```

----------
#### f strings WOOT!

In the bad old days there used to be lots of wonky formatting syntax to insert variables into strings. Thankfully we live after python 3.6, so we to to use f-strings, or format strings. Fstrings are one of my favorite features of python. We talked before about how python is highly abstracted. Fstrings are another tool that get you closer to human language and away from computer syntax.

Unfortunately, Legacy code that runs on pre python 3.6 is pretty common, so let's take a look at some examples of formatting text the old way, and then the awesome way.

```python
name = "Yoda"
age = "900"  # This is still a string, we wouldn't be able to perform math on it
print("%s is %s years old.".format(name, age)
```

That's not too bad, but it's a little clunky, and there's a lot to think about from the editor side of your brain(syntax) instead of running with the creator side of your brain(content). With fstrings you just wrap your variable name in curly braces, much faster to write and 1000% easier to read. Here's our example again

```python
name = "Yoda"
age = "900"  
print("{name} is {age} years old")  
```

Going back to our earlier example of printing each letter in a string and it's index, using fstrings we can format our output to make some neat things without a lot of code.

```python
my_string = "hello world"
for index, value in enumerate(my_string):
    print("{value} is {index} letters from the beginning of this word.)
```





<p>More on strings</p><hr><h3># Control Flow</h3><hr><h4>## Loops</h4><p>Loops are one of the most commonly used mechanisms for control flow, that is what order you program will take the steps provided. In python we have while loops and for loops. You can do mostly the same things with each, but they are engineered to work better in different scenarios. Generally speaking, you want to use a while loop when you want to repeat an action until a condition is met, you want to use a for loop when you want to repeat an action a predetermined number of times.</p><hr><h4>## while loop</h4><p>The basic syntax for a while loop is as follows</p><pre><span style="font-family: &quot;Courier New&quot;;">while condition:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; action()</span></pre><p>What this means is that while the condition stored in the variable 'condition' evaluates to True python will continue executing the function 'action()'. WARNING: it is pretty easy to use a while loop to trigger an infinite loop, freezing your computer from taking new input. If this happens use the keyboard shortcut Control+C to stop the execution. Depending on what your program was doing it may take a moment for you computer to catch up. Let's take a look at some examples</p><pre><span style="font-family: &quot;Courier New&quot;;">response = ""</span><br><span style="font-family: &quot;Courier New&quot;;">while response == '':</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; response = input("&gt;")</span><br><span style="font-family: &quot;Courier New&quot;;">print("Hello", response)</span></pre><hr><h3># Booleans</h3><hr><p>Booleans are a handy data type we'll be touching on as we go through other topics. They are a way to store and either/or value, typically True/False. Note: in python we capitalize True and False, this is something I commonly overlooked in the beginning. Booleans can also be represented as 0 and 1 where 0 is equivalent to False and 1 is equivalent to True. (BONUS TOPIC: Truthy v. Falsey)<br></p><p>If you ever want to trigger an infinite loop(say, if you wanted your program to run continuously), you can start it with "while True." True will always evaluate to True, so your loop will continue until you tell it to stop. To force your program to exit a loop you can insert a break statement. This will cease any repetition and resume the code at the instruction following the while loop</p><pre><span style="font-family: &quot;Courier New&quot;;">while True:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; &nbsp; &nbsp; break</span><br><span style="font-family: &quot;Courier New&quot;;">print("I broke out of the loop")</span></pre><p>There's more to loops, but we're going to take a look at if statements for a moment so we can add some greater complexity to our program.</p><hr><h4>## If statements</h4><p>Along with loops, if/else statements are the bread and butter of control flow. An if statement checks a condition, if true it proceeds to execute its block of code, if false it will skip to the next step. You can also have else statements, or as many elif("else if") statements as you want. The basic structure is</p><pre><span style="font-family: &quot;Courier New&quot;;">if condition_a:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; function_a()</span><br><span style="font-family: &quot;Courier New&quot;;">elif condition_b:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; function_b()</span><br><span style="font-family: &quot;Courier New&quot;;">else:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print("Your data did not pass any conditions")</span></pre><p>Let's take a look at using if statement's to determine a proper greeting</p><pre><span style="font-family: &quot;Courier New&quot;;">friend = "Yoda"</span><br><span style="font-family: &quot;Courier New&quot;;">foe = "Sidd"</span></pre><pre><span style="font-family: &quot;Courier New&quot;;"># prompt user for their name</span><br><span style="font-family: &quot;Courier New&quot;;">while True:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; name = input("What is your name")</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; if name != '':</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; &nbsp; &nbsp; break</span></pre><pre><span style="font-family: &quot;Courier New&quot;;"># say hello appropriately</span><br><span style="font-family: &quot;Courier New&quot;;">if name == friend:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print("Hello", friend)</span><br><span style="font-family: &quot;Courier New&quot;;">elif name == foe:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print("I choose treason.")</span><br><span style="font-family: &quot;Courier New&quot;;">else:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print("May the force be with you,", name)</span></pre><p>A note on if statements - there is a phenomenon known as a "dangling else." This is when you have a really long if statement followed by a short else. Typically it is better style to deal with the shorter branch first. This way you don't get to the end of a code block, see an "else", and have no idea where it came from.</p><pre><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;"># worse style<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">if foo == True:<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">&nbsp; &nbsp; function_a()<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">&nbsp; &nbsp; function_b()<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">&nbsp; &nbsp; function_c()<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">&nbsp; &nbsp; function_d()<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">else:<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">bar()<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;"># better style<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">if not foo:&nbsp; # this is an alternative to "if foo == False" we'll discuss later<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">    bar()<br></span></span><span style="font-family: &quot;Courier New&quot;;"><span style="font-size: 14px;">else:<br></span></span><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; function_a()<br></span><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; function_b()<br></span><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; function_c()<br></span><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; function_d()</span></pre><hr><h4>## for loop</h4><p>For loop are used when you want to repeat an action a predetermined number of times, say for each letter in a string. The basic syntax for a for loop is</p><pre><span style="font-family: &quot;Courier New&quot;;">for item in iterable_object:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; action()</span></pre><p>Hold up, more jargon, what is an iterable object? Well, that's any item whose components you can look at individually, like a string, list, or dictionary. Let's look at how we would do that with our earlier example of each letter in a string. To demonstrate, let's print them all individually</p><pre><span style="font-family: &quot;Courier New&quot;;">my_string = "hello world"</span><br><span style="font-family: &quot;Courier New&quot;;">for letter in my_string:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print(letter)</span></pre><p>As usual we can add more logic into our program though. Let's print every letter twice on a line.</p><pre><span style="font-family: &quot;Courier New&quot;;">my_string = "hello world"</span><br><span style="font-family: &quot;Courier New&quot;;">for letter in my_string:</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print(letter * 2)</span></pre><p>Or we can modify our iterable object at the beginning. This is how you can use indexing to print every other letter</p><pre style="line-height: 1.42857;"><span style="font-family: &quot;Courier New&quot;;">my_string = "hello world"<br></span><span style="font-family: &quot;Courier New&quot;;"># remember the syntax for slicing -&gt; [start : stop : step]<br></span><span style="font-family: &quot;Courier New&quot;;">for letter in my_string[::2}:&nbsp;<br></span><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print(letter)</span></pre><hr><h4>## enumerate</h4><p>Sometimes you want more than the letter in a word, sometimes you also want to know the index as well. Python has you covered with the built in function enumerate(). Enumerate takes an iterable object and return a list of pairs where the first item in the pair is the index of the item and the second is the item itself. Let's see it in action</p><pre><span style="font-family: &quot;Courier New&quot;;">my_string = "hello world"</span><br><span style="font-family: &quot;Courier New&quot;;">for index, value in enumerate(my_string):</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print(index, value)</span></pre><hr><h4>## f strings WOOT!</h4><p>In the bad old days there used to be lots of wonky formatting syntax to insert variables into strings. Thankfully we live after python 3.6, so we to to use f-strings, or format strings. Fstrings are one of my favorite features of python. We talked before about how python is highly abstracted. Fstrings are another tool that get you closer to human language and away from computer syntax.</p><p>Unfortunately, Legacy code that runs on pre python 3.6 is pretty common, so let's take a look at some examples of formatting text the old way, and then the awesome way.</p><pre><span style="font-family: &quot;Courier New&quot;;">name = "Yoda"</span><br><span style="font-family: &quot;Courier New&quot;;">age = "900"&nbsp; # This is still a string, we wouldn't be able to perform math on it</span><br><span style="font-family: &quot;Courier New&quot;;">print("%s is %s years old.".format(name, age)</span></pre><p>That's not too bad, but it's a little clunky, and there's a lot to think about from the editor side of your brain(syntax) instead of running with the creator side of your brain(content). With fstrings you just wrap your variable name in curly braces, much faster to write and 1000% easier to read. Here's our example again</p><pre><span style="font-family: &quot;Courier New&quot;;">name = "Yoda"</span><br><span style="font-family: &quot;Courier New&quot;;">age = "900"&nbsp;&nbsp;</span><br><span style="font-family: &quot;Courier New&quot;;">print("{name} is {age} years old")&nbsp;&nbsp;</span></pre><p>Going back to our earlier example of printing each letter in a string and it's index, using fstrings we can format our output to make some neat things without a lot of code.</p><pre><span style="font-family: &quot;Courier New&quot;;">my_string = "hello world"</span><br><span style="font-family: &quot;Courier New&quot;;">for index, value in enumerate(my_string):</span><br><span style="font-family: &quot;Courier New&quot;;">&nbsp; &nbsp; print("{value} is {index} letters from the beginning of this word.)</span></pre><p><br></p>