from fastapi import FastAPI
from app.db import init_db
from app.routers import users, applications
from app.middleware import check_user_agent

app = FastAPI(title="Job Application Tracker")

# Middleware
app.middleware("http")(check_user_agent)

# Initialize DB
init_db()

# Routers
app.include_router(users.router)
app.include_router(applications.router)
