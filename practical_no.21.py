# Create a Simple Attendance Management System to record and display student attendance details.
# Lists, dictionaries, file handling .

# Simple Attendance Management System

import json
import os

FILE_NAME = "attendance.json"

def load_attendance():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def mark_attendance(attendance):
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    status = input("Enter Attendance (Present/Absent): ").strip().capitalize()

    if status not in ["Present", "Absent"]:
        print("Invalid attendance status!")
        return

    attendance[roll] = {"name": name, "status": status}

    with open(FILE_NAME, "w") as file:
        json.dump(attendance, file, indent=4)

    print("Attendance recorded successfully!")

def display_attendance(attendance):
    if not attendance:
        print("No attendance records found.")
        return

    print("\n--- Attendance Records ---")
    for roll, details in attendance.items():
        print("Roll Number:", roll)
        print("Name:", details["name"])
        print("Status:", details["status"])
        print("------------------------")

def main():
    attendance = load_attendance()

    while True:
        print("\n1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance(attendance)
        elif choice == "2":
            display_attendance(attendance)
        elif choice == "3":
            print("Exiting Attendance System.")
            break
        else:
            print("Invalid choice! Try again.")

main()
