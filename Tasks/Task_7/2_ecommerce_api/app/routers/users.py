from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from app.db import get_session
from app.models import User
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from datetime import timedelta

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register")
def register(
    username: str,
    password: str,
    is_admin: bool = False,
    session: Session = Depends(get_session),
):
    existing = session.exec(select(User).where(User.username == username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")
    user = User(
        username=username, hashed_password=hash_password(password), is_admin=is_admin
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"msg": "User created", "username": user.username}


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token({"sub": user.username}, access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
