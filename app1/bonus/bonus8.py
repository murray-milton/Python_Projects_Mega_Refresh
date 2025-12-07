import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d")
journal = []
with open(f"../journal/{date}.txt", "x") as file:
    user_mood = input("How would you rate your day? (1-10): ")
    journal.append(user_mood)
    user_thoughts = input("What did you think of the day? ")
    journal.append(user_thoughts)

    for i, item in enumerate(journal):
        user_input = f"{i + 1}. {item}"
        file.write(user_input + "\n")

languages = ["English", "German", "Spanish"]

for language in languages:
    with open(f"../journal/{language}.txt", "x") as file:
        file.write(language)
