# Flask App Project

This is a simple Flask web application that displays text and database records using SQLAlchemy and HTML templates.  
It includes a modular architecture with Blueprints, an application factory, unit tests, and a separate DB insertion script.

# Flask Web App – User Management System

This project is a simple Flask web application that allows users to be added, viewed, edited, and deleted using a SQLite database. It uses modular file architecture, SQLAlchemy ORM, Flask Blueprints, HTML templates, custom CSS styling, and includes automated testing and linting for quality assurance.

---

## Setup Instructions (PLEASE READ CAREFULLY)

1. **Install requirements:**
```
pip install -r requirements.txt
```

2. **Initialize the database (one-time setup):**
```
python query.py
```
---

## How to Run the App

Start the Flask server:
```
python run.py
```

Open your browser and go to:
- http://localIP:5000/ → Homepage
- http://localIP:5000/add-user → Add a new user
- http://localIP:5000/users → View all users

---

## CRUD Functionality

| Action        | Route                   |
|---------------|--------------------------|
| Create User   | `/add-user` (HTML form) |
| Read Users    | `/users`                |
| Update User   | `/edit/<user_id>`       |
| Delete User   | `/delete/<user_id>`     |

---

## Styling

The app is styled using `style.css` located in `app/static/`.  
All HTML templates extend a unified layout through `base.html`.

---

## Testing with Pytest

Run all tests:
```
pytest
```

Test coverage includes:
- Homepage
- Add user (GET and POST)
- Edit user (GET and POST)
- Delete user
- View users
- 404 error handling

---

## Quality with Pylint

Run Pylint to check code style:
```
pylint app/
```

This ensures your code follows best practices and helps catch common bugs or formatting issues.

---

## Project Checklist

- ✅ Clean Project File Architecture
- ✅ Unit Testing Coverage with Pytest
- ✅ Good Code Style (Pylint Included)
- ✅ requirements.txt
- ✅ OOP Concept in SQLAlchemy User Model
- ✅ Multiple Flask Routing Methods (GET, POST)
- ✅ Separation of App Factory and Entry Point
- ✅ Flask Blueprints Used
- ✅ HTML Templates with Base Layout
- ✅ SQLAlchemy ORM for DB Operations
- ✅ Full CRUD Functionality (Create, Read, Update, Delete)
- ✅ Styled UI

---

## Contact

Author: Braulio Lora Encarnacion  
Email: loraencb@kean.edu
