import xml.etree.ElementTree as ET

fhand = open('sampleXML.txt')

data = fhand.read()
trees = ET.fromstring(data)
for i in trees:
    print('Book_ID',i.get('id'))
    print('Author :',i.find('author').text)
    print('Title :',i.find('title').text)
    print()