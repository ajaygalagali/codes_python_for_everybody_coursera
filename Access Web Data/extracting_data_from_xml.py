from urllib import request
import xml.etree.ElementTree as et


url = input('Enter URL :')

xml = request.urlopen(url)
data = xml.read()

content = data.decode()

tree = et.fromstring(content)
counts = tree.findall('.//count')
result = 0
for count in counts:
    result+=int(count.text)

print(result)
