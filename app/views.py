# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-30 14:28"
__Author__ = 'eyu Fanne'

from flask import Blueprint,render_template,g,redirect,url_for
from models import Goods
from .forms import SearchForm

bp = Blueprint('app',__name__)
@bp.route('/')
def index():
    goodslist = Goods.query.all()
    return render_template('index.html',goodslist=goodslist)

@bp.before_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/search', methods = ['GET','POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('main.index'))
    return redirect(url_for('app.search_results', query = g.search_form.search.data))


@bp.route('/search_results/<query>',methods=['GET','POST'])
def search_results(query):
    results = Goods.query.whoosh_search(query,fields=('product_id','name','price','weight','storage_location')).all()
    return render_template('search_results.html',
                           query = query,results = results)


