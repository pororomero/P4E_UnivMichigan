import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    # turns this into - http://py4e-data.dr-chuck.net/json?address=ann+Arobr%2C+Mi&key=42
    # this will handle the working url transformation by passing dictionary
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    # a file handle to that url
    uh = urllib.request.urlopen(url, context=ctx)
    # read to turn it into a big chunk of byte string - then convert it to python string
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # check if it is possible to turn json format into python dictionary
    try:
        js = json.loads(data)
    except:
        js = None

    # check the status if the content is there, there is a good ouput
    # if js is None, no status in js or if json's status is not OK
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    # opposite of json.loads - turns it into json form and print it with indentation = 4
    print(json.dumps(js, indent=4))

    # dig into the new python dictionary which one you're looking for
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
