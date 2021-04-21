__________
### Search Tool
__________

In this tutorial we will be building a search tool that will help you make better targeted searches to known resources. We'll look at taking in command line arguments, lists, and control flow using for loops. Let's jump in to the code.

__________
#### The Code

We start as usual with a shebang to let your computer what python to use. This is the standard shebang for macs:

```python
#! /usr/bin/env python3
```

Next we'll need to import some things. We're only bringing in one function from each of the modules we're using, so we'll import those directly instead of the entire module.

```python
from sys import argv
from webbrowser import open_new_tab
```

The first thing we are importing is `argv` from the `sys` module. This will allow us access to whatever the user enters as a command line argument, which we'll use to get their search query. `argv` is a concept you'll see across many programming languages. Commonly, and in python, the first item(`argv[0]`) is the name of the program being run. In my case that means `argv[0] == "searchdemo.py"`. The rest of `argv` are what's called "command line arguments", and they offer us a chance to take input from the user without having to call input() directly or creating an interface for the user. 

After that we are importing `open_new_tab` from the `webbrowser` module. This is a simple function that has some nice features. If you currently have your browser open, it will add a new tab to the window in your active monitor directed to the specified url(we'll cover this more later in the implentation). If you do not currently have your browser open, it will open a new window.

__________
#### Lists - Where to Search

Now we are going to meet one of the more robust features of python - lists. Lists are just what they sound like - an ordered collection of objects. We use `[]` to denote lists in python, though you can also make one using the list() function. We'll be covering lists in much greater detail in a later lesson, here we will be using them to store the addresses of our websites as strings.

```python
percent_list = ["https://www.google.com/search?hl=en&q=",
                "https://groups.google.com/search?q="]
```

We can see the name of our list is percent_list, I'll explain that further below. Next we see bracket followed by a comma separated list of strings, and a closing bracket to end the list. We've included the full "https" business to ensure the webbrowser module is directed to the correct url. We've also added some business after the ".com", this is the google syntax for search queries. If you open google.com and run a search, you can check the address of the results and see it will begin similarly. There may be a little more there before the "q=", but what we have here is sufficient to perform a search in english. 

You can also see in the address of your results that after the "q=" it starts listing the terms you are searching for. If your search query was more than one word, you will also see that rather than using spaces, google has filled the gaps with "%20". This is google's method for negotiating space characters since they aren't allowed in website addresses. Another common method is to replace spaces with a "+", as the following sites do:

```python
plusList = ["https://losangeles.craigslist.org/search/sss?query=",
            "https://www.amazon.com/s?k="]
```

Again we see there is additional business after the ".com", but anything we append to this url will return a search for that topic from these sites. A bonus challenge when we are done is to go out to other resources, see how they deal with space characters in search queries, then add them here.

__________
#### Open Multiple Searches at Once

Now we are taking input from the user via the command line at runtime, and we have sites to search that input on, let's look at how we can actually open these new tabs. Since we are going to be doing a repeated action a known amount of times(the length of our lists), we can use a for loop. Actually, we'll use a separate for loop for each of our lists. In our loop we'll need to take our list of strings and turn it into one search query. Fortunately python offers us the `join` method for just such a case. You use the join method by putting the text you want to insert into your list in quotations, then calling the `join` method on that text, using your list as the argument. That sounds a little weird written out, let's look at it in code:

```python
for url in percentList:
    url = url + "%20".join(argv[1:])
    open_new_tab(url)
```

Here we have `"%20"` in quotes because that is what we are inserting between each item in our list of command line arguments passed by the user. That list starts at index 1, because recall that `argv[0]` is just the name of the program, and not something we need to include in our search. We do not have an ending index listed because we want to include all tha the user input. Once we have the list joined as a single string we can concatenate it to the base search url from our list(sorry, I explained the middle line of code backwards from how it's written, but that is how the order of operations will be executed).

```python
for url in plusList:
    url = url + "+".join(argv[1:])
    open_new_tab(url)
```

Now that we have all of our pieces, we can stich it together with a main() and try it from the command line. Navigate to the directory where you have saved the file, then call itwith python3 and the file name like this `python3 searchdemo.py python for loops` and you should get new tabs correctly searching for loops from each of the listed sites. Once that is working, go back and replace the shopping sites with coding sites, and the tool will be complete.

```python
#! /usr/bin/env python3

# take in command line query 
from sys import argv
from webbrowser import open_new_tab

def main():
    # list of websites
    # split sites based on space 
    percentList = ["https://www.google.com/search?hl=en&q=",
                    "https://groups.google.com/search?q="]
    plusList = ["https://losangeles.craigslist.org/search/sss?query=",
                "https://www.amazon.com/s?k="]

    # for loop over lists
    # open each site
    for url in percentList:
        url = url + "%20".join(argv[1:])
        open_new_tab(url)

    for url in plusList:
        url = url + "+".join(argv[1:])
        open_new_tab(url)


if __name__ == "__main__":
    main()
    
```