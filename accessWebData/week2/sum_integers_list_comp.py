# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:39:16 2020

@author: Harvey
This is same as sum_integers but it's by using list comprehensions.
"""


import re
print(sum([int(x) for x in re.findall('[0-9]+', open('actual_data.txt').read())]))


