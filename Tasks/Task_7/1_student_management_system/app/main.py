from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import init_db
from app.middleware import RequestLoggerMiddleware
from app.routers import students, users

app = FastAPI(title="Student Management System")

# DB setup
init_db()

# Middleware
app.add_middleware(RequestLoggerMiddleware)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(users.router)
app.include_router(students.router)
