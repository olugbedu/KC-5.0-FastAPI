# E-Commerce API (FastAPI)

## Features
- User registration & JWT login
- Admin-only product creation
- Public product listing
- Cart add & checkout
- Orders saved to `orders.json`
- Response time middleware

## Setup
```bash
git clone <your-repo-url>
cd ecommerce_api
pip install -r requirements.txt
```
## Run
```bash
uvicorn app.main:app --reload
```
## Usage

- Register /users/register

- Login /users/login

- Add product /products/admin/ (admin only)

- View products /products/

- Add to cart /cart/add/

- Checkout /cart/checkout/