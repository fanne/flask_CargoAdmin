# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 18:01"
__Author__ = 'eyu Fanne'

from wtforms import StringField,PasswordField
from wtforms import form
from wtforms import validators
from wtforms.validators import DataRequired
from ..models import User
from werkzeug.security import check_password_hash,generate_password_hash
from flask.ext.wtf import Form

class LoginForm(Form):
    username = StringField(label=u'用户名', validators=[DataRequired()])
    password = PasswordField(label=u'密码', validators=[DataRequired()])

    # def get_user(self):
    #     user = User.query(username=self.username.data).first()
    #     return user
    #
    # def validate_name(self,field):
    #     user = self.get_user()
    #     print user.username
    #     if user:
    #         if not check_password_hash(user.password,self.password.data):
    #             raise validators.ValidationError('password error')
    #     else:
    #         raise validators.ValidationError('user error')

# class LoginForm(form.Form):
#     name = StringField('name',validators=[DataRequired()])
#     password = PasswordField('password',validators=[DataRequired()])
#
