# Import the necessary modules
from src.app import (
    create_app,
)  # This is to import the function that creates the Flask application
from src import routes  # This is to import the routes module

# Create an instance of the Flask application
app = create_app()

# Initialize the routes with the Flask application instance
routes.init_app(app)

# This is the entry point of the application
if __name__ == "__main__":
    # Run the application
    # debug=True enables debug mode for the application
    # host='0.0.0.0' makes the server publicly available
    # port=5000 is the port number the server will listen on
    # threaded=True enables multithreading
    # use_reloader=True enables the reloader which will restart the server if code changes are detected
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True, use_reloader=True)
