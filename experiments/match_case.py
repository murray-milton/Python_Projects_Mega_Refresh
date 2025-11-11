""" Using a simple match case logic"""

todos = []
greeting = "Welcome to the to do app!"
print(greeting.upper())
while True:
    user_action = (
        input("Enter your action (add, show, delete, edit,  or quit): ").strip().lower()
    )

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display" | "list":
            for todo in todos:
                todo = todo.title()
                print(todo)
        case "delete":
            delete_todo = input("Enter the todo you want to delete: e.g: 1, 2, 3")
            del todos[int(delete_todo) - 1]
        case "edit":
            edit_todos = input("Enter the todo you want to edit: e.g: 1, 2, 3")
            new_todo = input("Enter your new todo: ")
            todos[int(edit_todos) - 1] = new_todo
        case "quit":
            break
        case _:
            print("Invalid action. Please try again.")
print("Thanks for using the to do app!")
