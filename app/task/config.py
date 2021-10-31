# Flask
from flask import Blueprint


task = Blueprint('tasks', __name__, url_prefix='/tasks')
