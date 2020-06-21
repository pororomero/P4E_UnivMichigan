# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:44:40 2020

@author: Harvey
Instruction: 
    6.5 Write code using find() and string slicing (see section 6.10) to 
    extract the number at the end of the line below. Convert the extracted 
    value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475";
found = text[text.find(':')+1:]
print(float(found.strip()))