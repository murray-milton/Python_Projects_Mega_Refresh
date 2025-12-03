filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]
print(filenames)

names = ["john smith", "jay santi", "eva kuki"]

names_capitalized = [name.title() for name in names]
print(names_capitalized)

usernames = ["john 1990", "alberta1970", "magnola2000"]

user_entries = ["10", "19.1", "20"]
converted_float = []
for username, user_entry in zip(usernames, user_entries):
    converted_float.append(float(user_entry))
print(converted_float)


numbers = [10, 20, 30]

multiple = [numb * 2 for numb in numbers]
print(multiple)

new = [i for i in ["a", "b", "c"]]
print(new)
