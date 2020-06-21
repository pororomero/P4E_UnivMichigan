# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:57:27 2020

@author: Harvey
Instruction:
    8.4 Open the file romeo.txt and read it line by line. For each line, split 
    the line into a list of words using the split() method. The program should 
    build a list of words. For each word on each line check to see if the word 
    is already in the list and if not append it to the list. When the program 
    completes, sort and print the resulting words in alphabetical order.
    You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

fhand = open('romeo.txt')
lst_words = []
for line in fhand:
    words = line.split()
    for word in words:
        if not word in lst_words:
            lst_words.append(word)
            
lst_words.sort()
print(lst_words)