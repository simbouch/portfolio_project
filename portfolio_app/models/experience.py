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
            # Current Position
            Experience(
                title="AI Developer (Alternance/Apprentissage)",
                company="CHRU de Nancy & Simplon Microsoft AI School",
                location="Nancy, France",
                start_date=date(2024, 9, 1),
                end_date=None,  # Current position
                description="Work-study program combining intensive AI training with practical application at CHRU de Nancy. Developing healthcare AI solutions with focus on automated robotics, OCR tools, and LLM/NLP applications. Emphasizing ethics and human impact in AI development for healthcare environments.",
                technologies="Python, TensorFlow, PyTorch, FastAPI, LLM/NLP, OCR (Tesseract, EasyOCR), AI Agents, Azure ML, Docker, MLflow, Automated Robotics, Django, Streamlit",
                achievements="• Developing automated robotics systems for CHRU de Nancy\n• Building advanced OCR tools for medical document processing\n• Implementing LLM/NLP solutions for healthcare applications\n• Created malaria detection system using CNN and Django\n• Developed TRAQ diagnostic tool for behavioral disorders\n• Built educational AI tools with LangChain and local LLMs\n• Focusing on AI ethics and human-centered design"
            ),

            # Recent Experience
            Experience(
                title="Data Scientist/Analyst",
                company="CLINICOG",
                location="Nancy, France",
                start_date=date(2024, 4, 1),
                end_date=date(2024, 7, 31),
                description="Designed and deployed machine learning models and neural networks using Python for healthcare data analysis. Created Streamlit applications to assist clinical psychologists with diagnostic tools, focusing on high-performance and intuitive user interfaces.",
                technologies="Python, Machine Learning, Neural Networks, Streamlit, Healthcare Data Analytics, Clinical Psychology Tools",
                achievements="• Developed clinical diagnostic tools for psychologists\n• Improved workflow efficiency for healthcare professionals\n• Deployed production-ready ML applications\n• Created intuitive user interfaces for complex data analysis"
            ),

            Experience(
                title="Data Scientist",
                company="DBCALL | Réseau DEF",
                location="Roubaix, France",
                start_date=date(2023, 11, 1),
                end_date=date(2023, 12, 31),
                description="Developed machine learning models in Python, created APIs for data integration, utilized PL/SQL for database operations, and integrated Microsoft ecosystem tools for business intelligence and data management.",
                technologies="Python, Machine Learning, API Development, PL/SQL, Power BI, Microsoft Dataverse, Azure, Business Intelligence",
                achievements="• Built scalable ML models for business intelligence\n• Created robust data integration APIs\n• Implemented comprehensive BI solutions\n• Integrated Microsoft ecosystem tools for data management"
            ),

            Experience(
                title="Application Developer/Designer",
                company="RegiePub",
                location="Nancy, France",
                start_date=date(2023, 6, 1),
                end_date=date(2023, 8, 31),
                description="Designed, developed, and deployed a complete web application using modern PHP frameworks. Implemented full-stack solution with Symfony backend and responsive frontend integration.",
                technologies="PHP, Symfony Framework, Full-Stack Development, Web Application Design, Responsive Design",
                achievements="• Delivered complete web application from concept to deployment\n• Implemented modern PHP architecture with Symfony\n• Created responsive user interfaces\n• Established best practices for full-stack development"
            ),

            # Long-term Previous Experience
            Experience(
                title="Director of Scientific and Technical Police Laboratory",
                company="National Police Laboratory",
                location="France",
                start_date=date(2006, 1, 1),
                end_date=date(2021, 12, 31),
                description="Led scientific and technical operations for forensic investigations, managed laboratory operations, and supervised analytical processes for criminal investigations. Applied advanced analytical techniques and maintained quality standards for forensic evidence processing.",
                technologies="Forensic Analysis, Laboratory Management, Scientific Investigation, Quality Control, Analytical Chemistry",
                achievements="• Managed forensic laboratory operations for 15+ years\n• Supervised complex criminal investigations\n• Maintained high-quality standards for evidence processing\n• Led team of forensic scientists and technicians"
            )
        ]

        for experience in sample_experiences:
            existing = Experience.query.filter_by(title=experience.title, company=experience.company).first()
            if not existing:
                db.session.add(experience)

        db.session.commit()
