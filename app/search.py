"""

1. How do you open a web browser in python
2. How would do google search

"""

import webbrowser
from googlesearch import search
import sys
import os

def open_browser(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

def search_my_term(term,s, count):
    return [url for url in search(term, start=s,stop=count)]

def ignore():
    with open("data/ignore.txt") as f:
        return f.read().splitlines()
    
def required(urls,ignore_list):
    url_req=[]
    for url in urls:
        flag=0
        for domain in ignore_list:
            if(url.find(domain)!=-1):
                flag=1
                break
        if(flag==0):
            url_req.append(url)
    return url_req

term = sys.argv[1]
count = int(sys.argv[2])

print (term, count)

urls=[]
url_list=[]
final=[]
ignore_list=ignore()

urls = search_my_term(term,0,count)
url_list=required(urls,ignore_list)
for url in url_list:
    final.append(url)    
while(len(final)!=count):
    urls = search_my_term(term,len(url_list)+2,count-len(url_list))
    url_list = required(urls,ignore_list)
    for url in url_list:
        final.append(url)
    


open_browser(final)
os.system("google-chrome")
