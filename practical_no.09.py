# Develop a Student Marks Management System using lists for storing and updating marks.
# Lists, insertion, deletion, traversal.

# Student Marks Management System (Marks Only)
student_marks = []

while True:
    print("========================================")
    print("    STUDENT MARKS MANAGEMENT SYSTEM     ")
    print("========================================")
    print("1. Insert Marks")
    print("2. Delete Marks")
    print("3. Update Marks")
    print("4. Display All Marks")
    print("5. Search for a Mark")
    print("6. Exit")
    print("========================================")
    
    choice = input("Enter your choice (1-6): ").strip()
    print() 

    # 1. INSERTION
    if choice == "1":
        marks = float(input("Enter student marks to add: "))
        student_marks.append(marks)
        print(f"Success: Marks {marks} added.\n")

    # 2. DELETION
    elif choice == "2":
        marks = float(input("Enter the exact marks value to delete: "))
        if marks in student_marks:
            student_marks.remove(marks)
            print(f"Success: Marks {marks} removed.\n")
        else:
            print(f"Error: Marks value {marks} not found in the list.\n")

    # 3. UPDATE
    elif choice == "3":
        if len(student_marks) == 0:
            print("No records available to update.\n")
        else:
            print("Current positions available:")
            for i in range(len(student_marks)):
                print(f"Index {i}: {student_marks[i]}")
            
            index = int(input("Enter the index number you want to update: "))
            if 0 <= index < len(student_marks):
                new_marks = float(input(f"Enter new marks for index {index}: "))
                student_marks[index] = new_marks
                print("Success: Marks updated successfully.\n")
            else:
                print("Error: Invalid index position.\n")

    # 4. DISPLAY ALL
    elif choice == "4":
        if len(student_marks) == 0:
            print("No marks recorded yet.\n")
        else:
            print("Recorded Marks List:")
            for i in range(len(student_marks)):
                print(f"Student {i + 1}: {student_marks[i]}")
            print()

    # 5. SEARCH
    elif choice == "5":
        marks = float(input("Enter marks value to search: "))
        if marks in student_marks:
            count = student_marks.count(marks)
            print(f"Found! The mark {marks} exists in the list (appears {count} time(s)).\n")
        else:
            print(f"The mark {marks} was not found.\n")

    # 6. EXIT
    elif choice == "6":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.\n")
