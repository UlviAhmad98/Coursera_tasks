import urllib.request, urllib.parse, urllib.error
import json

url=input("Enter location: ")
print("Retrieving ", url)

uh=urllib.request.urlopen(url)
js_file=uh.read()
print("Retrieved ", len(js_file), " characters")

js=json.loads(js_file)

counter=0
for item in js['comments']:
    value=item['count']
    counter+=value

print('Count: ', counter)

# sample json: http://py4e-data.dr-chuck.net/comments_42.json