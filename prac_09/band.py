"""
CP1404 - Practical
Band
"""


class Band:
    """Band class to manage a group of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band, showing all musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing what each musician in the Band is playing."""
        return "\n".join(musician.play() for musician in self.musicians)
