# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 15:24"
__Author__ = 'eyu Fanne'

from flask_admin import Admin
from views import MyIndexView,UserView,GoodsView
from app.models import User,db,Goods

def create_admin(app=None):
    admin = Admin(app, name="CargoAdmin",
                  index_view=MyIndexView(),
                  template_mode='bootstrap3',
                  base_template='admins/my_master.html')
    admin.add_view(UserView(User,db.session))
    admin.add_view(GoodsView(Goods,db.session))


