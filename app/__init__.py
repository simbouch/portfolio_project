
# portfolio_project/app/__init__.py

from flask import Flask
from .controllers import portfolio_controller
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def format_date(value, format="%Y"):
    """Custom date filter for Jinja2 templates."""
    return value.strftime(format)

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize plugins
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(portfolio_controller.bp)

    # Register the custom filter
    app.jinja_env.filters['date'] = format_date

    return app
