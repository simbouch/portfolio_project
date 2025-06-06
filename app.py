# WSGI entry point for production deployment
import os
from app import create_app

# Create the Flask application instance
app = create_app(os.environ.get('FLASK_CONFIG', 'config.ProductionConfig'))

if __name__ == '__main__':
    # For local development
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
