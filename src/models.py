"""
    1. Import db from .app 

    2. Create Todo class that inherits from db.Model

    3. Define columns for Todo class
    - task_id: Integer, primary_key
    - task: String
    - status: Boolean
"""

# Imports
from src.app import db

# Create Todo class
class Todo(db.Model):
    task_id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(255), unique=True)
    status = db.Column(db.Boolean)