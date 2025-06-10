# portfolio_project/app/models/experience.py

from datetime import datetime, timezone
from .. import db

class Experience(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)  # Null if current position
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200))
    achievements = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Experience {self.title} at {self.company}>'

    @property
    def duration(self):
        """Calculate duration of experience."""
        end = self.end_date or datetime.now().date()
        start = self.start_date

        years = end.year - start.year
        months = end.month - start.month

        if months < 0:
            years -= 1
            months += 12

        if years > 0 and months > 0:
            return f"{years} year{'s' if years > 1 else ''}, {months} month{'s' if months > 1 else ''}"
        elif years > 0:
            return f"{years} year{'s' if years > 1 else ''}"
        elif months > 0:
            return f"{months} month{'s' if months > 1 else ''}"
        else:
            return "Less than a month"

    @property
    def is_current(self):
        """Check if this is a current position."""
        return self.end_date is None

    def display_info(self):
        """Displays information about the experience."""
        return f"Experience: {self.title} at {self.company}, Duration: {self.duration}, Description: {self.description}"

    @staticmethod
    def create_sample_data():
        """Create sample experiences for the portfolio."""
        from datetime import date

        sample_experiences = [
            Experience(
                title="AI Developer - TT2S Program (Alternance/Apprentissage)",
                company="CHRU Nancy & Simplon Microsoft AI School",
                location="Nancy, France",
                start_date=date(2024, 9, 1),
                end_date=None,  # Current position
                description="Comprehensive TT2S (Titre Technique de Niveau 2 Supérieur) program combining 3-month intensive AI training with 16-month work-study at CHRU Nancy. Developing healthcare AI solutions with focus on automated robotics, OCR tools, and LLM/NLP applications. Emphasizing ethics and human impact in AI development for healthcare environments.",
                technologies="Python, TensorFlow, PyTorch, FastAPI, LLM/NLP, OCR (Tesseract, EasyOCR), AI Agents, Azure ML, Docker, MLflow, Automated Robotics",
                achievements="• Developing automated robotics systems for CHRU Nancy\n• Building advanced OCR tools for medical document processing\n• Implementing LLM/NLP solutions for healthcare applications\n• Created RPA POC for PDF information extraction\n• Focusing on AI ethics and human-centered design\n• Deployed ML models with Docker and MLflow in healthcare environment"
            ),
            Experience(
                title="Data Scientist & Analyst",
                company="Freelance Projects",
                location="Nancy, France",
                start_date=date(2023, 1, 1),
                end_date=date(2024, 8, 31),
                description="Developed machine learning models and data analysis solutions for various clients. Specialized in predictive modeling, computer vision, and web application development.",
                technologies="Python, Scikit-learn, Pandas, Django, Flask, Streamlit, Vue.js",
                achievements="• Built NutriScore prediction ML model\n• Created clustering web application with PCA\n• Developed Boston housing price comparison tool\n• Delivered 10+ data science projects"
            ),
            Experience(
                title="Biomedical Engineer & Forensic Scientist",
                company="Various Healthcare & Forensic Institutions",
                location="Morocco & France",
                start_date=date(2008, 1, 1),
                end_date=date(2022, 12, 31),
                description="15+ years of analytical expertise in biomedical engineering and forensic sciences. Specialized in complex problem-solving, data analysis, and scientific research methodologies.",
                technologies="Laboratory Equipment, Statistical Analysis, Research Methodologies, Data Collection",
                achievements="• 15+ years of analytical experience\n• Expert in complex problem-solving\n• Strong foundation in scientific methodology\n• Transitioned expertise to data science"
            )
        ]

        for experience in sample_experiences:
            existing = Experience.query.filter_by(title=experience.title, company=experience.company).first()
            if not existing:
                db.session.add(experience)

        db.session.commit()
