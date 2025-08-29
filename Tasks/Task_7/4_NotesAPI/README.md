# Notes API (Task 4)

A FastAPI-based Notes Management API with database + JSON file backup + middleware logging.

## Features
- Create, list, get, delete notes
- SQLModel (SQLite) database
- Auto backup to `notes.json`
- Middleware that counts & logs requests
- CORS enabled (`http://localhost:3000`, `http://127.0.0.1:5500`)

## Installation
```bash
git clone <repo_url>
cd Task4-NotesAPI
pip install -r requirements.txt
```
## Run
```bash
uvicorn app.main:app --reload
```