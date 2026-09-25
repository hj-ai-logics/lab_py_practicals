# Create a Product Inventory System to search, sort, and manage product prices.
# List methods, sorting, searching

# Product Inventory System

products = [
    ["Laptop", 55000],
    ["Mobile", 20000],
    ["Headphones", 2500],
    ["Keyboard", 1200],
    ["Mouse", 700]
]

while True:
    print("\n===== PRODUCT INVENTORY SYSTEM =====")
    print("1. Display Products")
    print("2. Add Product")
    print("3. Search Product")
    print("4. Sort Products by Price")
    print("5. Update Price")
    print("6. Delete Product")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Display products
    if choice == 1:
        print("\nProduct\t\tPrice")
        for product in products:
            print(product[0], "\t\t₹", product[1])

    # Add product
    elif choice == 2:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))

        products.append([name, price])
        print("Product added successfully!")

    # Search product
    elif choice == 3:
        name = input("Enter product name to search: ")

        found = False

        for product in products:
            if product[0].lower() == name.lower():
                print("Product Found!")
                print("Name:", product[0])
                print("Price: ₹", product[1])
                found = True
                break

        if not found:
            print("Product not found.")

    # Sort products
    elif choice == 4:
        products.sort(key=lambda x: x[1])

        print("\nProducts sorted by price:")
        for product in products:
            print(product[0], "₹", product[1])

    # Update price
    elif choice == 5:
        name = input("Enter product name: ")

        found = False

        for product in products:
            if product[0].lower() == name.lower():
                new_price = float(input("Enter new price: "))
                product[1] = new_price
                print("Price updated successfully!")
                found = True
                break

        if not found:
            print("Product not found.")

    # Delete product
    elif choice == 6:
        name = input("Enter product name to delete: ")

        found = False

        for product in products:
            if product[0].lower() == name.lower():
                products.remove(product)
                print("Product deleted successfully!")
                found = True
                break

        if not found:
            print("Product not found.")

    # Exit
    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
