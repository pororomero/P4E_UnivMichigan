# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:43:13 2020

@author: Harvey
Instruction: 
    4.6 Write a program to prompt the user for hours and rate per hour using 
    input to compute gross pay. Pay should be the normal rate for hours up to 
    40 and time-and-a-half for the hourly rate for all hours worked above 40 
    hours. Put the logic to do the computation of pay in a function called 
    computepay() and use the function to do the computation. The function 
    should return a value. Use 45 hours and a rate of 10.50 per hour to test
    the program (the pay should be 498.75). You should use input to read a 
    string and float() to convert the string to a number. Do not worry about 
    error checking the user input unless you want to - you can assume the user 
    types numbers properly. Do not name your variable sum or use the 
    sum() function
"""
def computepay(hrs, rate):
    """ Returns the gross pay."""
    if hrs <= 40:
        gross_pay = hrs * rate
    else:
        initial_payment = 40 * rate
        gross_pay = initial_payment + (hrs-40) * (1.5 * rate)
        
    return gross_pay

# Ask for hours and rate per hour input
hours = float(input("Enter Hours: "))
rate_hour = float(input("Enter Rate: "))

# print result
print("Pay", computepay(hours, rate_hour))