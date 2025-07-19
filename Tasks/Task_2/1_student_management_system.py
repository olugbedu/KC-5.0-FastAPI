students = []

def add_student():
    try:
        name = input("Enter student name: ")
        scores = []
        for _ in range(1, 4):
            score = float(input(f"Enter score {_}: "))
            scores.append(score)

        student = {"name": name, "scores": scores}
        students.append(student)
        print(f"{name} added successfully!\n")
    except ValueError:
        print("Invalid input! Scores must be numbers.\n")

def get_performance(avg):
    if avg < 50:
        return "Fail"
    elif avg < 80:
        return "Pass"
    else:
        return "Excellent"

def show_all_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n All Students ")
    for student in students:
        avg = sum(student["scores"]) / 3
        status = get_performance(avg)
        print(f"{student['name']} - Avg: {avg:.2f}, Status: {status}")
    print()

def search_student():
    name = input("Enter name to search: ").lower()
    found = False
    for student in students:
        if student["name"].lower() == name:
            avg = sum(student["scores"]) / 3
            status = get_performance(avg)
            print(f"\n{student['name']} - Scores: {student['scores']}, Avg: {avg:.2f}, Status: {status}\n")
            found = True
            break
    if not found:
        print("Student not found.\n")

def main():
    while True:
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.\n")

main()
