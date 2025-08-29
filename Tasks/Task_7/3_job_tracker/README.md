# Job Application Tracker API

## Features
- Register & login users with JWT authentication.
- Add and view your job applications.
- Search applications by status.
- Middleware rejects requests without `User-Agent` header.

## Setup
```bash
git clone <your_repo>
cd job_tracker
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

