# portfolio_project/app/models/project.py

from datetime import datetime, timezone

from .. import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technology_used = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    project_type = db.Column(db.String(50), nullable=False, default="general")
    github_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    featured = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Project {self.title}>"

    def display_info(self):
        """Displays the basic info of a project."""
        return (
            f"Project: {self.title}, Technologies: {self.technology_used}, "
            f"Duration: {self.duration}"
        )

    @property
    def owner_avatar_url(self):
        """Returns the project owner's avatar URL."""
        return "https://avatars.githubusercontent.com/u/183075384?v=4"

    @staticmethod
    def create_sample_data():
        """Create sample projects for the portfolio."""
        sample_projects = [
            Project(
                title="IA Continu Solution - Enterprise ML Template",
                description=(
                    "Production-ready ML template with complete automation, advanced "
                    "monitoring, and Discord integration. Features microservices "
                    "architecture, 30-second automated ML pipeline with drift detection, "
                    "MLflow tracking, and comprehensive health monitoring across 5 "
                    "independent services."
                ),
                technology_used=(
                    "Docker, FastAPI, MLflow, Prefect, Streamlit, Discord API, "
                    "JWT Auth, Prometheus, Grafana"
                ),
                duration="8 weeks",
                project_type="enterprise",
                github_url="https://github.com/simbouch/ia_continu_solution",
                featured=True,
            ),
            Project(
                title="Flashcards Full-Stack Platform with OCR",
                description=(
                    "Full-stack platform for automatic flashcard generation from "
                    "PDFs/images. OCR with Tesseract, Q&A via locally fine-tuned "
                    "French LLM, SQLite storage, FastAPI REST with auth, Vue.js "
                    "review UI, Dockerized services, CI/CD pipelines, monitoring "
                    "& GDPR compliance."
                ),
                technology_used=(
                    "FastAPI, Vue.js, OCR, French LLM, Python, JavaScript, "
                    "SQLite, Docker, CI/CD"
                ),
                duration="6 weeks",
                project_type="web",
                github_url="https://github.com/simbouch/flashcards-projet",
                featured=True,
            ),
            Project(
                title="RPA POC System for PDF Information Extraction",
                description=(
                    "Professional AI-powered system for automated PDF information "
                    "extraction. Supports 4 specialized models and offers a modern "
                    "interface with Streamlit. Intelligent RPA system using AI for "
                    "document processing and data extraction workflows."
                ),
                technology_used=(
                    "Python, OCR (Tesseract, EasyOCR, PaddleOCR), AI Agents, "
                    "Streamlit, TensorFlow"
                ),
                duration="4 weeks",
                project_type="ai_automation",
                github_url="https://github.com/simbouch/rpa_1_poc",
                featured=True,
            ),
            Project(
                title="ML Optimization Framework with Optuna",
                description=(
                    "Educational project demonstrating Optuna's hyperparameter "
                    "optimization capabilities through interactive examples and "
                    "comprehensive tutorials. Features 6 different optimization "
                    "studies, interactive dashboard, TPE sampling, pruning "
                    "techniques, and multi-objective optimization with real ML models."
                ),
                technology_used=(
                    "Python, Optuna, Docker, Scikit-learn, SQLite, Interactive "
                    "Dashboard, TPE Sampling, Pruning"
                ),
                duration="4 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/ml-optimization-framework",
                featured=True,
            ),
            Project(
                title="LangChain Learning App 2025",
                description=(
                    "Educational tool powered by LangChain and Streamlit that "
                    "transforms course notes into interactive flashcards using "
                    "local language model (Ollama + Phi) with no external API "
                    "dependencies. Features built-in OCR, user-friendly interface, "
                    "and fully offline operation."
                ),
                technology_used=(
                    "LangChain, Streamlit, Ollama, Phi, NLP, Educational AI, "
                    "Local LLM, OCR"
                ),
                duration="5 weeks",
                project_type="ai_education",
                github_url="https://github.com/simbouch/langchain_learning_app_2025",
                featured=True,
            ),
            Project(
                title="Malaria Detection Application",
                description=(
                    "Deep learning application using CNN for malaria detection from "
                    "blood cell images. Provides an intuitive interface to upload "
                    "images and receive predictions, making it accessible for medical "
                    "practitioners and researchers."
                ),
                technology_used=(
                    "Python, TensorFlow, CNN, Computer Vision, Streamlit, "
                    "Deep Learning"
                ),
                duration="4 weeks",
                project_type="deep_learning",
                github_url="https://github.com/simbouch/malaria_detection",
                featured=True,
            ),
            Project(
                title="Malaria Detection Django App",
                description=(
                    "Django web application for malaria detection from medical "
                    "images using a pre-trained CNN model for real-time "
                    "classification. Leverages a pre-trained Convolutional Neural "
                    "Network (CNN) model for real-time predictions."
                ),
                technology_used=(
                    "Django, JavaScript, CNN, Computer Vision, Medical AI, "
                    "TensorFlow"
                ),
                duration="4 weeks",
                project_type="deep_learning",
                github_url="https://github.com/simbouch/malaria_project_django",
                featured=True,
            ),
            Project(
                title="Clustering Flask Web Application",
                description=(
                    "Flask-based web application for clustering datasets with PCA "
                    "and K-Means. Features dynamic file uploads, visualizations, "
                    "and synthetic data generation for testing. Perfect for "
                    "exploring clustering techniques interactively!"
                ),
                technology_used=(
                    "Flask, Scikit-learn, PCA, K-Means, Plotly, Pandas, Bootstrap"
                ),
                duration="3 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/clustering",
            ),
            Project(
                title="NutriScore Prediction App",
                description=(
                    "NutriScore Wizard is a web application that predicts the "
                    "NutriScore grade for food products based on their nutritional "
                    "information. The app provides an intuitive interface for "
                    "users to input product details."
                ),
                technology_used=(
                    "Python, Flask, Scikit-learn, Pandas, Bootstrap, "
                    "Machine Learning"
                ),
                duration="3 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/nutriscore_prediction_app",
            ),
            Project(
                title="Audio Analysis Toolkit",
                description=(
                    "Comprehensive audio analysis toolkit built with Python, "
                    "featuring waveform visualization, spectral analysis, STFT, "
                    "MFCC extraction, and sound classification using Librosa "
                    "and Streamlit."
                ),
                technology_used=(
                    "Python, Librosa, Streamlit, NumPy, Matplotlib, Scikit-learn"
                ),
                duration="3 weeks",
                project_type="data_science",
                github_url="https://github.com/simbouch/audio-analysis-toolkit",
                featured=True,
            ),
            Project(
                title="Boston Housing ML Comparison",
                description=(
                    "Machine learning project comparing linear regression and "
                    "neural networks for Boston housing price prediction. Includes "
                    "feature engineering, model evaluation, and performance "
                    "comparison analysis."
                ),
                technology_used=(
                    "Python, Scikit-learn, Pandas, Matplotlib, Seaborn, Jupyter"
                ),
                duration="2 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/boston-housing-ml-comparison",
            ),
            Project(
                title="TRAQ Diagnostic Tool",
                description=(
                    "Streamlit-based tool designed to assist in the diagnosis of "
                    "behavioral and attention-related disorders using the TRAQ "
                    "questionnaire. Computes key scores, visualizes results, and "
                    "generates detailed reports for download."
                ),
                technology_used=(
                    "Python, Streamlit, Healthcare Analytics, Data Analysis"
                ),
                duration="3 weeks",
                project_type="healthcare",
                github_url="https://github.com/simbouch/traq_diagnostic",
                featured=True,
            ),
            Project(
                title="KinePasLoin - Movie Ticket Booking",
                description=(
                    "Personal project for a simple movie ticket booking application. "
                    "The app integrates with the OMDB API to fetch and display movie "
                    "details, allows users to calculate ticket costs, and manages a "
                    "shopping cart using local storage."
                ),
                technology_used="HTML, JavaScript, API Integration, OMDB API",
                duration="2 weeks",
                project_type="web",
                github_url="https://github.com/simbouch/kinepasloin",
            ),
            Project(
                title="Reverso - Business Management System",
                description=(
                    "Java-based solution designed for managing clients, contracts, "
                    "and related business entities within a database. Built on "
                    "robust object-oriented principles, it provides functionalities "
                    "such as database connectivity, CRUD operations, and structured "
                    "exception handling."
                ),
                technology_used="Java, Database Management, OOP, SQL",
                duration="4 weeks",
                project_type="enterprise",
                github_url="https://github.com/simbouch/reverso",
            ),
            Project(
                title="OCR Projects Collection",
                description=(
                    "Collection of OCR projects including PaddleOCR, EasyOCR, and "
                    "Tesseract implementations. Lightweight web interfaces for fast, "
                    "accurate text extraction from French receipts and documents "
                    "with GPU-friendly processing."
                ),
                technology_used=(
                    "Python, PaddleOCR, EasyOCR, Tesseract, Streamlit, OCR"
                ),
                duration="6 weeks",
                project_type="ai_automation",
                github_url="https://github.com/simbouch/paddle_streamlit_ocr",
            ),
            Project(
                title="Web Scraping with Scrapy",
                description=(
                    "Scrapy project to scrape book data from Books to Scrape and "
                    "saves the extracted information in a CSV file. Demonstrates "
                    "web scraping techniques and data extraction workflows."
                ),
                technology_used=(
                    "Python, Scrapy, BeautifulSoup, Data Extraction, CSV"
                ),
                duration="2 weeks",
                project_type="data_science",
                github_url="https://github.com/simbouch/my_scrapy_project",
            ),
            Project(
                title="Credit Risk Classification",
                description=(
                    "Machine learning project aimed at building a classification "
                    "model to predict the eligibility of clients for credit at a "
                    "bank. Leverages Python-based tools and techniques to evaluate "
                    "and optimize credit risk assessment."
                ),
                technology_used=(
                    "Python, Scikit-learn, Classification, Risk Assessment, Banking"
                ),
                duration="3 weeks",
                project_type="machine_learning",
                github_url="https://github.com/simbouch/classification",
            ),
        ]

        for project in sample_projects:
            existing = Project.query.filter_by(title=project.title).first()
            if not existing:
                db.session.add(project)

        db.session.commit()
