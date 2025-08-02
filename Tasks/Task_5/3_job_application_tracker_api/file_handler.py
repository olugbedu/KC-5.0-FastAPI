import json
import os

FILE_PATH = "applications.json"

def load_applications():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_applications(applications):
    with open(FILE_PATH, "w") as file:
        json.dump(applications, file, indent=4)
