from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Product
from app.db import get_session
from app.auth import get_current_admin

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/admin/", response_model=Product)
def create_product(
    product: Product,
    session: Session = Depends(get_session),
    admin: str = Depends(get_current_admin),
):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@router.get("/", response_model=list[Product])
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()
