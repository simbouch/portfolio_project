# portfolio_project/app/controllers/portfolio_controller.py
from flask import Blueprint, render_template
from app.models.project import WebProject, DataScienceProject
from app.models.skill import Skill
from app.models.experience import Experience
from datetime import datetime

bp = Blueprint("portfolio", __name__)


@bp.route("/")
def index():
    current_year = datetime.now().year
    return render_template("portfolio/index.html", current_year=current_year)


@bp.route("/projects")
def projects():
    # Sample projects
    projects = [
        WebProject(
            title="Portfolio Website",
            description="A personal portfolio website showcasing projects.",
            technology_used=["HTML", "CSS", "JavaScript", "Flask"],
            duration="2 months",
            frontend="HTML, CSS, JavaScript",
            backend="Flask",
        ),
        DataScienceProject(
            title="Health Prediction Model",
            description="A machine learning model predicting health outcomes.",
            technology_used=["Python", "TensorFlow", "Scikit-Learn"],
            duration="3 months",
            algorithms=["Random Forest", "Neural Network"],
        ),
    ]
    return render_template("portfolio/projects.html", projects=projects)


@bp.route("/skills")
def skills():
    # Sample skills
    skills = [
        Skill(
            name="Python",
            proficiency="Advanced",
            description="Experienced in Python for data analysis and web development.",
        ),
        Skill(
            name="Machine Learning",
            proficiency="Advanced",
            description="Skilled in scikit-learn, TensorFlow, and Keras.",
        ),
        Skill(
            name="SQL",
            proficiency="Intermediate",
            description="Proficient in SQL for database querying and management.",
        ),
    ]
    return render_template("portfolio/skills.html", skills=skills)


@bp.route("/experience")
def experience():
    # Sample experiences
    experiences = [
        Experience(
            title="Data Scientist",
            company="Clinicog",
            duration="April 2024 - July 2024",
            description="Developed and deployed machine learning models for health data analysis.",
        ),
        Experience(
            title="Data Scientist",
            company="DBCALL | Réseau DEF-Roubaix",
            duration="November 2023 - December 2023",
            description="Created APIs and integrated Microsoft tools for data visualization and analysis.",
        ),
        Experience(
            title="Application Developer",
            company="RegiePub - Nancy",
            duration="June 2023 - August 2023",
            description="Developed a full-stack web application using PHP and Symfony.",
        ),
    ]
    return render_template("portfolio/experience.html", experiences=experiences)
