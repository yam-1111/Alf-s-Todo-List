# Import the db object from the app module
from .app import db

# Define a Todo model that inherits from db.Model
class Todo(db.Model):
    # Define a task_id column as an Integer type and set it as the primary key
    task_id = db.Column(db.Integer, primary_key=True)

    # Define a task column as a String type with a maximum length of 100 characters
    task = db.Column(db.String(100))

    # Define a status column as a Boolean type
    status = db.Column(db.Boolean)
