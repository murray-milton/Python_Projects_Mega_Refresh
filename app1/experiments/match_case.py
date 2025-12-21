"""Todo CLI that enable the user to add, show, delete, edit, and quit."""

todos = []
greeting = "Welcome to the to do app!"
print(greeting.upper())
while True:
    user_action = (
        input("Enter your action (add, show, delete, edit, complete  or quit): ")
        .strip()
        .lower()
    )

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display" | "list":
            for index, todo in enumerate(todos):
                todo = todo.title()
                print(f"{index + 1}.{todo}")
        case "delete":
            delete_todo = input("Enter the todo you want to delete: e.g: 1, 2, 3")
            del todos[int(delete_todo) - 1]
        case "edit":
            edit_todos = input("Enter the todo you want to edit: e.g: 1, 2, 3")
            new_todo = input("Enter your new todo: ")
            todos[int(edit_todos) - 1] = new_todo
        case "complete":
            completed_todo = input("Which todo do you want to mark as completed?")
            del todos[int(completed_todo) - 1]
        case "quit":
            break
        case _:
            print("Invalid action. Please try again.")
print("Thanks for using the to do app!")
