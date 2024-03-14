import json

filename = './app/data/text.json'

def write_to_json(chat, userId):
    # ファイルを読み込んでリストに格納
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError:
    # JSONDecodeErrorが発生した場合、空のリストをデフォルト値として使用する
        data = []
    
    # 新しい要素をリストに追加
    data.append({"userId": userId, "message": chat})
    
    # ファイルを書き込みモードで再度開いて、リスト全体をJSON形式で書き込む
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