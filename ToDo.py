tasks = []  # list that saves all the tasks added till now

def show_menu():
    print("\n___To-Do___")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task added: {task}")

def view_task():
    if not tasks:
        print("No tasks have been entered yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_task()
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Task '{removed}' is removed")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# main loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print("Please enter a valid option! (1-4)")

