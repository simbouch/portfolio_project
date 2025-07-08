#!/usr/bin/env python3
"""Reset database and load new sample data."""
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def reset_database():
    """Reset the database and load new sample data."""
    try:
        from portfolio_app import create_app, db
        from portfolio_app.models.experience import Experience
        from portfolio_app.models.project import Project
        from portfolio_app.models.skill import Skill

        app = create_app()

        with app.app_context():
            print("🗄️ Resetting database...")

            # Drop all tables
            db.drop_all()
            print("✅ Dropped all tables")

            # Create all tables
            db.create_all()
            print("✅ Created all tables")

            # Create new sample data
            print("📊 Creating sample data...")

            Project.create_sample_data()
            print(f"✅ Created {Project.query.count()} projects")

            Experience.create_sample_data()
            print(f"✅ Created {Experience.query.count()} experiences")

            Skill.create_sample_data()
            print(f"✅ Created {Skill.query.count()} skills")

            print("🎉 Database reset completed successfully!")

            # Show some sample projects to verify
            print("\n📋 Sample projects:")
            projects = Project.query.limit(5).all()
            for project in projects:
                print(f"  - {project.title}: {project.github_url}")

    except Exception as e:
        print(f"❌ Error resetting database: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    reset_database()
