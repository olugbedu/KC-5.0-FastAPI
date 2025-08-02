import json
from os.path import exists


def load_students():
    if not exists("students.json"):
        return []
    with open("students.json", "r") as file:
        return json.load(file)


def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def calculate_average_and_grade(subject_scores):
    if not subject_scores:
        return 0.0, "F"
    avg = sum(subject_scores.values()) / len(subject_scores)
    if avg >= 70:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"
    return avg, grade
