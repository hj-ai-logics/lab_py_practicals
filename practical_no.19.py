# Develop a Secure Login System with proper error handling and invalid input detection.
# Exception handling, try-except, validation logic.

# Secure Login System with Exception Handling
username = "harshvardhan S. jadhav"
password = "9126"

try:
    u = input("Enter username: ").strip()
    p = input("Enter password: ").strip()

    if not u or not p:
        raise ValueError("Username and password cannot be empty.")

    if u == username and p == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)
