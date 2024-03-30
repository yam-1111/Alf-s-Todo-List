"""
    1. import render_template, request, redirect, url_for from flask

    2. import db from .app

    3. import Todo from .models

    4. Create a function called init_app that takes app as an argument

    5. Create a route for the index page
        - Get all the tasks from the database
        - Render the index.html template with the tasks - render_template("index.html", todo_list=todo_list)

    6. Create a route for the add task page
        - Get the task from the request form
        - Create a new Todo object with the task and status
        - Add the new Todo object to the database
        - Commit the changes to the database
        - Redirect the user to the index page - redirect(url_for("index"))

    7. Create a route for the update task page
        - Get the task from the database based on the task_id
        - Update the status of the task
        - Commit the changes to the database
        - Redirect the user to the index page - redirect(url_for("index"))

    8. Create a route for the delete task page
        - Get the task from the database based on the task_id
        - Delete the task from the database
        - Commit the changes to the database
        - Redirect the user to the index page - redirect(url_for("index"))


    Usable Functions for database manipulation:
    1. Todo.query.all() - Get all the tasks from the database
    2. Todo.query.get(task_id) - Get a task from the database based on the task_id
    3. db.session.add(new_task) - Add a new task to the database
    4. db.session.commit() - Commit the changes to the database
    5. db.session.delete(todo) - Delete a task from the database
"""

# Imports
from flask import send_from_directory

# Create a function called init_app that takes app as an argument
def init_app(app):
    # Create a route for the index page
    @app.route("/")
    def index():
        pass
    
    # Create a route for the add task
    @app.route("/add_task", methods=["POST"])
    def add_task():
        pass

    # Create a route for the update task
    @app.route("/update_task/<int:task_id>")
    def update_task(task_id):
        pass

    # Create a route for the delete task
    @app.route("/delete_task/<int:task_id>")
    def delete_task(task_id):
        pass


                                # DO NOT TOUCH THESE ENPOINTS #

    @app.route("/static/images/<path:filename>")
    def server_static_images(filename):
        response = send_from_directory("static/images", filename)
        response.headers["Cache-Control"] = "public, max-age=31536000"
        return response

    @app.route("/static/css/<path:filename>")
    def server_static_css(filename):
        response = send_from_directory("static/css", filename)
        response.headers["Cache-Control"] = "public, max-age=31536000"
        return response
