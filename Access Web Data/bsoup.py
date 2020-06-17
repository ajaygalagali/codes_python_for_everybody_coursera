from urllib import request
from bs4 import BeautifulSoup

fhand = request.urlopen("https://www.dr-chuck.com")

soup = BeautifulSoup(fhand,'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))