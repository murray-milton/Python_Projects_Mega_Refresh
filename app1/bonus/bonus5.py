user_action = input("Add a new member: ")

file = open("../files/members.txt", "r")
members = file.readlines()
file.close()

members.append(user_action)

file = open("../files/members.txt", "w")
file.writelines(members)
file.close()
