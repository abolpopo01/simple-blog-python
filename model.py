
import json, os

DBFILE = "DB.json"

def read_db():
    if not os.path.exists(DBFILE):
        return []
    with open(DBFILE, 'r', encoding="utf-8") as f:
        return json.load(f)

def save_to_db(data):
    with open(DBFILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
