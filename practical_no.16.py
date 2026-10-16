# Create a Banking Menu System using modular functions for deposit, withdrawal, and balance inquiry.
# Functions, modular programming.

balance = 5000

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
        print("New balance:", balance)
    else:
        print("Enter a valid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount > 0 and amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)
    elif amount > balance:
        print("Insufficient balance.")
    else:
        print("Enter a valid amount.")

def check_balance():
    print("Your current balance is:", balance)

while True:
    print("\n--- BANKING MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        print("Thank you for using the Banking System.")
        break
    else:
        print("Invalid choice. Please try again.")
