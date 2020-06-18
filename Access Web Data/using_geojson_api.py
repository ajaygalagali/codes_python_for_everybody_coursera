from urllib import request,parse,error
import json

url = input('Enter URL: ')
address = input('Enter Address: ')
encAddress = parse.urlencode({'address':address})
encKey = parse.urlencode({'key':'42'})
urlHandl = request.urlopen(url+encKey+'&'+encAddress)

data = urlHandl.read().decode()
jData = json.loads(data)
print(jData['results'][0]['place_id'])

