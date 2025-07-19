import json
import os
from datetime import datetime

class Transaction:
    def __init__(self, category, amount):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount
        }

def load_transactions(filename="transactions.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_transactions(transactions, filename="transactions.json"):
    with open(filename, "w") as f:
        json.dump(transactions, f, indent=4)

def summarize_by_category(transactions):
    summary = {}
    for txn in transactions:
        category = txn["category"]
        amount = txn["amount"]
        summary[category] = summary.get(category, 0) + amount
    return summary
