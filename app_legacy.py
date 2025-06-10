# WSGI entry point for production deployment
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import the create_app function from the app package
from app import create_app

# Create the Flask application instance for production
app = create_app(os.environ.get('FLASK_CONFIG', 'config.ProductionConfig'))

if __name__ == '__main__':
    # For local development
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
