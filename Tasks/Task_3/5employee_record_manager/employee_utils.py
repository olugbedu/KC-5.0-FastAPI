import json
import os

DATA_FILE = "employees.json"

def save_employees(employee_list):
    data = []
    for emp in employee_list:
        data.append({
            "name": emp.name,
            "id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_employees():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Error loading employee file.")
        return []
