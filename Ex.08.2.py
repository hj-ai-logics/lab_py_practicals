feedback = input("Enter feedback: ")

target_words = ["badword", "spam", "abuse"]

for word in target_words:
    feedback = feedback.replace(word, "****")

print("Moderated Feedback:", feedback)
