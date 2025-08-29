from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import init_db
from app.routers import notes
from app.middleware import RequestCounterMiddleware

app = FastAPI(title="Notes Management API")

# Initialize DB
init_db()

# Add CORS
origins = ["http://localhost:3000", "http://127.0.0.1:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Request Counter Middleware
app.add_middleware(RequestCounterMiddleware)

# Routers
app.include_router(notes.router)
