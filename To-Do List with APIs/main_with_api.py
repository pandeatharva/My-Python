import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

# List all to-do items
def list_todos():
    response = requests.get(BASE_URL)
    todos = response.json()[:5]  # Get first 5 tasks
    for todo in todos:
        print(f"{todo['id']}. {todo['title']} - {'Completed' if todo['completed'] else 'Not Completed'}")

# Add a new to-do item
def add_todo():
    title = input("Enter the title of the new to-do item: ")
    data = {
        "title": title,
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=data)
    print(f"Added To-Do: {response.json()}")

# Mark a to-do item as completed
def mark_as_completed(todo_id):
    url = f"{BASE_URL}/{todo_id}"
    data = {
        "completed": True
    }
    response = requests.patch(url, json=data)
    print(f"To-Do Updated: {response.json()}")

# Menu
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. List To-Dos")
        print("2. Add To-Do")
        print("3. Mark To-Do as Completed")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            todo_id = input("Enter To-Do ID to mark as completed: ")
            mark_as_completed(todo_id)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
