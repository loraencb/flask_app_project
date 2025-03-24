"""Define the User model for SQLAlchemy ORM."""

from ..extension import db

class User(db.Model):
    """User model with name, email, phone, address, and password."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    password = db.Column(db.String(100))

    def __repr__(self):
        return f'<User {self.name}>'
