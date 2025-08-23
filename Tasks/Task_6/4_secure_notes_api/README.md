# Notes API with JWT Authentication

## Features
- JWT login authentication
- Add and view personal notes
- Notes stored in `notes.json` per user

## Endpoints
- `POST /login/` → Get JWT token
- `POST /notes/` → Add note (requires token)
- `GET /notes/` → View user’s notes (requires token)

## How to Run
```bash
uvicorn main:app --reload
