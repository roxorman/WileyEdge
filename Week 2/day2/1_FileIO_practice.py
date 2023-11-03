import os

def create_todo_list(filename):
    try:
        with open(filename, 'w') as f:
            f.write("TODO LIST:\n")
        print("To-Do list created successfully")
    except IOError:
        print("Error while creating To-Do list")
        
def add_task(filename, task):
    try:
        with open(filename, 'a') as f:
            f.write('- ' + task + "\n")
        print("Task added to the to-do list: " + task)
    except IOError:
        print("Error while adding task to the to-do list")
        
def view_todo_list(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error while reading to-do list")
        
def complete_task(filename, task):
    try:
        with open(filename, 'a') as f:
            f.write('- ' + task + " [DONE]\n")
        print("Task completed: " + task)
    except IOError:
        print("Error while completing task")
        
def delete_todo_list(filename):
    try:
        os.remove(filename)
        print("To-Do list deleted successfully")
    except IOError:
        print("Error while deleting to-do list")
        
def main():
    filename = "todo.txt"
    create_todo_list(filename)
    
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View the to-do list")
        print("3. Complete a task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(filename, task)
        elif choice == "2":
            view_todo_list(filename)
        elif choice == "3":
            task = input("Enter a task to complete: ")
            complete_task(filename, task)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
if __name__ == "__main__":
    main()
        