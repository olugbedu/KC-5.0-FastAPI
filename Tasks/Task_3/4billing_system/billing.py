import json
import os
import math
from datetime import datetime

BILL_FILE = "bills.json"

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_price(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        try:
            price = float(price)
            quantity = int(quantity)
            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive.\n")
                return
            product = Product(name, price, quantity)
            self.products.append(product)
            print(f"{quantity} x {name} added to cart.\n")
        except ValueError:
            print("Invalid price or quantity.\n")

    def view_cart(self):
        if not self.products:
            print("Cart is empty.\n")
            return
        print("\n--- Cart ---")
        total = 0
        for i, p in enumerate(self.products, 1):
            item_total = p.total_price()
            total += item_total
            print(f"{i}. {p.name} - ₦{p.price} x {p.quantity} = ₦{item_total}")
        total = self.apply_discount(total)
        print(f"Total (after discount if any): ₦{math.ceil(total)}\n")

    def apply_discount(self, total):
        if total > 10000:
            print("Discount applied: 10%")
            return total * 0.9
        return total

    def save_bill(self):
        if not self.products:
            print("Cart is empty. Nothing to save.\n")
            return

        data = load_bills()
        bill = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "items": [
                {
                    "name": p.name,
                    "price": p.price,
                    "quantity": p.quantity,
                    "total": p.total_price()
                }
                for p in self.products
            ],
            "total": math.ceil(self.apply_discount(sum(p.total_price() for p in self.products)))
        }
        data.append(bill)
        with open(BILL_FILE, "w") as f:
            json.dump(data, f, indent=2)
        print("Bill saved successfully.\n")
        self.products = []  # Clear cart after saving

def load_bills():
    if not os.path.exists(BILL_FILE):
        return []
    with open(BILL_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
