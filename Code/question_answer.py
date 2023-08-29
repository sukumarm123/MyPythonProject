import json

with open("question_dic.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
    message = f"{index + 1} - Your answer is: {question['user_choice']} " \
              f"& Correct answer is: {question['correct_answer']}"
    print(message)

print("You have scored: ", score, "/", len(data))

if len(data) == score:
    print("Excellent.")
else:
    print("Better luck next time.")