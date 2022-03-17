import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
#parser = ET.XMLParser(encoding="utf-8")



api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=0
counts=0
xyz=0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    #print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    
    xyz=len(data)
    
    #print('Retrieved', xyz, 'characters')
    xyz+=xyz
    #print(data.decode())
    #parser = ET.XMLParser(encoding="utf-8")
    #tree = ET.fromstring((data),parser=parser)
    tree = ET.fromstring(data.encode("utf-8"))
    #print(data.decode())
    counts=tree.find('comment').find('count').text
    counts+=counts
    count+=1
    #print('Count: ',count)
    #print('Sum: ', counts)
print('Retrieving', url)
print('Retrieved', xyz, 'characters')
print('Count: ',count)
print('Sum: ', counts)