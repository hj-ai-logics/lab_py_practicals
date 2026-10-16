# Phonebook Application

phonebook = {}

while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        number = input("Enter phone number: ").strip()

        if name in phonebook:
            print("Contact already exists!")
        else:
            phonebook[name] = number
            print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in phonebook:
            print("Phone Number:", phonebook[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to delete: ").strip()

        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        if phonebook:
            print("\nComplete Phonebook:")
            for name, number in sorted(phonebook.items()):
                print(name, ":", number)
        else:
            print("Phonebook is empty!")

    elif choice == "5":
        print("Exiting Phonebook. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
