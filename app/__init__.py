from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
# Om en användare inte är inloggad, omdirigera till "login"-vyn
login_manager.login_view = "main.login"


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)
    from app.routes import bp
    flask_app.register_blueprint(bp)

    db.init_app(flask_app)
    login_manager.init_app(flask_app)  # Add this line to initialize login manager

    with flask_app.app_context():
        from app import models
        db.create_all()

    return flask_app

