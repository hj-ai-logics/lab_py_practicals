# Student Contact Database

contacts = {
    101: "student1@gmail.com",
    102: "student2@gmail.com",
    103: "student3@gmail.com",
    104: "student4@gmail.com",
    105: "student5@gmail.com"
}

roll_no = int(input("Enter student roll number: "))

if roll_no in contacts:
    print("Email Address:", contacts[roll_no])
else:
    print("Student contact not found.")
