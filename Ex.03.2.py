
score = float(input("Enter graduation score (%): "))
backlogs = int(input("Enter number of active academic backlogs: "))

if score >= 70 and backlogs == 0:
    print("Eligible for Placement")
else:
    print("Not Eligible for Placement")
