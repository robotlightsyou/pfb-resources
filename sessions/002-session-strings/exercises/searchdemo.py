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
    for url in percentList:
        url = url + "%20".join(argv[1:])
        open_new_tab(url)

    for url in plusList:
        url = url + "+".join(argv[1:])
        open_new_tab(url)

# open each site

if __name__ == "__main__":
    main()
    