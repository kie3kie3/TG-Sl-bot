import json


def get_info():
    with open('db.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def update(data):
    with open('db.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_token():
    with open('/home/kie3/token.json', 'r', encoding='utf-8') as file:
        return json.load(file)
