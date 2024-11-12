# portfolio_project/app/models/project.py

class Project:
    def __init__(self, title, description, technology_used, duration):
        self.title = title
        self.description = description
        self.technology_used = technology_used
        self.duration = duration

    def display_info(self):
        """Displays the basic info of a project."""
        return f"Project: {self.title}, Technologies: {self.technology_used}, Duration: {self.duration}"

class WebProject(Project):
    def __init__(self, title, description, technology_used, duration, frontend, backend):
        super().__init__(title, description, technology_used, duration)
        self.frontend = frontend
        self.backend = backend

    def display_info(self):
        """Displays info specific to a web project."""
        base_info = super().display_info()
        return f"{base_info}, Frontend: {self.frontend}, Backend: {self.backend}"

class DataScienceProject(Project):
    def __init__(self, title, description, technology_used, duration, algorithms):
        super().__init__(title, description, technology_used, duration)
        self.algorithms = algorithms

    def display_info(self):
        """Displays info specific to a data science project."""
        base_info = super().display_info()
        return f"{base_info}, Algorithms: {', '.join(self.algorithms)}"
