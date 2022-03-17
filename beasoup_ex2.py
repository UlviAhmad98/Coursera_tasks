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
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    url_list=list()
    tags = soup('a')
    counter+=1
### example url: http://py4e-data.dr-chuck.net/known_by_Fikret.html

