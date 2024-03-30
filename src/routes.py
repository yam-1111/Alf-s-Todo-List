from flask import render_template, request, redirect, url_for
from .app import db
from .models import Todo
from flask import send_from_directory

def init_app(app):
    @app.route("/")
    def index():
        todo_list = Todo.query.all()
        return render_template("index.html", todo_list=todo_list)

    @app.route("/add_task", methods=["POST"])
    def add_task():
        task = request.form.get("task")
        new_task = Todo(task=task, status=False)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/update_task/<int:task_id>")
    def update_task(task_id):
        todo = Todo.query.get(task_id)
        todo.status = not todo.status
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/delete_task/<int:task_id>")
    def delete_task(task_id):
        todo = Todo.query.get(task_id)
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("index"))

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
