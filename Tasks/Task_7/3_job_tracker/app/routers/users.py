from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import User
from app.auth import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
def register(username: str, password: str, session: Session = Depends(get_session)):
    existing_user = session.exec(select(User).where(User.username == username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": "User registered successfully"}


@router.post("/login")
def login(username: str, password: str, session: Session = Depends(get_session)):
    user = session.exec(
        select(User).where(User.username == username, User.password == password)
    ).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
