#!/usr/bin/env python3
"""Update project schema to add owner_avatar_url field."""
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def update_project_schema():
    """Update the project schema and refresh sample data."""
    try:
        from portfolio_app import create_app, db
        from portfolio_app.models.project import Project

        app = create_app()

        with app.app_context():
            print("🔄 Updating project schema...")

            # Drop and recreate all tables to ensure schema is up to date
            db.drop_all()
            print("✅ Dropped all tables")

            # Create all tables with new schema
            db.create_all()
            print("✅ Created all tables with updated schema")

            # Create new sample data with owner_avatar_url
            Project.create_sample_data()
            print(f"✅ Created {Project.query.count()} projects with updated data")

            # Verify the data
            print("\n📋 Sample projects with GitHub URLs:")
            projects = Project.query.limit(5).all()
            for project in projects:
                print(f"  - {project.title}")
                print(f"    GitHub: {project.safe_github_url}")
                print(f"    Avatar: {project.safe_owner_avatar_url}")
                print(f"    Username: {project.github_username}")
                print()

            print("🎉 Project schema update completed successfully!")

    except Exception as e:
        print(f"❌ Error updating project schema: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    update_project_schema()
