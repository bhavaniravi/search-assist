"""

1. How do you open a web browser in python
2. How would do google search

"""

import webbrowser
from googlesearch import search
import sys

def open_browser(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

def search_my_term(term, count):
    return [url for url in search(term, stop=count)]


term = sys.argv[1]
count = sys.argv[2]
count=int(count)

print (term, count)

urls = search_my_term(term)
open_browser(urls)
