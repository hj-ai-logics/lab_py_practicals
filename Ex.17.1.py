import random

def roll_dice():
    try:
        num_dice = int(input("Enter the number of dice to roll: "))

        if num_dice <= 0:
            print("Please enter a positive number.")
            return

        total = 0
        print("\nDice Results:")

        for i in range(num_dice):
            result = random.randint(1, 6)
            print(f"Die {i + 1}: {result}")
            total += result

        print("Total Score:", total)

    except ValueError:
        print("Invalid input! Please enter an integer.")

roll_dice()
