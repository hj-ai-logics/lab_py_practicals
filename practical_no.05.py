#Develop a Monthly Expense Tracker that continuously records and calculates expenses entered by users. 
# for loop, while loop, accumulation logic 

expenses = []   # list to store expenses
total = 0       # accumulator for total expenses

print("=== Monthly Expense Tracker ===")
print("Enter your expenses. Type 'done' to finish.\n")

while True:
    entry = input("Enter expense amount (or 'done'): ")
    
    if entry.lower() == 'done':
        break
    
    try:
        amount = float(entry)   # convert input to number
        expenses.append(amount) # store expense
        total += amount         # accumulate total
    except ValueError:
        print("Invalid input! Please enter a number.")

# Display all expenses using for loop
print("\n--- Expense Summary ---")
for i, expense in enumerate(expenses, start=1):
    print(f"Expense {i}: ₹{expense:.2f}")

print(f"\nTotal Monthly Expenses: ₹{total:.2f}")
