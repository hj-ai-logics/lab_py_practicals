# Develop an Online Quiz System that asks multiple-choice questions, checks answers, and displays the final score.
# Conditional statements, loops, lists, functions.

# Online Quiz System

def start_quiz():
    questions = [
        {
            "question": "1. Which language is used for Python programming?",
            "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
            "answer": "B"
        },
        {
            "question": "2. Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "3. Which data type stores multiple items in Python?",
            "options": ["A. List", "B. Integer", "C. Float", "D. Boolean"],
            "answer": "A"
        },
        {
            "question": "4. Which loop is used to iterate over a sequence?",
            "options": ["A. if", "B. for", "C. else", "D. break"],
            "answer": "B"
        },
        {
            "question": "5. What is the output of 2 + 3?",
            "options": ["A. 4", "B. 6", "C. 5", "D. 3"],
            "answer": "C"
        }
    ]

    score = 0

    print("===== ONLINE QUIZ SYSTEM =====")

    for q in questions:
        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid input! Please enter A, B, C, or D.")
            answer = input("Enter your answer: ").strip().upper()

        if answer == q["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer! Correct answer:", q["answer"])

    print("\n===== QUIZ RESULT =====")
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(questions) - score)
    print("Final Score:", score, "/", len(questions))
    print("Percentage:", (score / len(questions)) * 100, "%")


start_quiz()
