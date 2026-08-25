text = input("Enter email/text: ")

count_at = text.count('@')
count_comma = text.count(',')
count_exclamation = text.count('!')

print("@ =", count_at)
print(", =", count_comma)
print("! =", count_exclamation)
