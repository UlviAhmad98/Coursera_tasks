import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counter=0
count=0
lst=tree.findall('comments/comment')
for item in lst:
    count_n=int(item.find('count').text)

    counter+= 1
    count+= count_n
    
print('Count: ', counter)
print('Sum: ', count)

# #sample URL: http://py4e-data.dr-chuck.net/comments_42.xml