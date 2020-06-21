# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:55:36 2020

@author: Harvey
Instruction: 
    3.1 Write a program to prompt the user for hours and rate per hour using 
    input to compute gross pay. Pay the hourly rate for the hours up to 40 
    and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 
    hours and a rate of 10.50 per hour to test the program (the pay should be 
    498.75). You should use input to read a string and float() to convert the 
    string to a number. Do not worry about error checking the user input - 
    assume the user types numbers properly.
"""
# Computer gross pay
hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# check  which is applicable
if hrs <= 40:
    gross_pay = hrs * rate
else:
    initial_payment = 40 * rate
    gross_pay = initial_payment + (hrs-40) * (1.5 * rate)

# print result
print(gross_pay)