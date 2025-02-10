import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)