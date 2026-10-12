# Inventory Management System

inventory = {
    "Pen": 50,
    "Notebook": 30,
    "Pencil": 20,
    "Eraser": 10
}

print("Current Inventory:")
print(inventory)

item = input("\nEnter item name sold: ")
quantity = int(input("Enter quantity sold: "))

if item in inventory:
    if quantity <= inventory[item]:
        inventory[item] -= quantity
        print("Sale successful!")

        if inventory[item] == 0:
            print("Warning: Stock has dropped to zero!")
    else:
        print("Warning: Insufficient stock!")
else:
    print("Item not found in inventory.")

print("\nUpdated Inventory:")
for item, stock in inventory.items():
    print(item, ":", stock)
