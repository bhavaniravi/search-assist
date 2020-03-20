"""

1. How do you open a web browser in python
2. How would do google search

"""

import webbrowser
from googlesearch import search
import sys
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
chrome_path_NW = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --new-window"
controller = webbrowser.get(chrome_path)
controllerNW = webbrowser.get(chrome_path_NW)
def open_browser(urls):
    for url in urls:
        controller.open(url, new=1)

def search_my_term(term, count):
    return [url for url in search(term, stop=count)]


term = sys.argv[1]
count = int(sys.argv[2])

print (term, count)

urls = search_my_term(term, count)
controllerNW.open(urls[0],new=0)
open_browser(urls[1:])
