"""
Purpose: Simple command-line TODO list refresher
Description:
    This script demonstrates basic Python control flow, user input,
    and list handling. The program allows users to enter multiple
    TODO items interactively, storing them in memory, and printing
    them neatly once the user finishes.
"""

"""Todo CLI that enable the user to add, show, delete, edit, and quit."""

greeting = "Welcome to the to do app!"
print(greeting.upper())
while True:
    user_action = (
        input("Enter your action (add, show, delete, edit, complete  or quit): ")
        .strip()
        .lower()
    )

    if "add" in user_action or "new" in user_action or "create" in user_action:
        todo = user_action[4:].title() + "\n"

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            item = todo.strip("\n")
            print(f"{ index + 1}.{item.title()}")

    elif "delete" in user_action:
        delete_todo = input("Enter the todo you want to delete: e.g: 1, 2, 3: ")

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        del todos[int(delete_todo) - 1]

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "edit" in user_action:
        number = int(user_action[5:])

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter your new todo: ")
        todos[int(number) - 1] = new_todo + "\n"

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        removed_todo = todos[number - 1]
        todos.pop(number - 1)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

        print(
            f"The following todo has been marked as completed: {removed_todo.strip('\n')}"
        )

    elif "quit" in user_action:
        break

    else:
        print("Invalid action. Please try again.")

print("Thanks for using the to do app!")
