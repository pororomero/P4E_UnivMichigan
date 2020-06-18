# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:07:37 2020

@author: Harvey
Instruction:
    The basic outline of this problem is to read the file, look for integers 
    using the re.findall(), looking for a regular expression of '[0-9]+' and 
    then converting the extracted strings to integers and summing up the 
    integers.
"""
import re

file = open('actual_data.txt')
total_sum = 0
for line in file:
    integers = re.findall('[0-9]+', line)
    if integers:
        total_sum += sum([int(x) for x in integers])
file.close()
print(total_sum)