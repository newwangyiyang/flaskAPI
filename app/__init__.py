"""
    核心对象的初始化
"""

from .app import Flask
from flask_cors import CORS


def register_blueprint_v1(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base_model import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    CORS(app)

    register_blueprint_v1(app)
    register_plugin(app)
    return app