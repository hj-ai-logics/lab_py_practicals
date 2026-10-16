balance = 0
history = []

while True:
    print("\n1. Add Funds")
    print("2. Pay Bill")
    print("3. Check Balance")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        if amount > 0:
            balance += amount
            history.append("Added Rs. " + str(amount))
            print("Money added successfully!")
        else:
            print("Invalid amount!")

    elif choice == "2":
        amount = float(input("Enter bill amount: "))
        if 0 < amount <= balance:
            balance -= amount
            history.append("Paid Rs. " + str(amount))
            print("Bill paid successfully!")
        else:
            print("Invalid amount or insufficient balance!")

    elif choice == "3":
        print("Balance: Rs.", balance)

    elif choice == "4":
        print("Transaction History:", history)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
