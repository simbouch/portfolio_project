#!/bin/bash

# Build script for Render deployment
echo "🚀 Starting build process..."

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Set up the database
echo "🗄️ Setting up database..."
python -c "
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    from portfolio_app import create_app, db
    
    app = create_app(os.environ.get('FLASK_CONFIG', 'config.ProductionConfig'))
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print('✅ Database tables created successfully!')
        
        # Create sample data
        from portfolio_app.models.project import Project
        from portfolio_app.models.experience import Experience
        from portfolio_app.models.skill import Skill
        
        # Only create sample data if tables are empty
        if Project.query.count() == 0:
            Project.create_sample_data()
            print('✅ Sample projects created!')
            
        if Experience.query.count() == 0:
            Experience.create_sample_data()
            print('✅ Sample experiences created!')
            
        if Skill.query.count() == 0:
            Skill.create_sample_data()
            print('✅ Sample skills created!')
            
        print('🎉 Database setup completed successfully!')
        
except Exception as e:
    print(f'⚠️ Database setup warning: {e}')
    print('Continuing with deployment...')
"

echo "✅ Build process completed!"
