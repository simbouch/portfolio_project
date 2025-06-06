# portfolio_project/app/models/skill.py

from datetime import datetime, timezone
from .. import db

class Skill(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)  # 1-100 scale
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))  # For icon class names
    featured = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Skill {self.name}>'

    @property
    def proficiency_level(self):
        """Return proficiency as a descriptive level."""
        if self.proficiency >= 90:
            return "Expert"
        elif self.proficiency >= 75:
            return "Advanced"
        elif self.proficiency >= 60:
            return "Intermediate"
        elif self.proficiency >= 40:
            return "Beginner"
        else:
            return "Learning"

    def display_info(self):
        """Displays the information about the skill."""
        return f"Skill: {self.name}, Proficiency: {self.proficiency}%, Description: {self.description}"

    @staticmethod
    def create_sample_data():
        """Create sample skills for the portfolio."""
        sample_skills = [
            # Programming Languages
            Skill(name="Python", category="Programming Languages", proficiency=95,
                  description="Advanced Python development for AI/ML, web applications, and data science",
                  icon="fab fa-python", featured=True),
            Skill(name="JavaScript", category="Programming Languages", proficiency=85,
                  description="Modern JavaScript (ES6+) for frontend and backend development",
                  icon="fab fa-js-square", featured=True),
            Skill(name="SQL", category="Programming Languages", proficiency=90,
                  description="Database design, optimization, and complex query writing",
                  icon="fas fa-database", featured=True),

            # AI & Machine Learning
            Skill(name="Large Language Models (LLM)", category="AI & Machine Learning", proficiency=88,
                  description="Working with LLMs, prompt engineering, and AI agent development",
                  icon="fas fa-robot", featured=True),
            Skill(name="Machine Learning", category="AI & Machine Learning", proficiency=90,
                  description="Supervised and unsupervised learning algorithms",
                  icon="fas fa-brain", featured=True),
            Skill(name="Deep Learning", category="AI & Machine Learning", proficiency=85,
                  description="CNN, TensorFlow, PyTorch for computer vision and neural networks",
                  icon="fas fa-network-wired", featured=True),
            Skill(name="Computer Vision", category="AI & Machine Learning", proficiency=82,
                  description="Image processing, object detection, and medical image analysis",
                  icon="fas fa-eye"),
            Skill(name="AI Agents", category="AI & Machine Learning", proficiency=80,
                  description="Developing intelligent agents and automation systems",
                  icon="fas fa-robot"),

            # OCR & Document Processing
            Skill(name="OCR Technologies", category="AI & Machine Learning", proficiency=85,
                  description="Tesseract, EasyOCR, PaddleOCR for document processing",
                  icon="fas fa-file-text"),

            # Web Frameworks & APIs
            Skill(name="FastAPI", category="Web Frameworks", proficiency=88,
                  description="High-performance API development with FastAPI",
                  icon="fas fa-rocket", featured=True),
            Skill(name="Flask", category="Web Frameworks", proficiency=90,
                  description="Building scalable web applications with Flask",
                  icon="fas fa-flask"),
            Skill(name="Django", category="Web Frameworks", proficiency=82,
                  description="Full-stack web development with Django framework",
                  icon="fas fa-server"),
            Skill(name="Vue.js", category="Web Frameworks", proficiency=80,
                  description="Modern frontend development with Vue.js",
                  icon="fab fa-vuejs"),

            # Data Science & Analysis
            Skill(name="Data Analysis", category="Data Science", proficiency=92,
                  description="Statistical analysis and data visualization",
                  icon="fas fa-chart-line", featured=True),
            Skill(name="Pandas", category="Data Science", proficiency=90,
                  description="Data manipulation and analysis with Pandas",
                  icon="fas fa-table"),
            Skill(name="NumPy", category="Data Science", proficiency=88,
                  description="Numerical computing with NumPy",
                  icon="fas fa-calculator"),
            Skill(name="Scikit-learn", category="Data Science", proficiency=90,
                  description="Machine learning library for Python",
                  icon="fas fa-cogs"),
            Skill(name="Streamlit", category="Data Science", proficiency=85,
                  description="Building interactive data applications with Streamlit",
                  icon="fas fa-stream"),
            Skill(name="Librosa", category="Data Science", proficiency=78,
                  description="Audio analysis and feature extraction",
                  icon="fas fa-music"),

            # Deep Learning Frameworks
            Skill(name="TensorFlow", category="Deep Learning", proficiency=85,
                  description="Deep learning and neural network development",
                  icon="fas fa-brain"),
            Skill(name="PyTorch", category="Deep Learning", proficiency=80,
                  description="Research-oriented deep learning framework",
                  icon="fas fa-fire"),
            Skill(name="CNN", category="Deep Learning", proficiency=82,
                  description="Convolutional Neural Networks for image processing",
                  icon="fas fa-network-wired"),

            # Tools & Technologies
            Skill(name="Git", category="Tools", proficiency=88,
                  description="Version control and collaborative development",
                  icon="fab fa-git-alt"),
            Skill(name="Docker", category="Tools", proficiency=75,
                  description="Containerization and deployment",
                  icon="fab fa-docker"),
            Skill(name="Linux", category="Tools", proficiency=78,
                  description="Linux system administration and command line",
                  icon="fab fa-linux"),

            # Databases
            Skill(name="PostgreSQL", category="Databases", proficiency=82,
                  description="Advanced PostgreSQL database management",
                  icon="fas fa-database"),
            Skill(name="SQLite", category="Databases", proficiency=88,
                  description="Lightweight database for development and testing",
                  icon="fas fa-database"),
        ]

        for skill in sample_skills:
            existing = Skill.query.filter_by(name=skill.name).first()
            if not existing:
                db.session.add(skill)

        db.session.commit()
