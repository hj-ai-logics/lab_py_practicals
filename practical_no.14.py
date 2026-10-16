# Develop a Phonebook / Word Frequency Counter Application for storing contacts or analyzing text frequency.
# Dictionaries, string processing .

# Phonebook Application

phonebook = {}

while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        print("\nPhonebook:")
        for name, phone in phonebook.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in phonebook:
            print("Phone number:", phonebook[name])
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Thank you!")
        break
