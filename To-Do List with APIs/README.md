TO-DO List Application without APIs

A simple command-line to-do list application built in Python that allows users to manage tasks, save them to a file, and handle invalid input/errors.
Features

Add Task: Add new tasks to the list.
Display Tasks: View all tasks in the current list.
Delete Task: Remove tasks by task number.
Save/Load Tasks: Automatically save tasks to tasks.txt and load them when the app starts.
Error Handling: Handles invalid inputs such as empty tasks, non-existent task numbers, and invalid menu choices.

How It Works

The application displays a menu with options to add, view, or delete tasks.
Tasks are saved to tasks.txt after every change (add or delete).
Error handling is implemented to handle invalid inputs gracefully.

Usage

Display Tasks: View the current list of tasks.
Add Task: Add a task by providing a description.
Delete Task: Remove a task by entering its task number.
Exit: Exit the application; tasks will be saved automatically.

Example:


To-Do List Menu:
1. Display tasks
2. Add task
3. Delete task
4. Exit
Choose an option: 2

Enter a new task: Buy groceries
Task 'Buy groceries' added successfully!