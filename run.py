# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 14:30"
__Author__ = 'eyu Fanne'

from app import create_app
app=create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5003)