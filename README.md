# Flask Greeting API

This is a simple Flask-based web application that provides a greeting API. The API accepts a name parameter via the query string and returns a personalized greeting message.

## Features

- **GET `/api/greet`**: This endpoint accepts a `name` parameter via the query string and returns a greeting message.
  - If no name is provided, it defaults to greeting a "Guest".
  
## Requirements

To run this project, you need to have Python installed on your system. This application uses the Flask web framework.

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone or download the repository to your local machine.
2. Install the required Python packages by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you can install Flask directly:

    ```bash
    pip install flask
    ```

## Usage

1. Ensure the Flask app is running by executing the following command in your project directory:

    ```bash
    python app.py
    ```

    By default, the app will run on `http://0.0.0.0:5050`.

2. You can now access the greeting API. Open a browser or use a tool like `curl` or Postman to send a GET request to the following URL:

    ```http
    http://localhost:5050/api/greet?name=YourName
    ```

    Replace `YourName` with the name you wish to greet. If no name is provided, the response will default to "Guest".

### Example Requests

1. **Request with Name**:

    ```http
    GET http://localhost:5050/api/greet?name=John
    ```

    **Response**:

    ```json
    {
        "message": "Hello, John!"
    }
    ```

2. **Request without Name** (defaults to "Guest"):

    ```http
    GET http://localhost:5050/api/greet
    ```

    **Response**:

    ```json
    {
        "message": "Hello, Guest!"
    }
    ```

## Development

### Running the App in Debug Mode

The app runs with debug mode enabled by default (`debug=True`), which provides detailed error messages and auto-reloads the server during development.

### Modifying the Greeting Message

If you'd like to modify the greeting message, you can adjust the line in the `greet_user` function:

```python
response_message = {"message": f"Hello, {user_name}!"}
```
