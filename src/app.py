# Import the Flask module for creating a web server
from flask import Flask

# Import the SQLAlchemy module for database operations
from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy object
db = SQLAlchemy()

# Define a function to create a Flask application
def create_app():
    # Create a Flask web server
    app = Flask(__name__)

    # Configure the database URI for the SQLAlchemy object
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    # Disable track modifications for SQLAlchemy to suppress warning
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the SQLAlchemy object with the Flask app
    db.init_app(app)

    # Create all the database tables within the application context
    with app.app_context():
        db.create_all()

    # Return the created Flask application
    return app
