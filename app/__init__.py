from flask import Flask
from flask_cors import CORS

from app.company.view import app_company


def create_app():
    app = Flask(__name__)
    CORS(app)
    _register_blueprint(app)
    return app


def _register_blueprint(app):
    app.register_blueprint(app_company)
