# Vocabulary Flashcard Application

flashcards = {
    "Artificial Intelligence": "Technology that enables machines to perform tasks requiring human intelligence.",
    "Machine Learning": "A branch of AI that allows computers to learn from data.",
    "Python": "A high-level programming language.",
    "Algorithm": "A step-by-step procedure to solve a problem.",
    "Database": "An organized collection of data."
}

score = 0
total = len(flashcards)

print("===== VOCABULARY FLASHCARDS =====")

for word, definition in flashcards.items():
    print("\nWord:", word)
    answer = input("Enter the definition: ").strip()

    print("Correct Definition:", definition)

    if answer.lower() == definition.lower():
        print("Correct Answer!")
        score += 1
    else:
        print("Incorrect Answer!")

accuracy = (score / total) * 100

print("\n===== FINAL RESULT =====")
print("Total Questions:", total)
print("Correct Answers:", score)
print("Accuracy:", accuracy, "%")
