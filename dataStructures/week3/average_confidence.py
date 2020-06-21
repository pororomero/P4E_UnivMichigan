# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:04:12 2020

@author: Harvey
Instruction:
    7.2 Write a program that prompts for a file name, then opens that file and 
    reads through the file, looking for lines of the form:
            X-DSPAM-Confidence:    0.8475
    Count these lines and extract the floating point values from each of the 
    lines and compute the average of those values and produce an output as 
    shown below. Do not use the sum() function or a variable named sum in your 
    solution.
    You can download the sample data at 
    http://www.py4e.com/code3/mbox-short.txt when you are testing below enter 
    mbox-short.txt as the file name.
"""
# Ask for the file 
fname = input('Enter a filename: ')
try:
    fhand = open(fname)
except:
    print("File '" + fname + "' not found.")
    quit()
    
# Check for each line and record line count and sum
line_count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        number = line[line.find(':')+1:].strip()
        line_count += 1
        total += float(number)

# Print resulting average
print('Average spam confidence:', total/line_count)

