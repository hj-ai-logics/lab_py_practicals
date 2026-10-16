# Geometric Calculations

import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

while True:
    print("\n--- Geometric Calculator ---")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        radius = float(input("Enter radius: "))

        if radius >= 0:
            print("Area of Circle:", round(circle_area(radius), 2))
        else:
            print("Radius cannot be negative.")

    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        if length >= 0 and width >= 0:
            print("Area of Rectangle:", rectangle_area(length, width))
        else:
            print("Dimensions cannot be negative.")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
