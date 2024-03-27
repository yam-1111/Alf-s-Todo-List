from flask import Blueprint, render_template, request, redirect, url_for, current_app
from src import db
from src.models.models import Todo

bp = Blueprint("views", __name__)


@bp.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)
