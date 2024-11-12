# Configuration settings
# portfolio_project/config.py

import os

class Config:
    """Base configuration with common settings."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_secret_key")
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI", "sqlite:///development.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """Production environment configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///production.db")

class TestingConfig(Config):
    """Testing environment configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI", "sqlite:///test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
