"""
    1. Import create_app from src.app

    2. Import routes from src

    3. Create an instance of the app using create_app

    4. Initialize routes with app

    5. Run the app using app.run()

    6. Set debug=True, host="0.0.0.0", port=5000, threaded=True, use_reloader=True
"""

# Imports
from src.app import create_app
from src import routes

app = create_app()
routes.init_app(app) 
# Run app
if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True, use_reloader=True)
