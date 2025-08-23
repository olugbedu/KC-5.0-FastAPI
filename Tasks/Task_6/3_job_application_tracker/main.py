# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import secrets
import json
import os

app = FastAPI(title="Job Application Tracker")

security = HTTPBasic()

USERS_FILE = "users.json"
APPLICATIONS_FILE = "applications.json"


class UserRegister(BaseModel):
    username: str
    password: str


class JobApplication(BaseModel):
    job_title: str
    company: str
    date_applied: str
    status: str


def load_json(filename: str):
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_json(filename: str, data: dict):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    users_db = load_json(USERS_FILE)
    user = users_db.get(credentials.username)

    if not user or not secrets.compare_digest(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post("/register/")
def register(user: UserRegister):
    users_db = load_json(USERS_FILE)
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = {"password": user.password}
    save_json(USERS_FILE, users_db)
    return {"message": f"User {user.username} registered successfully!"}


@app.post("/login/")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    users_db = load_json(USERS_FILE)
    user = users_db.get(credentials.username)

    if not user or not secrets.compare_digest(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": f"Welcome {credentials.username}!"}


@app.post("/applications/")
def add_application(
    app_data: JobApplication, current_user: str = Depends(get_current_user)
):
    apps_db = load_json(APPLICATIONS_FILE)
    if current_user not in apps_db:
        apps_db[current_user] = []
    apps_db[current_user].append(app_data.dict())
    save_json(APPLICATIONS_FILE, apps_db)
    return {"message": "Application added successfully"}


@app.get("/applications/")
def get_applications(current_user: str = Depends(get_current_user)):
    apps_db = load_json(APPLICATIONS_FILE)
    return apps_db.get(current_user, [])
