from functions import get_todos, write_todos

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

    if user_action.startswith("add"):
        todo = user_action[4:].title() + "\n"

        todos = get_todos("files/todos.txt")

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos("files/todos.txt")

        for index, todo in enumerate(todos):
            item = todo.strip("\n")
            print(f"{index + 1}.{item.title()}")

    elif "delete" in user_action:
        delete_todo = input("Enter the todo you want to delete: e.g: 1, 2, 3: ")

        todos = get_todos()

        del todos[int(delete_todo) - 1]

        write_todos(todos)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("Enter your new todo: ")
            todos[int(number) - 1] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Invalid number. Please try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            removed_todo = todos[number - 1]
            todos.pop(number - 1)

            write_todos(todos)

            print(
                f"The following todo has been marked as completed: {removed_todo.strip('\n')}"
            )
        except IndexError:
            print("There is no todo in that range. Please try again.")
            continue

    elif user_action.startswith("quit"):
        break

    else:
        print("Invalid action. Please try again.")

print("Thanks for using the to do app!")
