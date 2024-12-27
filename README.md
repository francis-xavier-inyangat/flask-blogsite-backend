# Flask Backend API with Authentication and Blueprint Architecture

## Overview
This project is built using the **Python Flask Framework** and focuses on creating a robust backend architecture for a web application. It demonstrates key backend engineering principles, including:

- Designing and implementing **RESTful APIs**.
- Utilizing Flask's **Blueprint Architecture** for modularity and scalability.
- Securing and managing connections to an **SQLite database**.
- Serving a basic frontend using **Jinja Templates**.

The project is structured to showcase the ability to create a secure, scalable, and maintainable backend while adhering to best practices.

---

## Features

### Backend APIs
- **User Authentication**:
  - Registration and login endpoints.
  - Password hashing using **Werkzeug** for security.
- **CRUD Operations**:
  - Create, Read, Update, and Delete functionalities for resources.
- **Error Handling**:
  - Robust error handling to ensure smooth API operation.

### Blueprint Architecture
- Modular design using Flask **Blueprints** for logical separation of concerns.
- Organized file structure for scalability and maintainability.

### Database
- Secure connection to an **SQLite database**.
- Database schema initialization using `schema.sql`.
- Example tables for user authentication and additional resources.

### Jinja Templates
- Basic frontend served using **Jinja Templates** to demonstrate integration between backend and frontend.
- Dynamically rendered pages with server-side data.

---

## Prerequisites
- Python 3.7+
- Pip (Python Package Manager)

### Install Required Packages
Run the following command to install the necessary dependencies:
```bash
pip install -r requirements.txt
```

---

## Project Structure
```
flask_learning/
  flaskr/
        ├── app/
    │   ├── __init__.py           # App factory and initialization
    │   ├── auth/
    │   │   ├── __init__.py       # Authentication blueprint
    │   │   ├── routes.py         # Routes for registration and login
    │   ├── main/
    │   │   ├── __init__.py       # Main blueprint
    │   │   ├── routes.py         # Routes for the main application
    │   ├── templates/            # Jinja templates for frontend
    │   ├── static/               # Static files (CSS, JS, images)
    │   ├── database.py           # Database connection and utilities
    ├── schema.sql                # SQLite schema definition
    ├── requirements.txt          # Python dependencies
    ├── run.py                    # Entry point for the application
    └── README.md                 # Documentation

```

---

## Usage

### Running the Application on Dev
_cd flask_learning_
1. Initialize the database:
   ```bash
   flask init-db || flask --app flaskr init-db
   ```
_cd flask_learning_
2. Start the Flask server:
   ```bash
   flask run || flask --app flaskr run 
   ```

3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## API Endpoints

### Authentication
- **POST /auth/register**
  - Registers a new user.
  - Payload:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
  - Response:
    ```json
    {
      "message": "User registered successfully"
    }
    ```

- **POST /auth/login**
  - Logs in an existing user.
  - Payload:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
  - Response:
    ```json
    {
      "message": "Welcome, username!"
    }
    ```

## Security
- **Password Security**:
  - Passwords are hashed using **Werkzeug's `generate_password_hash`**.
  - Securely verified using `check_password_hash`.

- **Database Security**:
  - SQL statements are parameterized to prevent SQL injection.

---

## Development

### Running in Development Mode
Enable debug mode for development:
```bash
export FLASK_ENV=development
flask run
```

### Testing
You can write and run unit tests using `pytest`:
```bash
pytest
```

---

## Future Enhancements
- Implement **JWT-based authentication** for tokenized session management.
- Add role-based access control (RBAC) for more granular permission handling.
- Expand API endpoints to include additional resources.
- Improve frontend templates with more dynamic and responsive designs.
- Integrate a production-ready database like PostgreSQL or MySQL.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- SQLite Documentation: [https://sqlite.org/docs.html](https://sqlite.org/docs.html)
- Werkzeug Security: [https://werkzeug.palletsprojects.com/](https://werkzeug.palletsprojects.com/)

Feel free to contribute to the project by submitting issues or pull requests!
