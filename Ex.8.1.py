# Read user-submitted names
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Format names in title case
full_name = f"{first_name.title()} {last_name.title()}"

# Output the cleaned full name
print("Clean Full Name:", full_name)
