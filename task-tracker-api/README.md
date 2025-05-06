# Task Tracker API

A simple Flask-based RESTful API to manage tasks. This project currently contains the backend for as task tracking application.

---

## Features

- Create tasks with a title and description
- Update task title, description, and status (`todo`, `in-progress`, `done`)
- Delete tasks
- Get a list of all tasks
- Built with Flask, SQLAlchemy, and SQLite
- Designed for integration with an Angular frontend

---

## Project Structure

```
task-tracker-api/
├── app/
│   ├── __init__.py        # App factory and route registration
│   ├── models.py          # SQLAlchemy models
│   └── routes.py          # API route definitions
├── config.py              # Configuration settings
├── run.py                 # Entry point to run the server
├── .env                   # Environment variables (e.g., DB URI)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/levirecla/task-tracker-api.git
cd task-tracker-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate     # On Windows Git Bash
# or
venv\Scripts\activate.bat      # On Windows CMD
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file:

```
DATABASE_URL=sqlite:///tasks.db
SECRET_KEY=your-secret-key
```

### 5. Run the application

```bash
python run.py
```

The API will start on `http://127.0.0.1:5000/`

---

## API Endpoints

| Method | Endpoint               | Description            |
|--------|------------------------|------------------------|
| GET    | `/api/tasks/`          | List all tasks         |
| POST   | `/api/tasks/`          | Create a new task      |
| PUT    | `/api/tasks/<id>`      | Update a task          |
| DELETE | `/api/tasks/<id>`      | Delete a task          |

### Example `POST /api/tasks/`

```json
{
  "title": "Finish Flask API",
  "description": "Add update and delete routes"
}
```

### Example `PUT /api/tasks/1`

```json
{
  "status": "done"
}
```

---

## Status Values

Valid task status values are:

- `todo`
- `in-progress`
- `done`

---

## Testing the API

You can use [Postman](https://www.postman.com/) or `curl` to test the API routes.

Example:

```bash
curl -X POST http://127.0.0.1:5000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "description": "Test creation"}'
```

---

## Built With

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- [Python 3.11](https://www.python.org/)

---

## Next Steps

- Add JWT authentication
- Add pagination for task lists
- Build Angular 18 frontend
- Dockerize for deployment

---

