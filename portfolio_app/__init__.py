
# portfolio_project/app/__init__.py

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime

db = SQLAlchemy()
mail = Mail()

def format_date(value, format="%Y"):
    """Custom date filter for Jinja2 templates."""
    if isinstance(value, str):
        return value
    return value.strftime(format)

def create_app(config_class="config.DevelopmentConfig"):
    # Configure Flask to use templates and static files from the portfolio_app directory
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')
    app.config.from_object(config_class)

    # Initialize plugins
    db.init_app(app)
    mail.init_app(app)

    # Register the custom filter
    app.jinja_env.filters['date'] = format_date

    # Import models to ensure they are registered with SQLAlchemy
    from .models import project, experience, skill

    # Create database tables and sample data
    with app.app_context():
        db.create_all()

        # Create sample data if tables are empty
        from .models.project import Project
        from .models.experience import Experience
        from .models.skill import Skill

        if Project.query.count() == 0:
            Project.create_sample_data()
        if Experience.query.count() == 0:
            Experience.create_sample_data()
        if Skill.query.count() == 0:
            Skill.create_sample_data()

    # Register main routes
    @app.route("/")
    def index():
        from .models.project import Project
        from .models.experience import Experience
        from .models.skill import Skill

        # Get featured projects (limit to 3)
        featured_projects = Project.query.filter_by(featured=True).limit(3).all()
        recent_experiences = Experience.query.order_by(Experience.start_date.desc()).limit(2).all()
        top_skills = Skill.query.filter_by(featured=True).limit(6).all()

        return render_template("index.html",
                             featured_projects=featured_projects,
                             recent_experiences=recent_experiences,
                             top_skills=top_skills)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/experience")
    def experience():
        from .models.experience import Experience
        experiences = Experience.query.order_by(Experience.start_date.desc()).all()
        return render_template("experience.html", experiences=experiences)

    @app.route("/projects")
    def projects():
        from .models.project import Project
        all_projects = Project.query.order_by(Project.created_date.desc()).all()
        return render_template("projects.html", projects=all_projects)

    @app.route("/skills")
    def skills():
        from .models.skill import Skill
        all_skills = Skill.query.order_by(Skill.category, Skill.name).all()

        # Group skills by category
        skills_by_category = {}
        for skill in all_skills:
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill)

        return render_template("skills.html", skills_by_category=skills_by_category)

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")
            message = request.form.get("message")

            # Validate form data
            if not name or not email or not message:
                flash("Please fill in all fields.", "danger")
                return redirect(url_for("contact"))

            # Try to send email if configured
            try:
                if app.config.get('MAIL_SERVER'):
                    msg = Message("New Contact Form Submission",
                                  sender=app.config.get('MAIL_USERNAME', email),
                                  recipients=[app.config.get('CONTACT_EMAIL', 'khribech.chouaib@gmail.com')])
                    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                    mail.send(msg)
                    flash("Your message has been sent successfully!", "success")
                else:
                    # Log the message for now (in production, you might want to save to database)
                    app.logger.info(f"Contact form submission - Name: {name}, Email: {email}, Message: {message}")
                    flash("Your message has been received! I'll get back to you soon.", "success")
            except Exception as e:
                app.logger.error(f"Error sending email: {e}")
                flash("Thank you for your message! I'll get back to you soon.", "success")

            return redirect(url_for("contact"))

        return render_template("contact.html")

    @app.route("/interests")
    def interests():
        return render_template("interests.html")

    # Register blueprints if they exist
    try:
        from .controllers import portfolio_controller
        app.register_blueprint(portfolio_controller.bp)
    except ImportError:
        pass  # Controllers are optional

    return app
