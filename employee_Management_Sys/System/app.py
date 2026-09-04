import sys

from termcolor import colored

from System.models import Person, Employee, InvalidAgeError, InvalidEmployeeIDError
from System.display import (
    show_banner, loading_screen, print_success, print_error, print_info,
    print_employee_table, ask_text, ask_age,
)


class EmployeeManagementApp:
    def __init__(self):
        self.employees = []
        self.load_sample_employees()

    def load_sample_employees(self):
        self.employees.append(Employee("Maria Santos", 28, "E001", "IT", "Software Developer"))
        self.employees.append(Employee("Juan Dela Cruz", 34, "E002", "HR", "Recruiter"))

    def find_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id.lower() == employee_id.lower():
                return emp
        return None

    def add_employee(self):
        print_info("Add a new employee")
        name = ask_text("Name: ")
        age = ask_age("Age: ")
        employee_id = ask_text("Employee ID: ")

        if self.find_employee(employee_id):
            print_error("An employee with this ID already exists.")
            return

        department = ask_text("Department: ")
        position = ask_text("Position: ")

        try:
            emp = Employee(name, age, employee_id, department, position)
        except (InvalidAgeError, InvalidEmployeeIDError) as e:
            print_error(str(e))
            return

        self.employees.append(emp)
        print_success(f"Employee '{emp.name}' added.")

    def view_employees(self):
        print_info("Employee list")
        print_employee_table(self.employees)

    def update_employee(self):
        employee_id = ask_text("Enter the Employee ID to update: ")
        emp = self.find_employee(employee_id)
        if not emp:
            print_error("No employee found with that ID.")
            return

        print_info("Leave a field blank to keep its current value.")
        name = input(f"Name [{emp.name}]: ").strip()
        age_input = input(f"Age [{emp.age}]: ").strip()
        department = input(f"Department [{emp.department}]: ").strip()
        position = input(f"Position [{emp.position}]: ").strip()

        age = None
        if age_input:
            if not age_input.isdigit():
                print_error("Age must be a whole number.")
                return
            age = int(age_input)

        try:
            emp.update_info(name=name or None, age=age,
                             department=department or None, position=position or None)
        except (InvalidAgeError, InvalidEmployeeIDError) as e:
            print_error(str(e))
            return

        print_success("Employee updated.")

    def delete_employee(self):
        employee_id = ask_text("Enter the Employee ID to delete: ")
        emp = self.find_employee(employee_id)
        if not emp:
            print_error("No employee found with that ID.")
            return

        confirm = input(f"Delete '{emp.name}'? (y/n): ").strip().lower()
        if confirm == "y":
            self.employees.remove(emp)
            print_success("Employee deleted.")
        else:
            print_info("Delete cancelled.")

    def search_employee(self):
        term = ask_text("Search by name or Employee ID: ").lower()
        results = [e for e in self.employees
                   if term in e.name.lower() or term in e.employee_id.lower()]
        print_employee_table(results)

    def oop_demo(self):
        employee_id = ask_text("Enter the Employee ID to inspect: ")
        emp = self.find_employee(employee_id)
        if not emp:
            print_error("No employee found with that ID.")
            return

        print_info("OOP Demo")
        print(f"isinstance(emp, Employee)       -> {isinstance(emp, Employee)}")
        print(f"isinstance(emp, Person)         -> {isinstance(emp, Person)}")
        print(f"issubclass(Employee, Person)    -> {issubclass(Employee, Person)}")
        print(f"emp.get_details()               -> {emp.get_details()}")

    def show_menu(self):
        print()
        print(colored("========== MAIN MENU ==========", "magenta"))
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. OOP Demo (isinstance / issubclass)")
        print("0. Exit")
        print(colored("================================", "magenta"))

    def run(self):
        show_banner()
        loading_screen()

        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.search_employee()
            elif choice == "6":
                self.oop_demo()
            elif choice == "0":
                print_info("Goodbye!")
                sys.exit(0)
            else:
                print_error("Invalid option, try again.")