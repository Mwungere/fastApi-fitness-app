Fitness Tracker App

Welcome to the Fitness Tracker App! This application helps users track their fitness activities, set goals, and monitor progress. It is built using FastAPI, a modern, fast (high-performance) web framework for Python.

Table of Contents

Features

Requirements

Installation

Usage

API Endpoints

License

Features

User authentication (registration, login, logout)

Track fitness activities (e.g., running, cycling, gym sessions)

Set and monitor fitness goals

View progress through dashboards and reports

API-first design for seamless integration with other services

Requirements

To run this project, ensure you have the following installed:

Python 3.8+

FastAPI

Uvicorn

A virtual environment tool (optional but recommended)

Database (PostgreSQL)

Installation

Follow these steps to set up the project on your local machine:

# Clone the repository:

    git clone https://github.com/your-username/fitness-tracker-app.git
    cd fitness-tracker-app

# Create a virtual environment: (optional but recommended)
        python -m venv venv
        source venv/bin/activate  # For Linux/Mac
        venv\Scripts\activate   # For Windows    

# Set up environment variables:

Create a .env file in the root of the project and configure the following variables:
    DATABASE_URL=sqlite:///./fitness.db  # Or your preferred database URL
    SECRET_KEY=your_secret_key_here
    ACCESS_TOKEN_EXPIRE_MINUTES=30

# Run migrations: (if applicable)
    alembic upgrade head  # SQLAlchemy
# or
    tortoise-orm migrate --run  # Tortoise         

# Start the application:

Use Uvicorn to run the application:
        uvicorn main:app --reload


# Usage

Access the API documentation:

Open your browser and visit:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Test the endpoints:

Use the provided documentation to test various endpoints, such as user registration, login, and fitness activity tracking.

Front-end Integration:

If you have a front-end application, connect it to the API base URL (http://127.0.0.1:8000).

API Endpoints

Here are some key endpoints for the app:

Authentication

POST /auth/register: Register a new user

POST /auth/login: Log in and obtain a token

POST /auth/logout: Log out the current user

Fitness Activities

GET /activities: Get all activities for the logged-in user

POST /activities: Add a new fitness activity

PUT /activities/{id}: Update an existing activity

DELETE /activities/{id}: Delete an activity            