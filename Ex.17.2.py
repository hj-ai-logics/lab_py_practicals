import secrets
import string

def generate_otp():
    characters = string.ascii_uppercase + string.digits

    otp = ''.join(
        secrets.choice(characters) for _ in range(6)
    )

    print("Your OTP is:", otp)

generate_otp()
