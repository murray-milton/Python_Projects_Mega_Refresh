"""
Purpose: Simple command-line TODO list refresher
Description:
    This script demonstrates basic Python control flow, user input,
    and list handling. The program allows users to enter multiple
    TODO items interactively, storing them in memory, and printing
    them neatly once the user finishes.
"""


def edit_todos(todo) -> None:
    todo_number = int(
        input("Please enter the number of the todo, which you want to edit:")
    )
    todo_number = todo_number - 1
    new_todo = input("Enter your new todo: ")
    todo[todo_number] = new_todo


def main() -> None:
    # Initialize an empty list to hold TODO items
    todos: list[str] = []

    while True:
        # Prompt the user for a new TODO item
        todo_item = input("Enter a TODO item: ").strip()

        # Add the item if it is not empty
        if todo_item:
            todos.append(todo_item)
            print(f"Added: '{todo_item}'.")
        else:
            print("Empty input ignored. Please enter a valid TODO.")
        edit_todo = (
            input("Would you like to edit any of your TODOs? (y/n): ").lower().strip()
        )
        if edit_todo == "y":
            edit_todos(todos)
        elif edit_todo == "n":
            continue
        else:
            print("Invalid choice. Ending program.")
            break
        # Controls the users adding of more TODOs
        user_choice = input("Add another? (y/n): ").lower().strip()

        # Decide whether to continue or exit
        if user_choice == "y":
            continue
        if user_choice == "n":
            break

        print("Invalid choice. Ending program.")
        break

    # Display the final list of TODOs
    print("\nYour TODO List")
    print("-" * 20)
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo}")


if __name__ == "__main__":
    main()
