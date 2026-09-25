# Active Inventory Catalog Manager

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

# Take item name from user
item = input("Enter product name to search: ")

# Search for the item
if item in products:
    index = products.index(item)
    print("Item found!")
    print("Product:", item)
    print("Index location:", index)
else:
    print("Item not found in inventory.")
