# coding:utf8
# by jyf
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_mail import Mail
import pymysql
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345678@127.0.0.1:3306/wulianwang"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
app.config["REDIS_URL"] = "redis://localhost:6379/0"
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")

# 邮件配置
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '17506483104@163.com'
app.config['MAIL_PASSWORD'] = 'mima1234'
app.config['JYF_MAIL_SUBJECT_PREFIX'] = '[JYF]'
app.config['JYF_MAIL_SENDER'] = '17506483104@163.com'


app.debug = True
mail = Mail(app)
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from app.auth import auth as auth_blueprint
from app.main import main as main_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint, url_prefix="/main")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
