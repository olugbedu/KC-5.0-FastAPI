from fastapi import FastAPI, HTTPException
from models import Student
from utils import load_students, save_students, calculate_average_and_grade

app = FastAPI()


@app.post("/students/")
def add_student(student: Student):
    students = load_students()
    for existing in students:
        if existing["name"].lower() == student.name.lower():
            raise HTTPException(status_code=400, detail="Student already exists.")

    avg, grade = calculate_average_and_grade(student.subject_scores)
    new_student = {
        "name": student.name,
        "subject_scores": student.subject_scores,
        "average": avg,
        "grade": grade,
    }
    students.append(new_student)
    save_students(students)
    return new_student


@app.get("/students/")
def get_all_students():
    return load_students()


@app.get("/students/{name}")
def get_student_by_name(name: str):
    students = load_students()
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    raise HTTPException(status_code=404, detail="Student not found.")
