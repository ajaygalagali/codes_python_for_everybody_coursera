import urllib.parse,urllib.request,urllib.error
import json

url = input('Enter URL: ')

urlHandl = urllib.request.urlopen(url)

data = urlHandl.read().decode()

jContent = json.loads(data)
result = 0
for i in jContent['comments']:
    result+=int(i['count'])
print(result)