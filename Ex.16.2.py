inventory = {
    "Pen": 50,
    "Notebook": 30,
    "Pencil": 20,
    "Eraser": 10
}

while True:
    print("\n1. Add Stock")
    print("2. Sell Item")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ").title()
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            inventory[item] = inventory.get(item, 0) + quantity
            print("Stock added successfully!")
        else:
            print("Invalid quantity!")

    elif choice == "2":
        item = input("Enter item name: ").title()
        quantity = int(input("Enter quantity sold: "))

        if quantity <= 0:
            print("Invalid quantity!")
        elif item in inventory and inventory[item] >= quantity:
            inventory[item] -= quantity
            print("Sale successful!")
        else:
            print("Item not found or insufficient stock!")

    elif choice == "3":
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(item, ":", quantity)

    elif choice == "4":
        print("Program ended!")
        break

    else:
        print("Invalid choice!")
