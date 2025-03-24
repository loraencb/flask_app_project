"""Application configuration."""

class Config:
    """Flask configuration class."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
