# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 14:27"
__Author__ = 'eyu Fanne'

from flask import Flask
from views import bp
from app.admin import create_admin
import flask_whooshalchemyplus
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_babel import Babel

from models import db

bootstrap = Bootstrap()
babel = Babel()


def create_app() :
    app = Flask(__name__)
    app.config.from_object('config')
    bootstrap.init_app(app)
    db.init_app(app)
    register_blueprints(app)
    create_admin(app)
    flask_whooshalchemyplus.init_app(app)
    init_login(app)
    babel.init_app(app)
    return app


def register_blueprints(app):
    app.register_blueprint(bp)

def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))
