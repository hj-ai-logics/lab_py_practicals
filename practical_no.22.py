# Mini Project:
  # Develop a real-world application such as Student Management System / Expense Tracker / Library Management System.
  # Integrating functions, data structures, lists, dictionaries, file handling, exception handling, modules

# Mini Project: Student Management System

import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error reading student records.")
    return {}


def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error saving student records.")


def add_student(students):
    try:
        roll = input("Enter Roll Number: ").strip()

        if not roll:
            print("Roll number cannot be empty.")
            return

        if roll in students:
            print("Student already exists.")
            return

        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        if not name or age <= 0 or not 0 <= marks <= 100:
            print("Invalid student details.")
            return

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        save_students(students)
        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for roll, details in students.items():
        print("Roll Number:", roll)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Marks:", details["marks"])
        print("-----------------------")


def search_student(students):
    roll = input("Enter Roll Number to search: ").strip()

    if roll in students:
        print("Student Details:", students[roll])
    else:
        print("Student not found.")


def delete_student(students):
    roll = input("Enter Roll Number to delete: ").strip()

    if roll in students:
        del students[roll]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
