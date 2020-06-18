# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:46:22 2020

@author: Harvey
xml1.py
"""

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data) # transform it into tree like structure, tree information
# within that xml tree data, go find the name and return its text node
print('Name:', tree.find('name').text) 
# within that xml tree data, go find the email and get the hide attribute
print('Attr:', tree.find('email').get('hide'))
