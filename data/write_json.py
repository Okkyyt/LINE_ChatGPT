import json

filename = './data/text.json'

def write_to_json(data):
    with open(filename, 'w') as json_file:
        print(data)
        json.dump(data, json_file)

def read_from_json():
    with open(filename, 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data

def delete_json():
    with open(filename, 'w') as f:
        f.write('')