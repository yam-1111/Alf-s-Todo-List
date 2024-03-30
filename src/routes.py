from flask import render_template, request, redirect, url_for
from .app import db 
from .models import Todo

def init_app(app):
    @app.route('/')
    def index():
        todo_list = Todo.query.all()
        return render_template('index.html', todo_list=todo_list)

    @app.route('/add_task', methods=['POST'])
    def add_task():
        task = request.form.get('task')
        new_task = Todo(task=task, status=False)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/update_task/<int:task_id>')
    def update_task(task_id):
        todo = Todo.query.get(task_id)
        todo.status = not todo.status
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/delete_task/<int:task_id>')
    def delete_task(task_id):
        todo = Todo.query.get(task_id)
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))