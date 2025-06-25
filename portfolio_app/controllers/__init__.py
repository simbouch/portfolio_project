from flask import Flask
from app.controllers.portfolio_controller import bp as portfolio_bp


def create_app():
    """
    Application factory to initialize and configure the Flask app.
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"

    # Register blueprints
    app.register_blueprint(portfolio_bp, url_prefix="/")

    return app
