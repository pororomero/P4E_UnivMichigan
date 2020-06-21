# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:48:25 2020

@author: Harvey
Instruction:
    5.2 Write a program that repeatedly prompts a user for integer numbers 
    until the user enters 'done'. Once 'done' is entered, print out the 
    largest and smallest of the numbers. If the user enters anything other 
    than a valid number catch it with a try/except and put out an appropriate 
    message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the 
    output below.
"""

largest = None
smallest = None
while True:
    # Get a value from the user
    num = input("Enter a number: ")
    if num == 'done':
            break
    try:
        num = int(num)
        # Initially set the trigger for the first
        if largest == None:
            largest = num
        if smallest == None:
            smallest = num
            continue # initially set the first value as smallest and largest
        
        # Check if the current num is largest or smallest with respect to the
        # recent value of largest and smallest
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)