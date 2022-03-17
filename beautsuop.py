# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
# import re

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
# tags = soup('span')

# counter=0
# for tag in tags:
#     Look at the parts of a tag
#     print(tag)
#     num=tag.contents[0]
#     counter+=int(num)
# print(counter)

####EXERCISE 2


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
url_list=list()
tags = soup('a')

user_input=int(input('Enter count: '))
position=int(input('Enter position: '))
print('Retrieving:' , url)

counter=0
while counter<user_input:
    for tag in tags:
        url=tag.get('href')
        url_list.append(url)
    url=url_list[(position-1)]
    print('Retrieving:' , url)
    counter+=1
    



