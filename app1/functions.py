FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of todo items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# print(__name__)
#
# if __name__ == "__main__":
#     print("Welcome to the Todos App Functions")


# Assign your accuracy score here
accuracy = 0.85

# Write your if statement here
if 0.0 <= accuracy <= 0.5:
    result = "Model performance: Poor."
elif 0.51 <= accuracy <= 0.75:
    result = "Model performance: Average."
elif 0.76 <= accuracy <= 0.90:
    result = "Model performance: Good."
elif 0.91 <= accuracy <= 1.0:
    result = "Model performance: Excellent."
else:
    result = "Invalid accuracy score."

# Check the result
print(result)

# Notebook grading
if result == "Model performance: Good.":
    print("Nice work!")
else:
    print("Not quite! Are your result strings formatted correctly?")


weight = 150
height = 1.93
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")


is_raining = False
is_sunny = False
if is_raining and is_sunny:
    print("Is there a rainbow?")


unsubscribed = False
location = "USA"
if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
