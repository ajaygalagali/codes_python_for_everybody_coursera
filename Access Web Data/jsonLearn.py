import json

fhand = open('sampleJSOn.txt')

data = fhand.read()

content = json.loads(data)
print(type(content))
print('Count',len(content))

for i in content:
    print(type(i))
    for q in i['friends']:
        print(type(i))
        print(q['name'])
        print()
