# Dictionary Lookup Utility

student = {
    "name": "Harshvardhan",
    "age": 20,
    "course": "AIML",
    "college": "AITRC Vita"
}

try:
    key = input("Enter the key to search: ").lower()

    print("Value:", student[key])

except KeyError:
    print("Item Not Found!")
