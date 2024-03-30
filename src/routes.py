# Import necessary modules from flask
from flask import render_template, request, redirect, url_for

# Import the database instance and Todo model from the app and models module respectively
from .app import db
from .models import Todo

# Import send_from_directory function from flask to serve static files
from flask import send_from_directory


# Function to initialize the application with routes
def init_app(app):
    # Route for the home page
    @app.route("/")
    def index():
        # Fetch all tasks from the database
        todo_list = Todo.query.all()
        # Render the index page with the tasks
        return render_template("index.html", todo_list=todo_list)

    # Route for adding a task, only allows POST method
    @app.route("/add_task", methods=["POST"])
    def add_task():
        # Get the task from the form data
        task = request.form.get("task")
        # Create a new task with status as False
        new_task = Todo(task=task, status=False)
        # Add the task to the database
        db.session.add(new_task)
        # Commit the changes to the database
        db.session.commit()
        # Redirect to the home page
        return redirect(url_for("index"))

    # Route for updating a task, task_id is passed in the URL
    @app.route("/update_task/<int:task_id>")
    def update_task(task_id):
        # Fetch the task from the database
        todo = Todo.query.get(task_id)
        # Toggle the status of the task
        todo.status = not todo.status
        # Commit the changes to the database
        db.session.commit()
        # Redirect to the home page
        return redirect(url_for("index"))

    # Route for deleting a task, task_id is passed in the URL
    @app.route("/delete_task/<int:task_id>")
    def delete_task(task_id):
        # Fetch the task from the database
        todo = Todo.query.get(task_id)
        # Delete the task from the database
        db.session.delete(todo)
        # Commit the changes to the database
        db.session.commit()
        # Redirect to the home page
        return redirect(url_for("index"))
    
    # DO NOT TOUCH!!! - Route for serving images and css file
    # Route for serving images from the static directory
    @app.route("/static/images/<path:filename>")
    def server_static_images(filename):
        # Send the image file from the directory
        response = send_from_directory("static/images", filename)
        # Set the Cache-Control header for the response
        response.headers["Cache-Control"] = "public, max-age=31536000"
        # Return the response
        return response

    # Route for serving CSS files from the static directory
    @app.route("/static/css/<path:filename>")
    def server_static_css(filename):
        # Send the CSS file from the directory
        response = send_from_directory("static/css", filename)
        # Set the Cache-Control header for the response
        response.headers["Cache-Control"] = "public, max-age=31536000"
        # Return the response
        return response
