from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from auth_utils import save_students, load_students

app = FastAPI(title="Secure Student Portal API")

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

STUDENTS_FILE = "students.json"


def authenticate(credentials: HTTPBasicCredentials):
    students = load_students(STUDENTS_FILE)
    username = credentials.username
    password = credentials.password

    if username not in students:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    stored_hash = students[username]["password"]
    if not pwd_context.verify(password, stored_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return username


@app.post("/register/")
def register(username: str, password: str):
    try:
        students = load_students(STUDENTS_FILE)
        if username in students:
            raise HTTPException(status_code=400, detail="User already exists")

        hashed_pw = pwd_context.hash(password)
        students[username] = {"password": hashed_pw, "grades": []}

        save_students(STUDENTS_FILE, students)
        return {"message": f"User {username} registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/login/")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    user = authenticate(credentials)
    return {"message": f"Welcome, {user}!"}


@app.post("/grades/")
def add_grade(grade: float, credentials: HTTPBasicCredentials = Depends(security)):
    user = authenticate(credentials)
    students = load_students(STUDENTS_FILE)
    students[user]["grades"].append(grade)
    save_students(STUDENTS_FILE, students)
    return {"message": f"Grade {grade} added for {user}"}


@app.get("/grades/")
def get_grades(credentials: HTTPBasicCredentials = Depends(security)):
    user = authenticate(credentials)
    students = load_students(STUDENTS_FILE)
    return {"username": user, "grades": students[user]["grades"]}
