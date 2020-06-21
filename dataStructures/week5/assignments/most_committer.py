# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:10:49 2020

@author: Harvey
Instruction: 
    9.4 Write a program to read through the mbox-short.txt and figure out who 
    has sent the greatest number of mail messages. The program looks for 
    'From ' lines and takes the second word of those lines as the person who 
    sent the mail. The program creates a Python dictionary that maps the 
    sender's mail address to a count of the number of times they appear in 
    the file. After the dictionary is produced, the program reads through the 
    dictionary using a maximum loop to find the most prolific committer.
"""

file = open('mbox-short.txt')
committers = {}
for line in file:
    if line.startswith('From '):
        address = line.split()[1]
        committers[address] = committers.get(address, 0) + 1

most_address = None
most_count = None
for committer in committers:
    if most_address == None or committers[committer] > most_count:
        most_address = committer
        most_count = committers[committer]
        
print(most_address, most_count)