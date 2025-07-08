# portfolio_project/app/models/experience.py

from datetime import datetime, timezone
from .. import db


class Experience(db.Model):
    __tablename__ = "experiences"

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
        return f"<Experience {self.title} at {self.company}>"

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
                title="AI Developer/Engineer",
                company="CHRU de Nancy",
                location="Nancy, Grand Est, France",
                start_date=date(2025, 2, 1),
                end_date=None,  # Current position
                description="Designing and developing AI solutions to address real-world healthcare challenges, with a strong emphasis on ethics and human-centered design. Focus on intelligent automation, document processing, and clinical data workflows using advanced technologies such as computer vision, OCR, NLP, and Large Language Models (LLMs). Projects include building AI-powered robotics systems, medical document digitization tools, and custom NLP pipelines for healthcare-specific use cases.",
                technologies="Python, TensorFlow, PyTorch, Computer Vision, OCR (Tesseract, EasyOCR, PaddleOCR), NLP, LLMs, AI Robotics, FastAPI, Docker, Azure ML, Streamlit, Django",
                achievements="• Developing AI-powered robotics systems for healthcare automation\n• Building medical document digitization and processing tools\n• Implementing custom NLP pipelines for healthcare applications\n• Creating computer vision solutions for medical imaging\n• Focusing on AI ethics and human-centered design principles\n• Delivering production-ready AI solutions for clinical environments",
            ),
            # AI Development Training
            Experience(
                title="AI Developer - Professional Training",
                company="Microsoft AI School by Simplon – IRIS CHRU",
                location="Nancy, France",
                start_date=date(2024, 9, 1),
                end_date=date(2024, 12, 31),
                description="Specialized professional training in AI development, data science, machine learning, deep learning, and Microsoft cloud computing with a focus on AI application development. Intensive program covering modern AI technologies and practical implementation.",
                technologies="Python, TensorFlow, PyTorch, Azure ML, Microsoft Cloud, Deep Learning, Machine Learning, AI Application Development",
                achievements="• Completed intensive AI development certification program\n• Mastered Microsoft cloud computing and Azure ML\n• Developed expertise in deep learning and neural networks\n• Built practical AI applications and solutions\n• Specialized in healthcare AI applications",
            ),
            # Recent Experience
            Experience(
                title="Data Scientist/Analyst",
                company="CLINICOG",
                location="Nancy, France",
                start_date=date(2024, 4, 1),
                end_date=date(2024, 7, 31),
                description="Designed and deployed machine learning models and neural networks in Python using healthcare data. Developed Streamlit applications to assist psychologists in diagnostics, creating intuitive and high-performance tools.",
                technologies="Python, Machine Learning, Neural Networks, Streamlit, Healthcare Data Analytics, Clinical Psychology Tools",
                achievements="• Developed clinical diagnostic tools for psychologists\n• Improved workflow efficiency for healthcare professionals\n• Deployed production-ready ML applications\n• Created intuitive user interfaces for complex data analysis",
            ),
            Experience(
                title="Data Scientist",
                company="DBCALL | Réseau DEF",
                location="Roubaix, France",
                start_date=date(2023, 11, 1),
                end_date=date(2023, 12, 31),
                description="Developed machine learning models in Python, built APIs, and integrated PL/SQL solutions. Implemented Microsoft tools (Power BI, Dataverse, Azure) for data analytics and business intelligence solutions.",
                technologies="Python, Machine Learning, API Development, PL/SQL, Power BI, Microsoft Dataverse, Azure, Business Intelligence",
                achievements="• Built scalable ML models for business intelligence\n• Created robust data integration APIs\n• Implemented comprehensive BI solutions\n• Integrated Microsoft ecosystem tools for data management",
            ),
            Experience(
                title="Application Developer",
                company="RegiePub",
                location="Nancy, France",
                start_date=date(2023, 6, 1),
                end_date=date(2023, 8, 31),
                description="Designed, developed, and deployed a full-stack web application using PHP and Symfony. Implemented complete solution from backend architecture to responsive frontend design.",
                technologies="PHP, Symfony Framework, Full-Stack Development, Web Application Design, Responsive Design",
                achievements="• Delivered complete web application from concept to deployment\n• Implemented modern PHP architecture with Symfony\n• Created responsive user interfaces\n• Established best practices for full-stack development",
            ),
            # Long-term Previous Experience
            Experience(
                title="Forensic Science & Technical Laboratory Director",
                company="Gendarmerie",
                location="Morocco",
                start_date=date(2006, 1, 1),
                end_date=date(2021, 12, 31),
                description="Led teams in forensic investigations, prepared scientific evidence reports (genetic, fingerprint, ballistic, toxicology, document fraud, digital forensics), and reconstructed crime scenes. Managed comprehensive forensic laboratory operations and supervised analytical processes for criminal investigations.",
                technologies="Forensic Analysis, Laboratory Management, Scientific Investigation, Quality Control, Analytical Chemistry, Digital Forensics, Genetic Analysis, Ballistics, Toxicology",
                achievements="• Managed forensic laboratory operations for 15+ years\n• Led teams in complex criminal investigations\n• Prepared scientific evidence reports across multiple forensic disciplines\n• Reconstructed crime scenes and analyzed evidence\n• Maintained high-quality standards for forensic evidence processing\n• Supervised genetic, fingerprint, ballistic, and toxicology analyses\n• Managed digital forensics and document fraud investigations",
            ),
        ]

        for experience in sample_experiences:
            existing = Experience.query.filter_by(
                title=experience.title, company=experience.company
            ).first()
            if not existing:
                db.session.add(experience)

        db.session.commit()
