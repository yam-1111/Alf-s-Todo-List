# AWSCC - PUP Manila Todo API Flask

This project provides a template for creating a Todo API using Flask. The API supports operations to create, read, update, and delete todos.

## Getting Started

These instructions will guide you to set up and run this project:

1. **Set up a virtual environment**

    Create a new virtual environment named `.venv` using the command:

    ```bash
    python -m venv .venv
    ```

2. **Activate the virtual environment**

    Activate the virtual environment with the following commands:

    For Windows:

    ```bash
    .venv\Scripts\activate
    ```

    For Unix or MacOS:

    ```bash
    source .venv/bin/activate
    ```

3. **Install dependencies**

    Install the required packages listed in the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

4. **Launch the application**

    Run the application using:

    ```bash
    python run.py
    ```

    The Flask development server starts and the application becomes accessible at `http://localhost:5000`.

## Project Structure

Here's an overview of the project's file structure:

- `src`: Contains the main application code.
- `src/static`: Houses the CSS and image files.
- `src/templates`: Stores the HTML files.
- `src/app.py`: Includes the main function to initiate and create the app.
- `src/models.py`: Defines the model for the todo.
- `src/routes.py`: Specifies the routes.
- `run.py`: Used to run the application.

## Tasks

Your assignment is to create routes for managing tasks:

1. **Add a task**

    Create a route to add a new task. This route should accept POST requests and take the task details as JSON in the request body.

2. **Update a task**

    Create a route to update an existing task. This route should accept PUT or PATCH requests, take the task ID as a URL parameter, and take the new task details as JSON in the request body.

3. **Change a task's status**

    Create a route to change a task's status. This route should accept PUT or PATCH requests, take the task ID as a URL parameter, and take the new status as JSON in the request body.

4. **Delete a task**

    Create a route to delete a task. This route should accept DELETE requests and take the task ID as a URL parameter.

Update your database model and schema as necessary to support these features.

## Workflow 

1. Begin by completing the tasks in app.py.
2. Create the Todo model in models.py.
3. Set up run.py.
4. Before running run.py, ensure you have set up the index route to return index.html in routes.py.
5. Create the endpoints for add_task, update_task/<int:task_id>, delete_task/<int:task_id>.
6. Test the app.

Enjoy using the AWSCC - PUP Manila - DCC: Alf's Todo List!