special_characters = ["@", "#", "$", "%", "^", "&", "*", "_", "*"]


user_password = input("Enter new password: ")

check_password = {}


if len(user_password) >= 8:
    """Checksum for password"""
    check_password["length"] = True
else:
    check_password["length"] = False


digit = False
for i in user_password:
    if i.isdigit():
        digit = True

check_password["digit"] = digit


upper_case = False
for i in user_password:
    if i.isupper():
        upper_case = True

check_password["upper_case"] = upper_case

print(check_password)

if all(check_password.values()):
    print("Password is strong!")
else:
    print("Password is weak!")
