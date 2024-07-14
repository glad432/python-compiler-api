# Python Compiler API

## Overview

This repository contains a Flask-based web API for compiling and running Python code snippets. It allows users to submit Python code and receive the output or error messages from the execution. The API is designed to handle Python code compilation, execution, and error handling in a secure and efficient manner.

## Setup

To set up the Python Compiler, follow these steps:

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/glad432/python-compiler-api.git
    ```
2. Navigate into the cloned repository directory
    ```
    cd python-compiler-api
    ```
3. Install the required dependencies listed in `requirements.txt` using pip:
    ```
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```
    python app.py
    ```
5. The application should now be running locally.

## Usage

- Open your web browser and go to `http://localhost:5000`.
- Enter Python code in the provided text area.
- Click the "Run Code" button to execute the code.
- The output or any errors will be displayed below the Preformatted Text element.

### Endpoints

The Python Compiler API provides a single endpoint:

- `POST /run`: Accepts Python code submitted in the request body and returns the output or error messages from its execution.

   Example usage with curl:

   ```bash
   curl -X POST -H "Content-Type: text/plain" -d "print('Hello, World!')" http://localhost:5000/run


### CORS Configuration:

CORS (Cross-Origin Resource Sharing) is configured to allow requests from specified origins, ensuring compatibility with cross-origin requests, such as those from https://example.com.

## Dependencies:

- Flask: A lightweight WSGI web application framework for Python.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS), making cross-origin AJAX possible.
- subprocess: The subprocess module in Python facilitates spawning new processes, managing their input/output, and handling return codes.

## Contributing:

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
