# coding:utf8
# by jyf
DEBUG = True
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from app import app

from flask_script import Manager, Shell

manage = Manager(app)

if __name__ == "__main__":
    manage.run()
