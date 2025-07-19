import json
import os

class Student:
    def __init__(self, name, subjects_scores):
        self.name = name
        self.subjects = subjects_scores  # dict like {"Math": 80, "English": 75}
        self.average = self.calculate_average()
        self.grade = self.assign_grade()

    def calculate_average(self):
        total = sum(self.subjects.values())
        return total / len(self.subjects)

    def assign_grade(self):
        avg = self.average
        if avg >= 70:
            return 'A'
        elif avg >= 60:
            return 'B'
        elif avg >= 50:
            return 'C'
        elif avg >= 40:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": self.subjects,
            "average": self.average,
            "grade": self.grade
        }

def load_students(filename="student.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_students(data, filename="student.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    name = input("Enter student name: ")
    subjects = {}
    while True:
        subject = input("Enter subject (or type 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            subjects[subject] = score
        except ValueError:
            print("Invalid score. Try again.")
    student = Student(name, subjects)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)
    print(f"Student {name} added successfully!")

def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"\nName: {student['name']}")
        print(f"Subjects & Scores: {student['subjects']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")

def update_student():
    students = load_students()
    name = input("Enter the name of the student to update: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            found = True
            print("Current subjects:", student["subjects"])
            subject = input("Enter the subject to update/add: ")
            try:
                score = float(input("Enter new score: "))
                student["subjects"][subject] = score
                temp_student = Student(student["name"], student["subjects"])
                student["average"] = temp_student.average
                student["grade"] = temp_student.grade
                save_students(students)
                print("Student record updated.")
            except ValueError:
                print("Invalid score.")
            break
    if not found:
        print("Student not found.")

def main():
    while True:
        print("\n=== Student Report Card App ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
