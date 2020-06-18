# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:41:25 2020

@author: Harvey
Instruction: Extracting Data from XML
    In this assignment you will write a Python program somewhat similar to 
    http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, 
    read the XML data from that URL using urllib and then parse and extract 
    the comment counts from the XML data, compute the sum of the numbers in 
    the file.
    We provide two files for this assignment. One is a sample file where we 
    give you the sum for your testing and the other is the actual data you 
    need to process for the assignment.

    Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_657510.xml 
                (Sum ends with 70)
    You do not need to save these files to your folder since your program 
    will read the data directly from the URL. Note: Each student will have 
    a distinct data url for the assignment - so only use your own data url 
    for analysis.
"""
# import this to access make an HTTP request and look at page contents
import urllib.request, urllib.parse, urllib.error
# import this to properly work with xml files
import xml.etree.ElementTree as ET

#ask for the xml url
url = input('Enter location: ')
print('Retrieving', url)
# make an xml request to open the xml url the read it as a string file
data = urllib.request.urlopen(url).read()    # this will return a byte
print('Retrieved', len(data), 'characters')
# tree is an organized structure of tree data, easy to work with
tree = ET.fromstring(data)

# this is an  XPath selector string to look through the entire tree of XML for 
# any tag named 'count' 
counts = tree.findall('.//count')
# counts now list of count node with integer in it
print("Count:", len(counts))
# find the sum of count for every count.text
total = sum([int(count.text) for count in counts])

print(total)
    