date = input("Enter today's date: ")
mood = ("How do you rate your mood today from 1 to 10: ")
thoughts = ("Let your thoughts flow:\n")

with open(f"{date}.txt", "w") as file:
    file.write(mood)
    file.write(thoughts)
