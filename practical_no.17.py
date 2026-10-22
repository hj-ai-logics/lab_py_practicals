# Develop a Random Password Generator / Dice Simulator using built-in Python modules.
# Modules, math module, random module.
import random
import string
import math
# Random Password Generator
def password_generator():
 length = int(input("Enter password length: "))
 if length <= 0:
 print("Password length must be greater than 0.")
 return
 characters = string.ascii_letters + string.digits + string.punctuation
 password = ''.join(random.choice(characters) for _ in range(length))
 print("Generated Password:", password
# Dice Simulator
def dice_simulator():
 dice_count = int(input("Enter number of dice to roll: "))
 if dice_count <= 0:
 print("Number of dice must be greater than 0.") return
 rolls = [random.randint(1, 6) for _ in range(dice_count)]
 print("Dice Results:", rolls)
 print("Total:", sum(rolls))
 # Calculate average using math module
 average = math.fsum(rolls) / dice_count
 print("Average:", average)
# Main Menu
while True:
 print("\n--- Random Password Generator / Dice Simulator ---")
 print("1. Generate Random Password")
 print("2. Simulate Dice Roll")
 print("3. Exit")
 choice = input("Enter your choice (1-3): ")
 if choice == '1':
 password_generator()
 elif choice == '2':
 dice_simulator()
 elif choice == '3':
 print("Thank you for using the program!")
 break
 else: print("Invalid choice. Please try again.")
