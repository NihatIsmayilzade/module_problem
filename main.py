from todo_list import TodoList

todo = TodoList()

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. Complete task")
    print("3. Remove task")
    print("4. Show tasks")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter task: ")
        todo.add_task(name)

    elif choice == "2":
        todo.show_tasks()
        number = int(input("Enter task number: "))
        todo.complete_task(number - 1)

    elif choice == "3":
        todo.show_tasks()
        number = int(input("Enter task number: "))
        todo.remove_task(number - 1)

    elif choice == "4":
        todo.show_tasks()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")