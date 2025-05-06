from flask import Blueprint, request, jsonify
from .models import db, Task

task_bp = Blueprint("tasks", __name__)

# GET route to retrieve a task
@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "description": t.description,
        "status": t.status
    } for t in tasks])

# POST route to add a task to the db
@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.json
    new_task = Task(title=data["title"], description=data.get("description", ""))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201

# PUT route to create a task
@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify({"message": "Task updated"})

# DELETE route to delete a task
@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    # Query and return the task if it exists
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})
