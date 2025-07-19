import json
import os

DATA_FILE = "diary.json"

def save_entries(entries):
    data = []
    for entry in entries:
        data.append({
            "date": entry.date,
            "title": entry.title,
            "content": entry.content
        })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_entries():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Error loading diary file. Starting with empty diary.")
        return []
