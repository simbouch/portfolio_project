# portfolio_project/app/models/project.py

from datetime import datetime, timezone
from .. import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technology_used = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    project_type = db.Column(db.String(50), nullable=False, default='general')
    github_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    featured = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Project {self.title}>'

    def display_info(self):
        """Displays the basic info of a project."""
        return f"Project: {self.title}, Technologies: {self.technology_used}, Duration: {self.duration}"

    @staticmethod
    def create_sample_data():
        """Create sample projects for the portfolio."""
        sample_projects = [
            Project(
                title="RPA POC System for PDF Information Extraction",
                description="Intelligent RPA system using AI for automated PDF information extraction. Implements OCR technologies and machine learning for document processing and data extraction workflows.",
                technology_used="Python, OCR (Tesseract, EasyOCR, PaddleOCR), AI Agents, FastAPI, TensorFlow",
                duration="4 weeks",
                project_type="ai_automation",
                github_url="https://github.com/simbouch/rpa-pdf-extraction",
                featured=True
            ),
            Project(
                title="Flashcards Full-Stack Platform with OCR",
                description="Complete learning platform with OCR capabilities for automatic flashcard creation. Features French LLM integration, FastAPI backend, and Vue.js frontend for interactive learning experience.",
                technology_used="FastAPI, Vue.js, OCR, French LLM, Python, JavaScript, PostgreSQL",
                duration="6 weeks",
                project_type="web",
                github_url="https://github.com/simbouch/flashcards-platform",
                featured=True
            ),
            Project(
                title="Audio Analysis Toolkit",
                description="Comprehensive audio analysis application using Librosa for feature extraction and Streamlit for interactive visualization. Includes spectral analysis, tempo detection, and audio classification.",
                technology_used="Python, Librosa, Streamlit, NumPy, Matplotlib, Scikit-learn",
                duration="3 weeks",
                project_type="data_science",
                github_url="https://github.com/simbouch/audio-analysis-toolkit",
                featured=True
            ),
            Project(
                title="Boston Housing ML Comparison",
                description="Comprehensive machine learning project comparing multiple algorithms for Boston housing price prediction. Includes feature engineering, model evaluation, and performance comparison analysis.",
                technology_used="Python, Scikit-learn, Pandas, Matplotlib, Seaborn, Jupyter",
                duration="2 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/boston-housing-ml"
            ),
            Project(
                title="Malaria Detection Application",
                description="Deep learning application using CNN for malaria detection from blood cell images. Built with Django framework and TensorFlow for medical image classification.",
                technology_used="Django, TensorFlow, CNN, Computer Vision, Python, HTML/CSS",
                duration="4 weeks",
                project_type="deep_learning",
                github_url="https://github.com/simbouch/malaria-detection",
                featured=True
            ),
            Project(
                title="Clustering Flask Web Application",
                description="Interactive web application implementing PCA and K-Means clustering algorithms. Features data visualization, dimensionality reduction, and cluster analysis with Flask backend.",
                technology_used="Flask, Scikit-learn, PCA, K-Means, Plotly, Pandas, Bootstrap",
                duration="3 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/clustering-webapp"
            ),
            Project(
                title="NutriScore Prediction App",
                description="Machine learning web application for predicting NutriScore grades based on nutritional values. Features real-time predictions, data visualization, and nutritional analysis.",
                technology_used="Python, Flask, Scikit-learn, Pandas, Bootstrap, Machine Learning",
                duration="3 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/nutriscore_prediction_app",
                demo_url="https://nutriscore-prediction.herokuapp.com"
            )
        ]

        for project in sample_projects:
            existing = Project.query.filter_by(title=project.title).first()
            if not existing:
                db.session.add(project)

        db.session.commit()
