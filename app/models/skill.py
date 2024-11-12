# portfolio_project/app/models/skill.py

# portfolio_project/app/models/skill.py

class Skill:
    def __init__(self, name, proficiency, description=""):
        self.name = name
        self.proficiency = proficiency
        self.description = description

    def display_info(self):
        """Displays the information about the skill."""
        return f"Skill: {self.name}, Proficiency: {self.proficiency}, Description: {self.description}"
