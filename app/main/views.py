# coding:utf8
# by jyf
from . import main
from flask import render_template, redirect, url_for, flash, session, request, Response, request, abort
from app.main.forms import ItemForm, ItemeditForm, SggleditForm, GcszForm, StaffForm
from app.models import User, Item, Device, Sensor, Sensor_thre, Staff, Warn, Notice
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from app import db, app, rd
from functools import wraps
import uuid
import os
import datetime
import json
from ..email import send_email
from flask_login import current_user


# 修改文件名称
def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return filename


# 工程主页面
@main.route("/<int:item_id>/", methods=["GET", "POST"])
def gczym(item_id=None):
    id = item_id
    item = Item.query.filter_by(item_id=id).first_or_404()
    # page_data = Device.query.filter_by(item_id=item_id).all()
    # 查询解调仪
    page_data = Device.query.filter_by(
        item_id=item_id
    ).all()
    # print (page_data)
    # 查询传感器
    page_data2 = Sensor.query.filter_by(
        item_id=item_id
    ).all()
    return render_template("gczym.html", item_id=id, page_data=page_data, page_data2=page_data2, item=item)


# 传感器历史数据
@main.route("/sensor_history/<int:sensor_id>/<int:item_id>/", methods=["GET", "POST"])
def sensor_history(sensor_id=None, item_id=None):
    page_data = Sensor.query.filter_by(
        sensor_id=sensor_id
    ).paginate(page=1, per_page=10)
    return render_template("sensor_history.html", sensor_id=sensor_id, item_id=item_id, page_data=page_data)


# 工程主页面的设置
@main.route("/item_edit/<int:sensor_id>/<int:item_id>/", methods=["GET", "POST"])
def item_edit(sensor_id=None, item_id=None):
    sensor = Sensor.query.filter_by(sensor_id=sensor_id, item_id=item_id).first()
    sensorthre = Sensor_thre.query.filter_by(sensor_id=sensor_id).first_or_404()
    form = ItemeditForm()
    # form.item_id.validators = []
    # form.sensor_id.validators = []
    # form.sensor_type.validators = []
    form.sensor_thre.validators = []
    # print (sensorthre.sensor_threshold)
    # print(sensor.sensor_type)
    if form.validate_on_submit():
        data = form.data
        sensorthre.sensor_threshold = data["sensor_thre"]
        db.session.add(sensorthre)
        db.session.commit()
        flash("修改阈值成功!", "ok")
        return redirect(
            url_for('main.item_edit', sensor_id=sensor_id, item_id=item_id, sensor=sensor, sensorthre=sensorthre))
    return render_template("item_edit.html", item_id=item_id, sensor_id=sensor_id, sensor=sensor, sensorthre=sensorthre,
                           form=form)


# 工程主页面传感器状态刷新
@main.route("/gczym_ssxx/<int:idd>/<int:item_id>/", methods=["GET", "POST"])
def gczym_ssxx(idd=None, item_id=None):
    b = Sensor.query.filter_by(sensor_id=idd, item_id=item_id).first()
    d = {'sensor_type': b.sensor_type, 'sensor_data': b.sensor_data}
    print (d)
    return json.dumps(d, default=str)


# 工程主页面的传感器阈值查询
@main.route("/gczym_yzcx/<int:idd>/<int:item_id>/", methods=["GET", "POST"])
def gczym_yzcx(idd=None, item_id=None):
    a = Sensor_thre.query.filter_by(sensor_id=idd, item_id=item_id).first()
    c = {'sensor_thre': a.sensor_threshold}
    print (c)
    return json.dumps(c, default=str)


# 电路板
@main.route("/dianluban/<int:item_id>/", methods=["GET", "POST"])
def dianluban(item_id=None):
    return render_template("dianluban.html", item_id=item_id)


# 摄像头
@main.route("/shexiangtou/<int:item_id>/", methods=["GET", "POST"])
def shexiangtou(item_id=None):
    return render_template("shexiangtou.html", item_id=item_id)


# 解调仪
@main.route("/jietiaoyi/<int:item_id>/", methods=["GET", "POST"])
def jietiaoyi(item_id=None):
    return render_template("jietiaoyi.html", item_id=item_id)


# 用户管理
@main.route("/usermanage/")
def usermanage(item_id=None):
    return render_template("usermanage.html", item_id=item_id)


# 告警历史
@main.route("/gjls/<int:item_id>/", methods=["GET", "POST"])
def gjls(item_id=None):
    # page_data = Warn.query.order_by(
    #     Warn.id.desc()
    # ).paginate(page=1, per_page=10)
    page_data = Warn.query.filter_by(item_id=item_id).paginate(page=1, per_page=10)
    return render_template("gjls.html", item_id=item_id, page_data=page_data)


# 告警历史查询
@main.route("/gjls_cx/<string:zhuangtai>/<int:item_id>/<string:starttime>/<string:endtime>/")
def gjls_cx(item_id=None, zhuangtai=None, starttime=None, endtime=None):
    page_data = Warn.query.filter_by(
        item_id=item_id, warn_state=zhuangtai
    ).filter(
        Warn.warn_time.between(starttime, endtime)
    ).paginate(page=1, per_page=10)
    print (page_data)
    return render_template("gjls_cx.html", item_id=item_id, page_data=page_data)


# 施工管理
@main.route("/sggl/<int:item_id>/<int:page>/", methods=["GET", "POST"])
def sggl(item_id=None, page=None):
    if page is None:
        page = 1
    page_data = Notice.query.filter_by(
        item_id=item_id
    ).paginate(page=page, per_page=10)
    page_data2 = Staff.query.filter_by(item_id=item_id).first()
    return render_template("sggl.html", item_id=item_id, page_data=page_data, page_data2=page_data2)


# 施工管理列表编辑
@main.route("/sggl_edit/<int:id>/<int:item_id>/", methods=["GET", "POST"])
def sggl_edit(id=None, item_id=None):
    form = SggleditForm()
    notice = Notice.query.filter_by(id=id, item_id=item_id).first_or_404()  # 这个notice定义一定不能写在if判断语句中
    if form.validate_on_submit():
        data = form.data
        notice.notice_remark = data["remark"],
        notice.notice_time = data["start_time"],
        notice.notice_comp = data["comp_time"]
        db.session.add(notice)
        db.session.commit()
        flash("修改成功!", "ok")
        return redirect(url_for('main.sggl_edit', item_id=item_id, id=id, notice=notice))
    return render_template("sggl_edit.html", item_id=item_id, id=id, notice=notice, form=form)


# 通知施工页面
@main.route("/sggl_tzsg/<int:item_id>/", methods=["GET", "POST"])
def sggl_tzsg(item_id=None):
    staff = Staff.query.filter_by(item_id=item_id).first_or_404()
    staff2 = staff.staff_phone
    send_email(staff2, '请您前往工程施工')
    return render_template("sggl_tzsg.html", staff=staff, item_id=item_id)


# 通知施工后自动记录施工信息
@main.route("/sggl_tzsg_zdjl/<int:item_id>/", methods=["GET"])
def sggl_tzsg_zdjl(item_id=None):
    # staff=Staff.query.filter_by(item_id=item_id).first_or_404()
    notice = Notice(
        notice_time=datetime.datetime.now().strftime("%Y-%m-%d"),
        notice_comp=datetime.datetime.now().strftime("%Y-%m-%d"),
        notice_remark="备注信息未填写",
        item_id=item_id

    )
    db.session.add(notice)
    db.session.commit()
    flash("成功！", "ok")
    return redirect(url_for('main.sggl_tzsg', item_id=item_id))


# 添加施工记录
@main.route("/sggl_tjjl/<int:item_id>/", methods=["GET", "POST"])
def sggl_tjjl(item_id=None):
    form = SggleditForm()
    if form.validate_on_submit():
        data = form.data
        notice = Notice(
            item_id=item_id,
            notice_time=data["start_time"],
            notice_comp=data["comp_time"],
            notice_remark=data["remark"]
        )
        db.session.add(notice)
        db.session.commit()
        flash("添加成功！", "ok")
        return redirect(url_for('main.sggl_tjjl', item_id=item_id))
    return render_template("sggl_tjjl.html", form=form, item_id=item_id)


# 施工人员信息修改
@main.route("/sggl_staff/<int:item_id>/", methods=["GET", "POST"])
def sggl_staff(item_id=None):
    form = StaffForm()
    staff = Staff.query.filter_by(item_id=item_id).first()
    if form.validate_on_submit():
        data = form.data
        staff.staff_name = data["staff_name"],
        staff.staff_phone = data["staff_rel"]
        db.session.add(staff)
        db.session.commit()
        flash("修改成功", "ok")
        return redirect(url_for('main.sggl_staff', item_id=item_id))
    return render_template("sggl_staff.html", form=form, item_id=item_id, staff=staff)


# 工程设置
@main.route("/gcsz/<int:item_id>/", methods=["GET", "POST"])
def gcsz(item_id=None):
    form = GcszForm()
    form.bridge.validators = []
    item = Item.query.filter_by(item_id=item_id).first_or_404()
    staff = Staff.query.filter_by(item_id=item_id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        staff.staff_name = data["staff_name"],
        staff.staff_phone = data["staff_rel"]
        db.session.add(staff)
        db.session.commit()
        file_url = secure_filename(form.bridge.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")
        bridge = change_filename(file_url)
        form.bridge.data.save(app.config["UP_DIR"] + bridge)
        item.bridge = bridge
        db.session.add(item)
        db.session.commit()
        flash("成功", "ok")
        return redirect(url_for('main.gcsz', item_id=item_id))

    return render_template("gcsz.html", item_id=item_id, item=item, staff=staff, form=form)


# 添加工程
@main.route("/engineering_add/", methods=["GET", "POST"])
def engineering_add():
    form = ItemForm()
    if form.validate_on_submit():
        data = form.data
        ensure = Item.query.filter_by(item_id=data["item_id"]).count()
        if ensure == 1:
            flash("工程号已存在！", "err")
            return redirect(url_for('main.engineering_add'))
        file_url = secure_filename(form.bridge.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")
        bridge = change_filename(file_url)
        form.bridge.data.save(app.config["UP_DIR"] + bridge)
        item = Item(
            item_id=data["item_id"],
            item_name=data["name"],
            item_loc=data["location"],
            item_manager=data["manager"],
            item_starttime=data["time"],
            bridge=bridge
        )
        db.session.add(item)
        db.session.commit()
        staff = Staff(
            item_id=data["item_id"],
            staff_name=data["staff_name"],
            staff_phone=data["staff_rel"]
        )
        db.session.add(staff)
        db.session.commit()
        flash("添加工程成功!", "ok")
        return redirect(url_for('main.engineering_add'))
    return render_template("engineering_add.html", form=form)


# 删除工程
@main.route("/engineering_del/<int:item_id>/", methods=["GET"])
def engineering_del(item_id=None):
    engineering = Item.query.filter_by(item_id=item_id).first_or_404()
    db.session.delete(engineering)
    db.session.commit()
    flash("删除工程成功！", "ok")
    return redirect(url_for('auth.indexofsupermanager', page=1))


# 超管首页设置工程
@main.route("/engineering_edit/<int:item_id>/", methods=["GET", "POST"])
def engineering_edit(item_id=None):
    form = ItemForm()
    form.item_id.validators = []
    form.name.validators = []
    form.location.validators = []
    form.manager.validators = []
    form.time.validators = []
    item = Item.query.filter_by(item_id=item_id).first_or_404()
    staff = Staff.query.filter_by(item_id=item_id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        ensure = Item.query.filter_by(item_name=data["name"]).count()
        idsum = Item.query.filter_by(item_id=data["item_id"]).count()
        idensure = Item.query.filter_by(item_id=data["item_id"]).first()
        file_url = secure_filename(form.bridge.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")
        bridge = change_filename(file_url)
        form.bridge.data.save(app.config["UP_DIR"] + bridge)
        # if ensure == 1 and item.item_name != data["name"]:
        #     flash("工程已存在!", "err")
        #     return redirect(url_for('main.engineering_edit', item_id=item_id))
        if idsum >= 1 and idensure.item_name != data["name"]:
            flash("工程号已存在!", "err")
            return redirect(url_for('main.engineering_edit', item_id=item_id))
        item.item_id = data["item_id"],
        item.item_name = data["name"],
        item.item_loc = data["location"],
        item.item_manager = data["manager"],
        item.item_starttime = data["time"],
        item.bridge = bridge
        db.session.add(item)
        db.session.commit()
        staff.staff_name = data["staff_name"],
        staff.staff_phone = data["staff_rel"]
        db.session.add(staff)
        db.session.commit()
        flash("修改工程成功!", "ok")
        return redirect(url_for('main.engineering_edit', item_id=item_id))
    return render_template('engineering_edit.html', form=form, item=item, staff=staff)


# 添加用户
@main.route("/user_add/")
def user_add():
    return render_template("user_add.html")


# 编辑用户
@main.route("/user_edit/")
def user_edit():
    return render_template("user_edit.html")
