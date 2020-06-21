# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:45:06 2020

@author: Harvey
Instruction:
    10.2 Write a program to read through the mbox-short.txt and figure out 
    the distribution by hour of the day for each of the messages. You can 
    pull the hour out from the 'From ' line by finding the time and then 
    splitting the string a second time using a colon.
        From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    Once you have accumulated the counts for each hour, print out the counts, 
    sorted by hour as shown below.
"""
file = open('mbox-short.txt')
time_count = {}
for line in file:
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]
        time_count[hour] = time_count.get(hour, 0) + 1

for time in sorted(time_count):
    print(time, time_count[time])
