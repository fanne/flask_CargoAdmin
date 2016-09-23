# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 15:29"
__Author__ = 'eyu Fanne'


from flask_admin import AdminIndexView,expose
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user,current_user,logout_user
from flask import redirect,request,url_for
from forms import LoginForm
from ..models import User,Goods

class MyIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login'))
        return self.render('admins/my_master.html')
        # return super(MyIndexView,self).index()

    @expose('/login',methods=('GET','POST'))
    def login(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(name=form.username.data).first()
            # print  user.password_hash

            if user is not None:
                print 'ddddddddd'
                if user.verify_password(form.password.data):
                    print 'true'
                    login_user(user)
                    return redirect(url_for('.index'))
                else:
                    print 'error'
            else:
                print 'user is None'
        return self.render('admins/index.html',form=form)
        # return super(MyIndexView,self).index()


    @expose('/logout')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def on_model_change(self, form, User, is_created):
        User.password = form.password_hash.data



class GoodsView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
