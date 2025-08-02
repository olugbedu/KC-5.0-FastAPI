from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel
from file_handler import load_applications, save_applications

app = FastAPI()

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str

@app.post("/applications/")
def add_application(application: JobApplication):
    try:
        applications = load_applications()
        applications.append(application.dict())
        save_applications(applications)
        return {"message": "Application added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/applications/")
def get_applications():
    try:
        return load_applications()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/applications/search")
def search_applications(status: Optional[str] = Query(None)):
    try:
        applications = load_applications()
        if status:
            applications = [app for app in applications if app["status"].lower() == status.lower()]
        return applications
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
