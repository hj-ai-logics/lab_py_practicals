# Create a Customer Feedback Formatter that formats feedback messages professionally.
# String formatting, built-in string methods 


raw_name = input("Enter customer name: ")
raw_feedback = input("Enter feedback message: ")
rating = input("Enter rating (1 to 5): ")

# -----------------------------------------
# CONCEPT 1: BUILT-IN STRING METHODS
# -----------------------------------------

# 1. Remove unwanted spaces
clean_name = raw_name.strip()
clean_feedback = raw_feedback.strip()

# 2. Capitalize the first letter of each word
formatted_name = clean_name.title()

# 3. Capitalize the first letter of the message
formatted_feedback = clean_feedback.capitalize()

# 4. Replace common abbreviations
formatted_feedback = formatted_feedback.replace(" u ", " you ").replace(" r ", " are ")

# 5. Count exclamation marks
exclamation_count = formatted_feedback.count("!")

# 6. Convert category to uppercase
if int(rating) >= 4:
    category = "POSITIVE".upper()
else:
    category = "NEEDS REVIEW".upper()

# -----------------------------------------
# CONCEPT 2: STRING FORMATTING (f-strings)
# -----------------------------------------

print("\n" + "=" * 45)
print(f"{'PROFESSIONAL FEEDBACK REPORT':^45}")
print("=" * 45)

print(f"Customer Name : {formatted_name}")
print(f"Rating        : {rating} / 5 Stars")
print(f"Category      : {category}")
print(f"Excitement    : {exclamation_count} exclamation mark(s)")

print("-" * 45)
print("Formatted Message:")
print(f"{formatted_feedback}")
print("=" * 45)
