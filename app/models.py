# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 14:41"
__Author__ = 'eyu Fanne'


from datetime import datetime
from jieba.analyse.analyzer import ChineseAnalyzer
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash,generate_password_hash
# from app import db
# from .import db
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        print 'dddddddddd'
        return check_password_hash(self.password_hash,password)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return self.name




class Goods(db.Model):
    __tablename__ = 'goods'
    __searchable__ = ['product_id','name','storage_location']
    __analyzer__ = ChineseAnalyzer()

    product_id = db.Column(db.Integer,index=True,primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    weight = db.Column(db.Float)
    norms = db.Column(db.String)
    residue_num = db.Column(db.Integer)
    sale_total = db.Column(db.Integer)
    storage_time = db.Column(db.DateTime,default=datetime.utcnow)
    storage_location = db.Column(db.String)

    meta = {
        'ordering':['-storage_time']
    }
