# Set up Python environment and create a “Student Introduction System” that accepts student details and displays formatted information. 
#  Python installation, print(), input(), variables, syntax 
print("=== Student Introduction System ===")
    
    # Accept student details
name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter enrolled course: ")
college = input("Enter college name: ")
hobbies = input("Enter hobbies (comma separated): ")
prn=input("Enter the PRN no. of student : ")

    # Display formatted information
print("\n--- Student Profile ---")
print(f" Name      : {name}")
print(f"Age       : {age}")
print(f"Course    : {course}")
print(f"college   : {college}")
print(f" Hobbies   : {hobbies}")
print("PRN :",prn)

print("------------------------")

