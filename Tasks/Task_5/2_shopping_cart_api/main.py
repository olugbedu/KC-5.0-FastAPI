from fastapi import FastAPI, HTTPException
from cart import load_products, load_cart, save_cart, add_to_cart, checkout

app = FastAPI()

@app.get("/products/")
def get_products():
    return load_products()

@app.post("/cart/add")
def add_item(product_id: int, qty: int):
    try:
        cart = load_cart()
        products = load_products()
        updated_cart = add_to_cart(cart, products, product_id, qty)
        save_cart(updated_cart)
        return updated_cart
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/cart/checkout")
def perform_checkout():
    cart = load_cart()
    return checkout(cart)
