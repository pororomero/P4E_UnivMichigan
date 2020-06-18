# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:28:31 2020

@author: Harvey
Instruction: 
    Calling a JSON API
        In this assignment you will write a Python program somewhat similar to 
    http://www.py4e.com/code3/geojson.py. The program will prompt for a 
    location, contact a web service and retrieve JSON for the web service and 
    parse that data, and retrieve the first place_id from the JSON. A place ID 
    is a textual identifier that uniquely identifies a place as within Google Maps.
    API End Points
        To complete this assignment, you should use this API endpoint that has 
    a static subset of the Google Data:
            http://py4e-data.dr-chuck.net/json?
    This API uses the same parameter (address) as the Google API. This API 
    also has no rate limit so you can test as often as you like. If you visit 
    the URL with no parameters, you get "No address..." response.
    To call the API, you need to include a key= parameter and provide the 
    address that you are requesting as the address= parameter that is properly 
    URL encoded using the urllib.parse.urlencode() function as shown in 
    http://www.py4e.com/code3/geojson.py
        Make sure to check that your code is using the API endpoint is as 
    shown above. You will get different results from the geojson and json 
    endpoints so make sure you are using the same end point as this 
    autograder is using.
"""

import urllib.parse, urllib.error, urllib.request
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address, 'key': api_key})
json_handle = urllib.request.urlopen(url)
print('Retrieving', url)
content = json_handle.read().decode()
print('Retrieved', len(content), 'characters')
json_dict = json.loads(content)

try:
    print('place_id:', json_dict['results'][0]['place_id'])
except Exception:
    print('No place_id found')
