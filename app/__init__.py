from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .models import db
from .routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    db.init_app(app)
    CORS(app)
    
    app.register_blueprint(task_bp, url_prefix="/api/tasks")
    
    with app.app_context():
        db.create_all()

    return app
