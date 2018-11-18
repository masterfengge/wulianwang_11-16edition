# coding:utf8
from datetime import datetime
from app import db

from sqlalchemy.sql import func
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# # 会员
# class User(db.Model):
#     __tablename__ = "user"
#     __table_args__ = {"useexisting": True}
#     id = db.Column(db.Integer, primary_key=True)  # 编号
#     name = db.Column(db.String(100), unique=True)  # 昵称
#     pwd = db.Column(db.String(100))  # 密码
#     email = db.Column(db.String(100), unique=True)  # 邮箱
#     phone = db.Column(db.String(11), unique=True)  # 手机号码
#     info = db.Column(db.Text)  # 个性简介
#     face = db.Column(db.String(255), unique=True)  # 头像
#     addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
#     uuid = db.Column(db.String(255), unique=True)  # 唯一标志符
#
#     # userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关系关联
#     # comments = db.relationship('Comment', backref='user')  # 评论外键关系关联
#     # moviecols = db.relationship('Moviecol', backref='user')  # 收藏外键关系关联
#
#     def __repr__(self):
#         return "<User %r>" % self.name
#
#     def check_pwd(self, pwd):
#         from werkzeug.security import check_password_hash
#         return check_password_hash(self.pwd, pwd)

# 项目使用用户
class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)  # 非空
    user_passport = db.Column(db.String(100), nullable=False)
    user_auth = db.Column(db.Integer)
    user_email = db.Column(db.String(100), nullable=False)
    user_phone = db.Column(db.Integer)
    # 设置外键
    item = db.relationship('Item', backref='user')  # 一个用户对应多个工程号

    def __repr__(self):
        return "<User %r>" % self.user_name


class Item(db.Model):
    __tablename__ = 'item'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)  # 工程号
    item_loc = db.Column(db.String(100), nullable=False)  # 工程位置
    item_manager = db.Column(db.String(20), nullable=False)  # 使用单位
    item_starttime = db.Column(db.DateTime, nullable=False)  # 开始时间
    item_name = db.Column(db.String(20), nullable=False)  # 工程名
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    bridge = db.Column(db.String(255), unique=True)  # 地址
    # 设置外键
    sensor = db.relationship('Sensor', backref='item')  # 一个工程对应多个传感器号
    notice = db.relationship('Notice', backref='item')  # 一个工程对应多个施工管理

    def __repr__(self):
        return "<Item %r>" % self.item_id


class Device(db.Model):
    __tablename__ = 'device'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    # 设置外键
    sensor = db.relationship('Sensor', backref='device')  # 一解调仪对应多个传感器号


class Sensor(db.Model):
    __tablename__ = 'sensor'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, nullable=False)
    sensor_data = db.Column(db.Float)
    sensor_type = db.Column(db.String(20), nullable=False)
    data_time = db.Column(db.DateTime, index=True, default=datetime.now)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))  # 所属工程号
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))  # 所属解调仪
    # 设置外键
    sensor_thre = db.relationship('Sensor_thre', backref='sensor')  # 一个传感器对应一个阈值
    warn_id = db.relationship('Warn', backref='sensor')  # 一个传感器对应多个告警历史

    def __repr__(self):
        return "<Sensor %r>" % self.sensor_id


class Sensor_thre(db.Model):
    __tablename__ = 'sensor_thre'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    sensor_threshold = db.Column(db.Float)  # 阈值
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))  # 所属传感器
    item_id = db.Column(db.Integer)

    def __repr__(self):
        return "<Sensor_thre %r>" % self.sensor_threshold


class Warn(db.Model):
    __tablename__ = 'warn'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    warn_time = db.Column(db.Date)  # 告警时间
    #
    sensor_data = db.Column(db.Float)
    sensor_type = db.Column(db.String(20), nullable=False)
    sensor_thre = db.Column(db.Float)
    #
    warn_state = db.Column(db.String(20), nullable=False)  # 告警处理状态,1代表处理完成,2代表待处理
    warn_message = db.Column(db.String(200), nullable=False)  # 短信发送状态
    warn_remark = db.Column(db.String(200))  # 备注
    item_id = db.Column(db.Integer, nullable=False)  # 所属工程号
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))  # 所属传感器

    def __repr__(self):
        return "<Warn %r>" % self.id


class Notice(db.Model):
    __tablename__ = 'notice'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    notice_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 通知时间
    notice_comp = db.Column(db.DateTime, nullable=True)  # 完成时间
    notice_remark = db.Column(db.String(200), nullable=True)  # 备注
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))  # 所属工程号

    # 设置外键
    staff = db.relationship('Staff', backref='notice')  # 一个通知对应一组人员信息

    def __repr__(self):
        return "<Notice %r>" % self.notice_time


class Staff(db.Model):
    __tablename__ = 'staff'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(20), nullable=False)
    staff_phone = db.Column(db.String(45), nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    notice_id = db.Column(db.Integer, db.ForeignKey('notice.id'))  # 所属通知

    def __repr__(self):
        return "<Staff %r>" % self.staff_name


db.create_all()

# if __name__ == "__main__":


# role = Role(
#     name="超级管理员",
#     auths=""
# )
# db.session.add(role)
# db.session.commit()
# from werkzeug.security import generate_password_hash
#
# admin = Admin(
#     name="imoocmovie",
#     pwd=generate_password_hash("imoocmovie"),
#     is_super=0,
#     role_id=1
# )
# db.session.add(admin)
# db.session.commit()
