from src.task import Task
from src.file_handler import save_tasks
from dateutil import parser


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the task list.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the new task.
        description (str): A brief description of the task.
        due_date (str): The due date of the task in 'DD-MM-YYYY' format.

    Returns:
        bool: True if the task is added successfully, False otherwise.

    Raises:
        ValueError: If the due date is not in the correct format.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    # Prevent duplicate tasks
    if any(task.title == title for task in tasks):
        print("Error: A task with this title already exists.")
        return False

    # Validate due date format
    if not due_date.strip():
        converted_date = None  # Accepts nothing e.g "no date set"
    else:
        converted_date = to_datetime(due_date)
        if not converted_date:  # if conversion fails
            print("Error: Invalid date format. Use Australian date order.")
            return False

    tasks.append(Task(title, description, converted_date))
    save_tasks(tasks)
    return True


def delete_task(tasks, title):
    """
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task to be deleted.

    Returns:
        bool: True if the task was found and deleted, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def list_tasks(tasks, status=None):
    """
    Display tasks in the task list, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): The status to filter tasks
        by (e.g., "pending" or "completed").

    Returns:
        None

    Side Effects:
        - Prints the list of tasks to the console.
    """
    if not status:
        # If status is not set
        filtered = tasks
    else:
        # Filter tasks based on their status
        filtered = []
        for task in tasks:
            if task.status == status:
                filtered.append(task)

    if not filtered:
        print("No tasks found.")
        return
    for task in filtered:
        print(
            f"{task.title} | {task.description} | "
            f"Due: {task.due_date_display} | Status: {task.status} |"
            f" Created: {task.date_created_display} | {task.time_left}"
        )


def filter_tasks_by_status(tasks, status):
    """
    Filter tasks by their status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str): The status to filter tasks by (e.g., "pending" or "completed").

    Returns:
        list: A list of Task objects that match the specified status.
    """
    return [task for task in tasks if task.status == status]


def to_datetime(value):
    """
    Converts strings to datetime objects with a flexible number of formats.

    Args:
        value (str): Input Value to be converted.

    Returns:
        datetime: the converted value.
    """
    if value is None or hasattr(value, "year"):
        return value
    try:
        return parser.parse(value, dayfirst=True)
    except (parser.ParserError, OverflowError):
        return False
      
      
def complete_task(tasks, title):
    """
    Change the status of a task from pending to completed based on its title.
    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task that will have its status changed:

    Returns:
        True if the task is found and changed, otherwise False.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title and task.status == "pending":
            task.status = "completed"
            save_tasks(tasks)
            return True
    return False
