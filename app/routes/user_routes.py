"""This file contains routes for user CRUD operations."""

from flask import Blueprint, render_template, request, redirect, url_for
from ..models.user import User
from ..extension import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def home():
    return render_template('home.html')

@user_bp.route('/add-user', methods=['GET', 'POST'])
def add_user():
    """Handles the form submission for adding a new user."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "<p style='color:red;'>Email already exists! <a href='/add-user'>Try again</a></p>"

        user = User(name=name, email=email, phone=phone, address=address, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_bp.list_users'))

    return render_template('add_user.html')

@user_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.name = request.form.get('name')
        user.email = request.form.get('email')
        user.phone = request.form.get('phone')
        user.address = request.form.get('address')
        user.password = request.form.get('password')
        db.session.commit()
        return redirect(url_for('user_bp.list_users'))

    return render_template('edit_user.html', user=user)

@user_bp.route('/delete/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_bp.list_users'))

@user_bp.route('/users')
def list_users():
    users = User.query.all()
    return render_template(
        'users.html',
        users=users
    )