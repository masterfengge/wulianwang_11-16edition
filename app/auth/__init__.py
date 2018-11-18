# coding:UTF-8
# by jyf
from flask import Blueprint
auth = Blueprint('auth', __name__)

from . import views