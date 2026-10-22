from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

class Task:
    """
    A class to represent a task in the task management application.

    Attributes:
        title (str): The title of the task.
        description (str): A brief description of the task.
        due_date (datetime): The due date of the task in 'DD-MM-YYYY' format.
        status (str): The current status of the task, defaults to 'pending'.
    """

    def __init__(self, title, description, due_date, status="pending"):
        """
        Initialise a Task object with title, description, due date, and status.

        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            due_date (str): The due date of the task in 'YYYY-MM-DD' format.
            status (str, optional): The status of the task. Defaults to 'pending'.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self._date_created = datetime.today()

    def to_dict(self):
        """
        Convert the Task object into a dictionary representation.

        Returns:
            dict: A dictionary containing the task details with keys:
                  'title', 'description', 'due_date', and 'status'.
        """
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(task_data):
        """
        Create a Task object from a dictionary representation.

        Args:
            task_data (dict): A dictionary with keys:'title', 'description',
                                'due_date', optionally 'status'.

        Returns:
            Task: A new Task object created from the dictionary data.
        """
        return Task(
            task_data["title"],
            task_data["description"],
            task_data["due_date"],
            task_data.get("status", "pending")
        )


    @property
    def due_date_display(self):
        if not self.due_date:
            return "No Due Date"
        elif isinstance(self.due_date, datetime):
            return self.due_date.strftime("%d/%m/%Y")
        else: return "ERROR: attr due_date is not datetime obj."

    @property
    def date_created_display(self):
        return self._date_created.strftime("%d/%m/%Y")

    @property
    def days_left(self):
        if self.due_date is None:
            return "Null"
        return (self.due_date - datetime.today()).days