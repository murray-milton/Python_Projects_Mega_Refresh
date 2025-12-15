elements = {
    "hydrogen": {"number": 1, "weight": 1.00794, "symbol": "H"},
    "helium": {"number": 2, "weight": 4.002602, "symbol": "He"},
}


helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight

oxygen = {
    "number": 8,
    "weight": 15.999,
    "symbol": "O",
}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print("elements = ", elements)

print(helium)
print(hydrogen_weight)
print(elements)


# Student Record example
student_records = {
    "John": {"age": 20, "major": "Computer Science", "grades": [85, 90, 92]},
    "Emma": {"age": 19, "major": "Mathematics", "grades": [95, 88, 91]},
}


# Add a new student
new_student = {"age": 20, "major": "Physics", "grades": [85, 90, 92]}

student_records["Alex"] = new_student
print(student_records)
