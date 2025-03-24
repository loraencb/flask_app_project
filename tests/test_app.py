"""Test suite for Flask App."""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app
from app.extension import db
from app.models.user import User

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()

        # Clear any existing test data before adding a user
        db.session.query(User).delete()
        db.session.commit()


        # Now safely add a fresh user
        user = User(
            name="Test User",
            email="test@example.com",
            phone="1234567890",
            address="123 Main St",
            password="testpass"
        )
        db.session.add(user)
        db.session.commit()

    return app


@pytest.fixture
def client(app):
    """Flask test client fixture."""
    return app.test_client()

def test_home_route(client):
    """Test homepage route."""
    response = client.get('/')
    assert response.status_code == 200

def test_users_route(client):
    """Test users listing route."""
    response = client.get('/users')
    assert response.status_code == 200
    assert b"Test User" in response.data

def test_add_user_form_get(client):
    """Test add user form GET route."""
    response = client.get('/add-user')
    assert response.status_code == 200

def test_add_user_form_post(client, app):
    """Test add user form POST route."""
    with app.app_context():
        response = client.post('/add-user', data={
            'name': 'User Two',
            'email': 'user2@example.com',
            'phone': '222-333-4444',
            'address': '456 Another St',
            'password': 'test123'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b"User Two" in response.data

def test_edit_user_get(client, app):
    """Test edit user form GET route."""
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        response = client.get(f'/edit/{user.id}')
        assert response.status_code == 200

def test_edit_user_post(client, app):
    """Test edit user form POST route."""
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        response = client.post(f'/edit/{user.id}', data={
            'name': 'Updated Name',
            'email': 'updated@example.com',
            'phone': '999-888-7777',
            'address': 'Updated Ave',
            'password': 'updatedpass'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b"Updated Name" in response.data

def test_delete_user(client, app):
    """Test delete user route."""
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        response = client.get(f'/delete/{user.id}', follow_redirects=True)
        assert response.status_code == 200
        assert b"Test User" not in response.data
