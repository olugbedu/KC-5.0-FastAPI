from employee_utils import save_employees, load_employees

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        name = input("Enter name: ")
        emp_id = input("Enter ID: ")
        department = input("Enter department: ")
        try:
            salary = float(input("Enter salary: "))
            if salary <= 0:
                print("Salary must be positive.\n")
                return
        except ValueError:
            print("Invalid salary input.\n")
            return
        emp = Employee(name, emp_id, department, salary)
        self.employees.append(emp)
        print("Employee added.\n")

    def view_employees(self):
        if not self.employees:
            print("No employee records found.\n")
            return
        print("\n--- Employee Records ---")
        for i, emp in enumerate(self.employees, 1):
            print(f"{i}. {emp.name} | ID: {emp.emp_id} | Dept: {emp.department} | Salary: ₦{emp.salary}")
        print()

    def search_by_id(self):
        search_id = input("Enter employee ID to search: ")
        found = False
        for emp in self.employees:
            if emp.emp_id == search_id:
                print(f"\nFound: {emp.name} | Dept: {emp.department} | Salary: ₦{emp.salary}\n")
                found = True
                break
        if not found:
            print("Employee not found.\n")

    def save_to_file(self):
        save_employees(self.employees)
        print("Employees saved to file.\n")

    def load_from_file(self):
        data = load_employees()
        self.employees = []
        for item in data:
            emp = Employee(item["name"], item["id"], item["department"], item["salary"])
            self.employees.append(emp)
        print("Employees loaded from file.\n")

def main():
    manager = EmployeeManager()

    while True:
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search by ID")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")

        choice = input("Choose an option (1–6): ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_employees()
        elif choice == "3":
            manager.search_by_id()
        elif choice == "4":
            manager.save_to_file()
        elif choice == "5":
            manager.load_from_file()
        elif choice == "6":
            print("Exiting Employee Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
