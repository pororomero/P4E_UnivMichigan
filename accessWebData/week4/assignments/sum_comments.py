# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:51:19 2020

@author: Harvey
sample_data: http://py4e-data.dr-chuck.net/comments_42.html
actual_data: http://py4e-data.dr-chuck.net/comments_657508.html
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
total_sum = 0
tags = soup('span')
for tag in tags:
    # Look at the number 
    number = tag.contents[0] # the number is the content
    total_sum += int(number)
    
print(total_sum)