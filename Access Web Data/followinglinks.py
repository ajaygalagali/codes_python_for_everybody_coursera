from urllib import request
from bs4 import BeautifulSoup
def parser(url):
    html = request.urlopen(url)

    soup = BeautifulSoup(html,'html.parser')

    links = soup('a')

    url = str(links[17].get('href'))
    print(url)
    return url


inURL = 'http://py4e-data.dr-chuck.net/known_by_Hendri.html'
for i in range(7):
    nURL = str(parser(inURL))
    inURL = nURL