# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:23:41 2020

@author: Harvey
Sample code from ppt
URL: http://www.dr-chuck.com/page1.htm
result: http://www.dr-chuck.com/page2.htm
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
# the next code will handle all of the HTTP requests and stuffs we did before
html = urllib.request.urlopen(url).read() # read will turn it into a long str
soup = BeautifulSoup(html, 'html.parser') # 'html.parser' will fix all the mess

# Retrieve all of the anchor tags
# You can ask soup object, give me the <a - anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))