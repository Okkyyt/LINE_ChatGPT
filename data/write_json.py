import json

filename = './data/text.json'

def write_to_json(chat,userId):
    data =[]
    data.append({"userId":userId,"message":chat})
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def read_from_json(userId):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for i in data:
            if i["userId"] == userId :
                loaded_data = i["message"]
                print(loaded_data)
        return loaded_data

def delete_json(userId):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    new_data = [item for item in data if item["userId"] != userId]

    with open(filename, 'w') as json_file:
        json.dump(new_data, json_file)