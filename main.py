from db import create_employee_table, add_employee, get_employees

if __name__ == "__main__":
    create_employee_table()
    add_employee("John Doe", "Software Engineer", "Engineering")
    add_employee("Jane Smith", "HR Manager", "Human Resources")

    employees = get_employees()
    print("Employees added successfully.")
    print("List of employees:")
    for employee in employees:
        print(employee)
