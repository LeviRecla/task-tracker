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

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required."}), 400

    valid_statuses = ["todo", "in-progress", "done"]
    status = data.get("status", "todo")
    if status not in valid_statuses:
        return jsonify({"error": f"Invalid status. Choose from {valid_statuses}."}), 400

    new_task = Task(
        title=data["title"].strip(),
        description=data.get("description", "").strip(),
        status=status
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description,
        "status": new_task.status
    }), 201



# PUT route to create a task
@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json

    if not data:
        return jsonify({"error": "No update data provided."}), 400

    # Validate title if updating
    if "title" in data and not data["title"].strip():
        return jsonify({"error": "Title cannot be empty."}), 400

    # Validate status
    if "status" in data:
        valid_statuses = ["todo", "in-progress", "done"]
        if data["status"] not in valid_statuses:
            return jsonify({"error": f"Invalid status. Choose from {valid_statuses}."}), 400

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)

    db.session.commit()
    return jsonify({"message": "Task updated"}), 200


# DELETE route to delete a task
@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    # Query and return the task if it exists
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})
