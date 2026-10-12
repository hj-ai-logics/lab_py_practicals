# Create a Library Book Record System to store and update book details.
# Dictionaries, key-value pairs, dictionary operations.
library = {}

while True:
    print("\n--- Library Book Record System ---")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Update Book Details")
    print("4. Search Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")

        if book_id in library:
            print("Book ID already exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = input("Enter Publication Year: ")

            library[book_id] = {
                "title": title,
                "author": author,
                "year": year
            }

            print("Book added successfully!")

    elif choice == "2":
        if not library:
            print("No book records found.")
        else:
            for book_id, details in library.items():
                print("\nBook ID:", book_id)
                print("Title:", details["title"])
                print("Author:", details["author"])
                print("Year:", details["year"])

    elif choice == "3":
        book_id = input("Enter Book ID to update: ")

        if book_id in library:
            print("1. Update Title")
            print("2. Update Author")
            print("3. Update Publication Year")

            field = input("Choose a field: ")

            if field == "1":
                library[book_id]["title"] = input("Enter new title: ")
                print("Title updated successfully!")
            elif field == "2":
                library[book_id]["author"] = input("Enter new author: ")
                print("Author updated successfully!")
            elif field == "3":
                library[book_id]["year"] = input("Enter new year: ")
                print("Year updated successfully!")
            else:
                print("Invalid field choice.")
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Enter Book ID to search: ")

        if book_id in library:
            print("Book Details:", library[book_id])
        else:
            print("Book not found.")

    elif choice == "5":
        book_id = input("Enter Book ID to delete: ")

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    elif choice == "6":
        print("Exiting Library Book Record System.")
        break

    else:
        print("Invalid choice. Please try again.")
