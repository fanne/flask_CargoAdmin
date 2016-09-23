# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 13:23"
__Author__ = 'eyu Fanne'

import os
basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is secret key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'Cargo.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS =True