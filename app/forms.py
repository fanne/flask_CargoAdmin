# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 17:27"
__Author__ = 'eyu Fanne'

from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])