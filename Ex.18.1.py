# Simple Diary Application

def add_entry():
    entry = input("Write your diary entry: ")

    with open("diary.txt", "a") as file:
        file.write(entry + "\n\n")

    print("Diary entry saved successfully!")


add_entry()
