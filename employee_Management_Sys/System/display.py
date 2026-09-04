import time

from art import text2art
from termcolor import colored
from tabulate import tabulate
from tqdm import tqdm

TABLE_HEADERS = ["Name", "Age", "Employee ID", "Department", "Position"]


# ---------- output helpers ----------

def print_success(msg):
    print(colored(f"[OK] {msg}", "green"))


def print_error(msg):
    print(colored(f"[ERROR] {msg}", "red"))


def print_info(msg):
    print(colored(f"[i] {msg}", "cyan"))


def show_banner():
    banner = text2art("EMS", font="small")
    print(colored(banner, "blue"))
    print(colored("        Employee Management System", "yellow"))
    print()


def loading_screen():
    for _ in tqdm(range(100), desc="Starting up", ncols=60, colour="green"):
        time.sleep(0.01)
    print()


def print_employee_table(employees):
    if not employees:
        print_info("No employees to show.")
        return
    rows = [emp.to_row() for emp in employees]
    print(tabulate(rows, headers=TABLE_HEADERS, tablefmt="fancy_grid"))


# ---------- input helpers ----------

def ask_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print_error("This field cannot be empty.")


def ask_age(prompt):
    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print_error("Age must be a whole number.")
            continue
        age = int(value)
        if age <= 0 or age > 120:
            print_error("Age must be between 1 and 120.")
            continue
        return ageS