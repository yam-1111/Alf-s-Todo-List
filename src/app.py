"""
    1. Import Flask from flask

    2. Import SQLAlchemy from flask_sqlalchemy

    3. Create an instance of SQLAlchemy called db - db = SQLAlchemy()

    4. Create a create_app function - def create_app():

    5. Create an instance of Flask called app inside the create_app function - app = Flask(__name__)

    6. Configure the app with the SQLALCHEMY_DATABASE_URI and SQLALCHEMY_TRACK_MODIFICATIONS  
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" 
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    7. Initialize the db with the app - db.init_app(app)

    8. With the app context, create the database - db.create_all()

    9. Return the app - return app
"""

# Import

# Create an instance of SQLAlchemy 

# def create_app():
def create_app():
    pass
