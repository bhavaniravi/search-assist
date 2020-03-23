"""

1. How do you open a web browser in python
2. How would do google search

"""

import webbrowser
import sys
from googlesearch import search

def open_browser(urls):
    for url in urls:
        webbrowser.get(using='google-chrome').open(url)

def search_my_term(term, start, count):
    return [url for url in search(term, start=start, stop=count)]

def ignore():
    with open("data/ignore.txt") as f:
        return f.read().splitlines()

def required(urls, ignore_list):
    url_req = []
    for url in urls:
        flag = 0
        for domain in ignore_list:
            if url.find(domain) != -1:
                flag = 1
                break
        if flag == 0:
            url_req.append(url)
    return url_req

term = sys.argv[1]
count = int(sys.argv[2])

print(term, count)

final = []
ignore_list = ignore()


urls = search_my_term(term, 0, count)
url_list = required(urls, ignore_list)
for url in url_list:
    final.append(url)    
while len(final) != count:
    urls = search_my_term(term, len(url_list)+2, count-len(url_list))
    url_list = required(urls, ignore_list)
    for url in url_list:
        final.append(url)
        
open_browser(final)
