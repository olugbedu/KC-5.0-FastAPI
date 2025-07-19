import json
import os
import math

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = math.ceil(price)  # Round up to nearest whole number
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

def load_books(filename="books.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_books(books, filename="books.json"):
    with open(filename, "w") as f:
        json.dump(books, f, indent=4)

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        book = Book(title, author, price, stock)
        books = load_books()
        books.append(book.to_dict())
        save_books(books)
        print(f"Book '{title}' added successfully.")
    except ValueError:
        print("Invalid price or stock input.")
