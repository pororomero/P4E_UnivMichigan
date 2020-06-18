# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:23:07 2020

@author: Harvey
"""

import xml.etree.ElementTree as ET

an_input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

# stuff is a tree of information that we can use to go through the data
stuff = ET.fromstring(an_input)
# find all the user tag under users
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print(item)
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
