# main.py
from fastapi import FastAPI, Depends, HTTPException
import json
import os
from auth import authenticate, admin_required, save_users, load_users, hash_password

app = FastAPI()

PRODUCTS_FILE = "products.json"
CART_FILE = "cart.json"


# ---------- Utilities ----------
def load_json(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)


def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ---------- User Management ----------
@app.post("/register/")
def register(username: str, password: str, role: str = "customer"):
    users = load_users()
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    if role not in ["admin", "customer"]:
        raise HTTPException(status_code=400, detail="Invalid role")
    users[username] = {"password": hash_password(password), "role": role}
    save_users(users)
    return {"message": f"User {username} registered as {role}"}


# ---------- Admin Endpoints ----------
@app.post("/admin/add_product/")
def add_product(product_id: str, name: str, price: float, user=Depends(admin_required)):
    products = load_json(PRODUCTS_FILE)
    if product_id in products:
        raise HTTPException(status_code=400, detail="Product already exists")
    products[product_id] = {"name": name, "price": price}
    save_json(PRODUCTS_FILE, products)
    return {"message": f"Product {name} added successfully"}


# ---------- Public Endpoints ----------
@app.get("/products/")
def list_products():
    products = load_json(PRODUCTS_FILE)
    return products


# ---------- Customer Endpoints ----------
@app.post("/cart/add/")
def add_to_cart(product_id: str, quantity: int, user=Depends(authenticate)):
    products = load_json(PRODUCTS_FILE)
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    cart = load_json(CART_FILE)
    username = user["username"]

    if username not in cart:
        cart[username] = []

    cart[username].append({"product_id": product_id, "quantity": quantity})
    save_json(CART_FILE, cart)
    return {
        "message": f"Added {quantity} of {products[product_id]['name']} to {username}'s cart"
    }


@app.get("/cart/")
def view_cart(user=Depends(authenticate)):
    cart = load_json(CART_FILE)
    return {user["username"]: cart.get(user["username"], [])}
