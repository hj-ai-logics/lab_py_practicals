# Develop a Secure Login System with proper error handling and invalid input detection.
# Exception handling, try-except, validation logic.

# Secure Login System with Exception Handling
username_correct = "HARSHVARDHAN"
password_correct = "HARSH@9126"
try: username = input("Enter username: ").strip()
 password = input("Enter password: ")
 if not username or not password:
 raise ValueError("Username and password cannot be empty.")
 if username == username_correct and password == password_correct:
 print("Login successful!")
 else: print("Invalid username or password.")
except ValueError as e:
 print("Input Error:", e)
except Exception as e:
 print("An unexpected error occurred:", e
