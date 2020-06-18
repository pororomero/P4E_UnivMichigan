# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:13:49 2020

@author: Harvey
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
    Find the link at position 3 (the first name is 1). Follow that link. 
    Repeat this process 4 times. The answer is the last name that you retrieve.
        Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
        Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Tobey.html
    Find the link at position 18 (the first name is 1). Follow that link. 
    Repeat this process 7 times. The answer is the last name that you retrieve.
    Hint: The first character of the name of the last page that you will load is: B
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def retrieve(url, pos):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    print("Retrieving:", url)
    
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    # Look at the parts of a tag
    pos_tag = tags[pos-1]
    url = pos_tag.get('href', None)
    name = pos_tag.contents[0]
    
    return url, name
    
URL = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for _ in range(count):
    URL, name = retrieve(URL, position)

print(name)
    

    





