#!/usr/bin/env python3
"""
Simple test script to verify the Flask application works correctly
"""
import pytest
from portfolio_app import create_app

def test_app_creation():
    """Test that the app can be created successfully"""
    app = create_app('config.DevelopmentConfig')
    assert app is not None

def test_index_route():
    """Test the index route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Bouchaib Khribech' in response.data

def test_about_route():
    """Test the about route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/about')
        assert response.status_code == 200
        assert b'About Me' in response.data

def test_projects_route():
    """Test the projects route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/projects')
        assert response.status_code == 200
        assert b'Projects' in response.data

def test_skills_route():
    """Test the skills route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/skills')
        assert response.status_code == 200
        assert b'Skills' in response.data

def test_experience_route():
    """Test the experience route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/experience')
        assert response.status_code == 200
        assert b'Experience' in response.data

def test_contact_route():
    """Test the contact route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/contact')
        assert response.status_code == 200
        assert b'Contact' in response.data

def test_interests_route():
    """Test the interests route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/interests')
        assert response.status_code == 200
        assert b'Interests' in response.data

def test_gallery_route():
    """Test the gallery route"""
    app = create_app('config.DevelopmentConfig')
    with app.test_client() as client:
        response = client.get('/gallery')
        assert response.status_code == 200
        assert b'Gallery' in response.data

if __name__ == '__main__':
    # Run basic tests
    print("Testing Flask application...")
    
    try:
        test_app_creation()
        print("✓ App creation test passed")
        
        test_index_route()
        print("✓ Index route test passed")
        
        test_about_route()
        print("✓ About route test passed")
        
        test_projects_route()
        print("✓ Projects route test passed")
        
        test_skills_route()
        print("✓ Skills route test passed")
        
        test_experience_route()
        print("✓ Experience route test passed")
        
        test_contact_route()
        print("✓ Contact route test passed")

        test_interests_route()
        print("✓ Interests route test passed")

        test_gallery_route()
        print("✓ Gallery route test passed")

        print("\n🎉 All tests passed! The application is working correctly.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        exit(1)
