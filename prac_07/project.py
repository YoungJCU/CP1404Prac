from datetime import datetime

class Project:
    """Represent a project with its details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage != "":
            self.completion_percentage = int(new_percentage)
        if new_priority != "":
            self.priority = int(new_priority)

    def __lt__(self, other):
        return self.priority < other.priority
