from src.task_manager import add_task, delete_task, list_tasks, complete_task
from src.file_handler import load_tasks

#functions
def show_list_options(tasks):
    print("\nWhat Tasks do you want listed?")
    print("1. All Tasks")
    print("2. Pending Tasks")
    print("3. Completed Tasks")

    choice = input("Enter your choice: ")
    if choice == "1":
        list_tasks(tasks)
    elif choice == "2":
        list_tasks(tasks, "pending")
    elif choice == "3":
        list_tasks(tasks, "completed")

#main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (DD-MM-YYYY): ")
            add_task(tasks, title, description, due_date)
        elif choice == "2":
            title = input("Title of the task to complete: ")
            if complete_task(tasks, title):
                print(f"Task: {title}. is now completed.")
        elif choice == "3":
            title = input("Title of the task to delete: ")
            if delete_task(tasks, title):
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        elif choice == "4":
            show_list_options(tasks)
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
