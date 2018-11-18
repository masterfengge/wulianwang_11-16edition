#coding:UTF-8
# by jyf
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, forms