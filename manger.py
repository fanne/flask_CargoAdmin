# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 14:46"
__Author__ = 'eyu Fanne'

# from flask_script import Manager,Shell,Server
from flask.ext.script import Manager, Shell
from flask_migrate import Migrate,MigrateCommand,upgrade
from app import create_app
from app.models import User,Goods
from app import db
from werkzeug. security import generate_password_hash

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User,Goods=Goods)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

@manager.command
def add_user():
    admin = User(id='1',name='admin',email='admin@qq.com',password_hash=generate_password_hash('admin123'))
    db.session.add(admin)
    db.session.commit()

if __name__ == '__main__':
    manager.run()