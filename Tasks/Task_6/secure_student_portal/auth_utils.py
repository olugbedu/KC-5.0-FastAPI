import json
import os


def load_students(file_path: str) -> dict:
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_students(file_path: str, data: dict):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
