import os


# Step 1: Load existing tasks from file (if any)
def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks


# Step 2: Save tasks to file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


# Step 3: Display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()


# Step 4: Add a task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!\n")
    else:
        print("Invalid task. Task cannot be empty.\n")


# Step 5: Delete a task
def delete_task(tasks):
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully!\n")
        else:
            print("Invalid task number. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a valid task number.\n")


# Step 6: Main program loop
def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("To-Do List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        print()  # Add a blank line for better readability

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '3':
            if tasks:
                delete_task(tasks)
                save_tasks(tasks, filename)
            else:
                print("No tasks to delete.\n")
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")


# Step 7: Run the main program
if __name__ == '__main__':
    main()