import json
import os

DATA_FILE = "packages.json"

def save_packages(packages):
    data = []
    for pkg in packages:
        data.append({
            "id": pkg.id,
            "sender": pkg.sender,
            "recipient": pkg.recipient,
            "status": pkg.status
        })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_packages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
