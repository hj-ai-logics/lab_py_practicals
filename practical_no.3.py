# Eligibility Checker System

marks = int(input("Enter your marks: "))
age = int(input("Enter your age: "))

# Simple if
if marks >= 50 and age >= 18:
    print(" Eligible for admission")

# if–else
else:
    print(" Not eligible")

# More detailed decision-making with nested if
if marks >= 50:
    if age >= 18:
        print(" Eligible for admission")
    else:
        print(" Not eligible: Age must be at least 18")
else:
    if age >= 18:
        print(" Not eligible: Marks must be at least 50")
    else:
        print("Not eligible: Both marks and age criteria not met")
