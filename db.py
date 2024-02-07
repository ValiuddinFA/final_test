import sqlite3

def create_employee_table():
    """Create the employee table if it doesn't exist"""
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY, name TEXT, position TEXT, department TEXT)''')
    conn.commit()
    conn.close()

def add_employee(name, position, department):
    """Add an employee to the database"""
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (name, position, department) VALUES (?, ?, ?)", (name, position, department))
    conn.commit()
    conn.close()

def get_employees():
    """Retrieve all employees from the database"""
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    employees = c.fetchall()
    conn.close()
    return employees
