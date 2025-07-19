import json
import os

DATA_FILE = "library_data.json"

def save_books(book_list):
    data = []
    for book in book_list:
        data.append({
            "title": book.title,
            "author": book.author,
            "available": book.available
        })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return data
