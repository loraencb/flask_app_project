from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()

    # Add sample users
    user1 = User(name="Alice Wonderland", email="alice@example.com")
    user2 = User(name="Bob SquarePants", email="bob@example.com")

    # Add to DB session
    db.session.add(user1)
    db.session.add(user2)

    # Commit changes
    db.session.commit()

    print("Sample users added successfully!")
