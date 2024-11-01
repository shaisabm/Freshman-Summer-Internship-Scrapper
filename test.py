import json

data = json.load( open('data.json'))
data['last_visited'] = "title"
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

file.close()