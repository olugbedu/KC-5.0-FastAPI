import json
import math
from os.path import exists

def load_products():
    return [
        {"id": 1, "name": "Pen", "price": 150.0},
        {"id": 2, "name": "Notebook", "price": 550.5},
        {"id": 3, "name": "Backpack", "price": 3000.75}
    ]

def load_cart():
    if not exists("cart.json"):
        return []
    with open("cart.json", "r") as f:
        return json.load(f)

def save_cart(cart):
    with open("cart.json", "w") as f:
        json.dump(cart, f, indent=4)

def add_to_cart(cart, products, product_id, qty):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise ValueError("Product not found.")
    cart.append({"product": product, "qty": qty})
    return cart

def checkout(cart):
    total = sum(item["product"]["price"] * item["qty"] for item in cart)
    return {"items": cart, "total": math.ceil(total)}
