"""
CP1404 - Practical
Project
Estimate: 1 hour
Actual:
"""

from datetime import datetime


class Project:
    """Represent a project with basic details."""

    def __init__(self, name, start_date, priority, estimate, completion_percent):
        """Initialize a project with name, start date, priority, estimate, and completion percentage."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion_percent = int(completion_percent)

    def __str__(self):
        """Return a formatted string of the project's details."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority}, estimate: ${self.estimate:,.2f}, "
                f"completion: {self.completion_percent}%")