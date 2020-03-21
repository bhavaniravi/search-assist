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
def search_rem(term,s,count):
    return [url for url in search(term,start=s,stop=count)]

def ignore():
    with open("/home/olagammal/Desktop/search-assist-master/ignore.txt") as f:
        return f.read().splitlines()

url_list=[]
term = sys.argv[1]
count = int(sys.argv[2])

print (term, count)

ignore_list=ignore()
final=0
urls = search_my_term(term, count)
for url in urls:
    if url not in ignore_list:
        url_list.append(url)
        final+=1
        
        
open_browser(url_list)


urls=[]
if(final!=count):
    urls = search_rem(term,final+2,count-final)
open_browser(urls)
