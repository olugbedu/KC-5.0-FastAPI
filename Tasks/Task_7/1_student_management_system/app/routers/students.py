from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Student
from app.db import get_session
from app.auth import get_current_user

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=Student)
def create_student(
    student: Student,
    session: Session = Depends(get_session),
    user: str = Depends(get_current_user),
):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@router.get("/", response_model=list[Student])
def read_students(session: Session = Depends(get_session)):
    return session.exec(select(Student)).all()


@router.get("/{student_id}", response_model=Student)
def read_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/{student_id}", response_model=Student)
def update_student(
    student_id: int,
    new_data: Student,
    session: Session = Depends(get_session),
    user: str = Depends(get_current_user),
):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = new_data.name
    student.age = new_data.age
    student.email = new_data.email
    student.grades = new_data.grades
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    session: Session = Depends(get_session),
    user: str = Depends(get_current_user),
):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(student)
    session.commit()
    return {"detail": "Student deleted successfully"}
