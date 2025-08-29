from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List
from datetime import datetime
from app.db import get_session
from app.models import JobApplication, User
from app.auth import get_current_user

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("/")
def add_application(
    company: str,
    position: str,
    status: str,
    session: Session = Depends(get_session),
    username: str = Depends(get_current_user),
):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    app = JobApplication(
        company=company,
        position=position,
        status=status,
        date_applied=datetime.utcnow(),
        user_id=user.id,
    )
    session.add(app)
    session.commit()
    session.refresh(app)
    return app


@router.get("/", response_model=List[JobApplication])
def list_applications(
    session: Session = Depends(get_session), username: str = Depends(get_current_user)
):
    user = session.exec(select(User).where(User.username == username)).first()
    return session.exec(
        select(JobApplication).where(JobApplication.user_id == user.id)
    ).all()


@router.get("/search")
def search_applications(
    status: str = Query(...),
    session: Session = Depends(get_session),
    username: str = Depends(get_current_user),
):
    user = session.exec(select(User).where(User.username == username)).first()
    apps = session.exec(
        select(JobApplication).where(
            JobApplication.user_id == user.id, JobApplication.status == status
        )
    ).all()
    if not apps:
        raise HTTPException(status_code=404, detail="No applications with that status")
    return apps
