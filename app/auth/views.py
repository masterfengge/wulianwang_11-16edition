# coding:utf8
# by jyf
from flask import render_template, redirect, url_for, flash, session, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User, Item
from .forms import LoginForm
from .. import db
from functools import wraps
from werkzeug.utils import secure_filename
import os
import datetime
import json


# 上下应用处理器
@auth.context_processor
def tpl_extra():
    data = dict(
        online_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    return data


# 登录装饰器
def login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "auth" not in session:
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


# 管理员首页
@auth.route("/", methods=["GET", "POST"])
# @login_req
def indexofsupermanager(page=None):
    if page is None:
        page = 1
    page_data = Item.query.order_by(
        Item.item_id.desc()
    ).paginate(page=page, per_page=10)
    itemnum = Item.query.count()
    # print (page_data)
    return render_template("indexofsupermanager.html", page_data=page_data, itemnum=itemnum)


# 动态刷新工程列表
@auth.route('/indexofsupermanager/<item_id>/refresh_data/', methods=['GET', 'POST'])
def refresh(item_id):
    b = Item.query.filter_by(item_id=item_id).first()
    d = {'item_id': b.item_id, 'name': b.item_name, 'location': b.item_loc, 'manager': b.item_manager,
         'time': b.item_starttime}
    print(d)
    return json.dumps(d, default=str)


# 搜索工程
@auth.route('/indexofsupermanager/<item_id>/search_data/', methods=['GET', 'POST'])
def search(item_id):
    a = Item.query.filter_by(item_id=item_id).first()
    c = {'item_id': a.item_id, 'name': a.item_name, 'location': a.item_loc, 'manager': a.item_manager,
         'time': a.item_starttime}
    print(c)
    return json.dumps(c, default=str)


# 登录页面
@auth.route("/login/", methods=["GET", "POST"])
def login():
    return render_template("login.html")
