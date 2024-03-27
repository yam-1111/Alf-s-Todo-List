from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from src.models.models import Todo
    with app.app_context():
        db.create_all()

    from src import views 
    app.register_blueprint(views.bp)

    return app