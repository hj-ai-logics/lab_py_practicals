# Develop a text analyzer  tool to count words, vowels,spaces,and character in the paragraph .
# String,indexing,slicing,string traversal.

# Text Analyzer

paragraph = input("Enter a paragraph: ")

words = len(paragraph.split())
vowels = 0
spaces = 0
characters = len(paragraph)

for ch in paragraph:
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1

print("\n--- Text Analysis ---")
print("Words      :", words)
print("Vowels     :", vowels)
print("Spaces     :", spaces)
print("Characters :", characters)
