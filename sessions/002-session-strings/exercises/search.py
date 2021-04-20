#! /usr/bin/env python3

import webbrowser
from sys import argv


percentList = ["https://www.google.com/search?hl=en&q=",
                "https://groups.google.com/search?q="]
plusList = ["https://losangeles.craigslist.org/search/sss?query=",
            "https://www.amazon.com/s?k="]


def main():
    query = input(">")
    # for url in percentList:
    #     url = url + "%20".join(list(query))
    #     url = url + "%20".join(argv[1:])
    #     webbrowser.open_new_tab(url)
    for url in plusList:
        # url = url + "+".join(argv[1:])
        url = url + "+".join(query.split())
        webbrowser.open_new_tab(url)


if __name__ == '__main__':
    exit(main())


# https://stackoverflow.com/questions/61458373/how-do-i-run-a-python-script-from-macs-spotlight-instead-of-having-to-open-ter
