# Create a Student Record File System to store and retrieve student details from files.
# File handling, file modes, read/write operations.
# Student Record File System
def add_student():
 with open("students.txt", "a") as file:
 roll = input("Enter Roll Number: ")
 name = input("Enter Student Name: ")
 marks = input("Enter Marks: ")
 file.write(f"{roll},{name},{marks}\n")
 print("Student record saved successfully!")
def view_students():
 try:
 with open("students.txt", "r") as file:
 print("\nStudent Records:")
 for line in file:
 roll, name, marks = line.strip().split(",")
 print("Roll Number:", roll)
 print("Name:", name)
 print("Marks:", marks)
 print("-------------------")
 except FileNotFoundError:
 print("No student records found.")
while True:
 print("\n1. Add Student")
 print("2. View Students")
 print("3. Exit")
 choice = input("Enter your choice: ")
 if choice == "1":
 add_student()
 elif choice == "2":
 view_students()
 elif choice == "3":
 print("Exiting program.")
 break
 else: print("Invalid choice. Try again.")
