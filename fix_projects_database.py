#!/usr/bin/env python3
"""Fix projects database by resetting and recreating with proper schema."""
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def fix_projects_database():
    """Fix the projects database and restore all projects."""
    try:
        from portfolio_app import create_app, db
        from portfolio_app.models.project import Project
        from portfolio_app.models.experience import Experience
        from portfolio_app.models.skill import Skill

        app = create_app()

        with app.app_context():
            print("🔧 Fixing projects database...")

            # Drop and recreate all tables to fix schema issues
            db.drop_all()
            print("✅ Dropped all tables")

            # Create all tables with correct schema
            db.create_all()
            print("✅ Created all tables with fixed schema")

            # Create sample data
            print("📊 Creating sample data...")
            
            Project.create_sample_data()
            print(f"✅ Created {Project.query.count()} projects")

            Experience.create_sample_data()
            print(f"✅ Created {Experience.query.count()} experiences")

            Skill.create_sample_data()
            print(f"✅ Created {Skill.query.count()} skills")

            print("🎉 Database fix completed successfully!")

            # Verify projects are working
            print("\n📋 Verifying projects:")
            projects = Project.query.limit(5).all()
            for project in projects:
                print(f"  - {project.title}")
                print(f"    GitHub: {project.safe_github_url}")
                print(f"    Avatar: {project.safe_owner_avatar_url}")
                print(f"    Username: {project.github_username}")
                print(f"    Type: {project.project_type}")
                print()

            print("✅ All projects are now working correctly!")

    except Exception as e:
        print(f"❌ Error fixing projects database: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    fix_projects_database()
