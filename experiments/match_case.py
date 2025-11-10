""" Using a simple match case logic"""

todos = []

while True:
    user_action = input("Enter your action (add, show, delete, or quit): ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "delete":
            delete_todo = input("Enter the todo you want to delete: e.g: 1, 2, 3")
            del todos[int(delete_todo) - 1]
        case "quit":
            break
print("Thanks for using the to do app!")
