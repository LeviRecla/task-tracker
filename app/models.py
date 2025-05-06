from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# task has an id, title, description, and status
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), default="todo")  # todo | in-progress | done
