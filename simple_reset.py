#!/usr/bin/env python3
"""Simple database reset script"""
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def simple_reset():
    """Reset database with clean data"""
    try:
        from portfolio_app import create_app, db
        from portfolio_app.models.project import Project
        from portfolio_app.models.experience import Experience
        from portfolio_app.models.skill import Skill

        app = create_app()

        with app.app_context():
            print("🔄 Simple database reset...")

            # Drop and recreate tables
            db.drop_all()
            db.create_all()
            print("✅ Tables reset")

            # Create sample data
            Project.create_sample_data()
            Experience.create_sample_data()
            Skill.create_sample_data()
            
            print(f"✅ Created {Project.query.count()} projects")
            print(f"✅ Created {Experience.query.count()} experiences")
            print(f"✅ Created {Skill.query.count()} skills")

            # Verify projects have GitHub URLs
            print("\n📋 Project GitHub URLs:")
            for project in Project.query.limit(5).all():
                print(f"  - {project.title}: {project.github_url}")

            print("\n🎉 Reset complete!")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    simple_reset()
