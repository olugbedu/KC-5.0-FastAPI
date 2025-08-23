from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List
import auth
import notes_handler

app = FastAPI(title="Secure Notes API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class Note(BaseModel):
    title: str
    content: str
    date: str


@app.post("/register/")
def register(username: str, password: str):
    users = auth.load_users()
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[username] = {"password": auth.get_password_hash(password)}
    auth.save_users(users)
    return {"message": "User registered successfully"}


@app.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = auth.create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/notes/")
def add_note(note: Note, token: str = Depends(oauth2_scheme)):
    username = auth.verify_token(token)
    notes_handler.add_note(username, note.dict())
    return {"message": "Note added successfully"}


@app.get("/notes/", response_model=List[Note])
def get_notes(token: str = Depends(oauth2_scheme)):
    username = auth.verify_token(token)
    return notes_handler.get_notes(username)
