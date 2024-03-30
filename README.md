# AWSCC - PUP Manila Todo API Flask

This is a template for creating a Todo API using Flask. This API allows you to create, read, update, and delete todos.

## Instructions

Follow these steps to set up and run this project:

1. **Create a virtual environment**

    Use the following command to create a new virtual environment named `.venv`:

    ```bash
    python -m venv .venv
    ```

2. **Activate the virtual environment**

    Before you can start using the virtual environment, you need to activate it. 

    On Windows, use:

    ```bash
    .venv\Scripts\activate
    ```

    On Unix or MacOS, use:

    ```bash
    source .venv/bin/activate
    ```

3. **Install the required packages**

    This project requires some packages to run. These packages are listed in the `requirements.txt` file. To install them, use:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**

    After you've installed the required packages, you can run the application with:

    ```bash
    python run.py
    ```

    This will start the Flask development server, and you can access the application at `http://localhost:5000`.


## File Structure

The project has the following file structure:

- `src`: Main application code.
- `src/static`: Contains the CSS and Images.
- `src/templates`: Contains the HTML File.
- `src/app.py`: Contains the main function to initiate and create the app.
- `src/models.py`: Contains the model for the todo
- `src/routes.py`: Contains the routes.
- `run.py`: This file is used to run the application.

## Task

Your task is to create the following routes for managing tasks:

1. **Adding a task**

    Create a route that allows users to add a new task. This route should accept POST requests and take the task details as JSON in the request body.

2. **Updating a task**

    Create a route that allows users to update an existing task. This route should accept PUT or PATCH requests, take the task ID as a parameter in the URL, and take the new task details as JSON in the request body.

3. **Changing the status of a task**

    Create a route that allows users to change the status of a task. This route should accept PUT or PATCH requests, take the task ID as a parameter in the URL, and take the new status as JSON in the request body.

4. **Deleting a task**

    Create a route that allows users to delete a task. This route should accept DELETE requests and take the task ID as a parameter in the URL.

Remember to update your database model and schema as necessary to support these features.

Enjoy using the AWSCC - PUP Manila - DCC: Alf's Todo List