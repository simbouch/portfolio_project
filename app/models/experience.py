# portfolio_project/app/models/experience.py

class Experience:
    def __init__(self, title, company, duration, description):
        self.title = title
        self.company = company
        self.duration = duration
        self.description = description

    def display_info(self):
        """Displays information about the experience."""
        return f"Experience: {self.title} at {self.company}, Duration: {self.duration}, Description: {self.description}"
