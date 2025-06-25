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
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class)

    # Initialize plugins
    db.init_app(app)
    mail.init_app(app)

    # Log email configuration status
    if app.config.get("MAIL_CONFIGURED", False):
        app.logger.info(
            f"✅ Email configured: {app.config.get('MAIL_USERNAME')} -> {app.config.get('CONTACT_EMAIL')}"
        )
    else:
        app.logger.warning("⚠️ Email not configured - messages will be logged only")

    # Register the custom filter
    app.jinja_env.filters["date"] = format_date

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
        recent_experiences = (
            Experience.query.order_by(Experience.start_date.desc()).limit(2).all()
        )
        top_skills = Skill.query.filter_by(featured=True).limit(6).all()

        return render_template(
            "index.html",
            featured_projects=featured_projects,
            recent_experiences=recent_experiences,
            top_skills=top_skills,
        )

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
            subject = request.form.get("subject", "General Inquiry")
            message = request.form.get("message")

            # Validate form data
            if not name or not email or not message:
                flash("Please fill in all required fields.", "danger")
                return redirect(url_for("contact"))

            # Validate email format
            import re

            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(email_pattern, email):
                flash("Please enter a valid email address.", "danger")
                return redirect(url_for("contact"))

            # CRITICAL: Always log the message first to ensure no data loss
            import datetime

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Log message to application logs (this ensures no message is ever lost)
            contact_log = f"""
=== PORTFOLIO CONTACT FORM SUBMISSION ===
Timestamp: {timestamp}
Name: {name}
Email: {email}
Subject: {subject if subject else 'General Inquiry'}
Message: {message}
IP Address: {request.environ.get('REMOTE_ADDR', 'Unknown')}
User Agent: {request.environ.get('HTTP_USER_AGENT', 'Unknown')}
==========================================
"""
            app.logger.info(contact_log)

            # Try to send email if configured
            email_sent = False
            try:
                if app.config.get("MAIL_CONFIGURED", False):
                    # Create email subject with proper formatting
                    email_subject = (
                        f"Portfolio Contact: {subject}"
                        if subject
                        else "Portfolio Contact: General Inquiry"
                    )

                    msg = Message(
                        subject=email_subject,
                        sender=app.config.get("MAIL_USERNAME"),
                        recipients=[
                            app.config.get(
                                "CONTACT_EMAIL", "khribech.chouaib@gmail.com"
                            )
                        ],
                        reply_to=email,
                    )

                    # Create formatted email body
                    msg.body = f"""New contact form submission from your portfolio website:

Timestamp: {timestamp}
Name: {name}
Email: {email}
Subject: {subject if subject else 'General Inquiry'}

Message:
{message}

---
This message was sent from your portfolio contact form.
Reply directly to this email to respond to {name}.

Technical Details:
IP: {request.environ.get('REMOTE_ADDR', 'Unknown')}
User Agent: {request.environ.get('HTTP_USER_AGENT', 'Unknown')}"""

                    msg.html = f"""
                    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                        <h2 style="color: #3498db;">New Portfolio Contact</h2>
                        <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                            <p><strong>Timestamp:</strong> {timestamp}</p>
                            <p><strong>Name:</strong> {name}</p>
                            <p><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
                            <p><strong>Subject:</strong> {subject if subject else 'General Inquiry'}</p>
                        </div>
                        <div style="background: white; padding: 20px; border-left: 4px solid #3498db;">
                            <h3>Message:</h3>
                            <p style="line-height: 1.6;">{message.replace(chr(10), '<br>')}</p>
                        </div>
                        <hr style="margin: 30px 0;">
                        <p style="color: #666; font-size: 14px;">
                            This message was sent from your portfolio contact form.<br>
                            Reply directly to this email to respond to {name}.
                        </p>
                        <div style="background: #f8f9fa; padding: 10px; margin-top: 20px; font-size: 12px; color: #666;">
                            <strong>Technical Details:</strong><br>
                            IP: {request.environ.get('REMOTE_ADDR', 'Unknown')}<br>
                            User Agent: {request.environ.get('HTTP_USER_AGENT', 'Unknown')}
                        </div>
                    </div>
                    """

                    mail.send(msg)
                    email_sent = True
                    app.logger.info(
                        f"✅ Email sent successfully to {app.config.get('CONTACT_EMAIL')} from {email}"
                    )
                    flash(
                        "Your message has been sent successfully! I'll get back to you soon.",
                        "success",
                    )

            except Exception as e:
                app.logger.error(f"❌ Error sending email: {str(e)}")
                email_sent = False

            # If email failed or not configured, still confirm receipt to user
            if not email_sent:
                app.logger.warning(f"⚠️ Email not sent, but message logged for: {email}")
                flash(
                    "Your message has been received! I'll get back to you soon.", "info"
                )

            return redirect(url_for("contact"))

        return render_template("contact.html")

    @app.route("/interests")
    def interests():
        return render_template("interests.html")

    @app.route("/gallery")
    def gallery():
        return render_template("gallery.html")

    # Register blueprints if they exist
    try:
        from .controllers import portfolio_controller

        app.register_blueprint(portfolio_controller.bp)
    except ImportError:
        pass  # Controllers are optional

    return app
