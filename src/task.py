from datetime import datetime, date
from dateutil.relativedelta import relativedelta

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
        """
        Property for displaying the due date of the task.
        Returns:
            str: representing the existing due date value of the task.
        """
        if not self.due_date:
            return "No Due Date"
        elif isinstance(self.due_date, datetime):
            return self.due_date.strftime("%d-%m-%Y")
        else: return "ERROR: attr due_date is not datetime obj."

    @property
    def date_created_display(self):
        """
        used to display the creation date private property
        Returns:
            str: Of the date created.
        """
        return self._date_created.strftime("%d-%m-%Y")

    @property
    def time_left(self):
        """
        to display in human-readable text the time left for a due date.
        Returns:
            str: represents the time left or time overdue relative to the due date.
        """
        if self.due_date is None:
            return "Null"
        due = self.due_date.date()
        overdue = due < date.today()
        if overdue:
            delta = relativedelta(date.today(), due)
        else:
            delta = relativedelta(due, date.today())
        text = f"{delta.years} years, {delta.months} months, {delta.days} days"
        return f"Time Overdue: {text}" if overdue else f"Time Left: {text}"