# Compliance Screening Portal

questions = [
    ("Should passwords be kept confidential?", "true"),
    ("Is sharing confidential data without permission safe?", "false"),
    ("Should security incidents be reported?", "true"),
    ("Can unknown email attachments always be trusted?", "false"),
    ("Should company policies be followed?", "true")
]

score = 0
total = len(questions)

print("===== COMPLIANCE SCREENING PORTAL =====")
print("Answer each question with True or False.\n")

for i, (question, correct_answer) in enumerate(questions, start=1):
    print(f"Q{i}. {question}")
    answer = input("Your answer (True/False): ").strip().lower()

    if answer in ("true", "false"):
        if answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    else:
        print("Invalid answer. Marked incorrect.\n")

accuracy = (score / total) * 100

print("===== FINAL RESULT =====")
print("Total Questions:", total)
print("Correct Answers:", score)
print(f"Accuracy: {accuracy:.2f}%")

if accuracy >= 80:
    print("Status: PASS")
else:
    print("Status: FAIL")
