# Flask
from flask import Flask

# Flask extentions
from flask_bootstrap import Bootstrap  # type: ignore
from flask_login import LoginManager  # type: ignore
from flask_login import login_manager

# Config
from .config import Config

# Blueprints
from .auth import auth
from .task import task

# Models
from .models import UserModel


# Configure the login manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query(user_id)



def create_app():
    """Create and configure an instance of the Flask application.

    Returns:
        app (Flask): The Flask application instance.
    """

    app = Flask(__name__)
    Bootstrap(app)

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(task)

    return app
