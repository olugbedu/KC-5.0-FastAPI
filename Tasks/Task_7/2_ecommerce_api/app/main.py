from fastapi import FastAPI
from app.db import init_db
from app.middleware import ResponseTimeMiddleware
from app.routers import users, products, cart

app = FastAPI(title="E-Commerce API")

# Init DB
init_db()

# Middleware
app.add_middleware(ResponseTimeMiddleware)

# Routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
