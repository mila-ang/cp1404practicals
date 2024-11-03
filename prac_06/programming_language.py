"""
CP1404 - Practical
Programming Language
Estimate: 15 minutes
Actual:
"""


class ProgrammingLanguage:
    """Represent a programming language with typing, reflection, and year of origin."""

    def __init__(self, name, typing, reflection, year):
        """Initialize the programming language with its attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"