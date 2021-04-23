import json 

def get_user_list_values(user_id: str, list_name: str) -> list:
    db = r'C:\Users\ilyah\Все_основное\it\Python\Projects\VSL_Bot-1\vslbot\data\db.json'
    with open(db) as db:
        data = json.load(db)
    return data['users'][user_id]['lists'][list_name]

def get_lists_names(user_id: str):
    db = r'C:\Users\ilyah\Все_основное\it\Python\Projects\VSL_Bot-1\vslbot\data\db.json'
    with open(db) as f:
        data = json.load(f)
    try:
        return data['users'][user_id]['lists'].keys()
    except Exception as e:
        return "У тебя еще нет списков"

def new_list(user_id, list_name: str, values: list) -> None:
    db = r'C:\Users\ilyah\Все_основное\it\Python\Projects\VSL_Bot-1\vslbot\data\db.json'
    with open(db, "r") as read_file:
        data = json.load(read_file)
    try:
        data['users'][user_id]['lists'][list_name] = values
    except KeyError:
        data['users'][user_id] = {"lists":{list_name:values}}
    with open(db, "w", encoding='utf-8') as write_file:
        json.dump(data, write_file)