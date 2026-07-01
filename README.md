# FastAPI JWT Auth API

A RESTful API built using FastAPI, PostgreSQL, SQLAlchemy ORM, and JWT Authentication. This project demonstrates secure user authentication, password hashing, CRUD operations, and a modular router-based architecture.

# Features

JWT Authentication

User Registration

User Login using OAuth2

Password Hashing with Passlib (bcrypt)

Create Posts

Read Posts

Update Posts

Delete Posts

PostgreSQL Database

SQLAlchemy ORM

Dependency Injection

Modular Router Structure

HTTP Exception Handling

# Tech Stack

Python

FastAPI

PostgreSQL

SQLAlchemy

JWT

OAuth2

Passlib (bcrypt)

Pydantic

# Project Structure

```text
app/
│
├── routers/
│   ├── auth.py
│   ├── oauth2.py
│   ├── post.py
│   └── user.py
│
├── database.py
├── models.py
├── schemas.py
├── utilis.py
├── main.py
│
README.md
requirements.txt
```

# Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/fastapi-jwt-auth-api.git
```

```bash
cd fastapi-jwt-auth-api
```

## Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure PostgreSQL

Update the database connection string in `database.py`.

```python
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/database_name"
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```text
http://127.0.0.1:8000/redoc
```

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /login | Authenticate a user |

## Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users | Register a new user |
| GET | /users/{id} | Retrieve a user |

## Posts

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /posts | Create a post |
| GET | /posts | Retrieve all posts |
| GET | /posts/{id} | Retrieve a single post |
| PUT | /posts/{id} | Update a post |
| DELETE | /posts/{id} | Delete a post |

# Authentication

Protected endpoints require a valid JWT access token.

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

# Future Improvements

Post ownership and authorization

Pagination

Search and filtering

Comments system

Likes and reactions

Docker support

Alembic database migrations

Automated testing

Deployment

# Author

Abdullah

Undergraduate Computer Engineering Student

Interested in Backend Development, Artificial Intelligence, and Software Engineering.

# License

MIT License
