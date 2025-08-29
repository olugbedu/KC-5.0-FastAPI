from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Product, User
from app.db import get_session
from app.auth import get_current_user
import json, os

router = APIRouter(prefix="/cart", tags=["cart"])

ORDERS_FILE = "orders.json"


@router.post("/add/")
def add_to_cart(
    product_id: int,
    quantity: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")

    return {"msg": f"{quantity} x {product.name} added to cart (not persisted)"}


@router.post("/checkout/")
def checkout(
    product_id: int,
    quantity: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")

    product.stock -= quantity
    session.add(product)
    session.commit()

    order = {
        "user": user.username,
        "product": product.name,
        "quantity": quantity,
        "total": product.price * quantity,
    }

    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w") as f:
            json.dump([], f)

    with open(ORDERS_FILE, "r+") as f:
        data = json.load(f)
        data.append(order)
        f.seek(0)
        json.dump(data, f, indent=2)

    return {"msg": "Checkout successful", "order": order}
