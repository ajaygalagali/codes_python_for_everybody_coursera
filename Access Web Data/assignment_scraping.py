from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen('http://py4e-data.dr-chuck.net/comments_662705.html')

soup = BeautifulSoup(html,'html.parser')

spans = soup('span')
result =0
for span in spans:

    result+=int(span.text)

print(result)