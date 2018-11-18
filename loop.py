# coding:utf-8
from app import db, app
from app.models import Item, Device, Sensor, Sensor_thre, Warn
from app.email import  send_email

app.app_context().push()#手动进行上下文联系
def loop():
    while (1):
        res = Item.query.all()
        for i in res:

            datas = Sensor.query.filter_by(item_id=i.item_id).all()  # 每个工程号下的传感器数据

            for data in datas:
                for t in data.sensor_thre:

                    if t.sensor_threshold:
                        if data.sensor_data < t.sensor_threshold:

                            continue
                        # 生成告警历史
                        else:
                            warn = Warn(warn_time=data.data_time,
                                        sensor_data=data.sensor_data,
                                        sensor_type=data.sensor_type,
                                        sensor_thre=t.sensor_threshold,
                                        warn_state='未处理',
                                        warn_message='未发送',
                                        sensor_id=data.sensor_id)
                            # 发送邮件
                            mail = i.user.user_email
                            state = send_email(mail, 'Comfirm your Account')
                            if state == 1:
                               print('A confirmation email has been sent to your email.')
                               warn.warn_message = ['已发送']
                            db.session.add(warn)
                            db.session.commit()
        break

#
if __name__ == "__main__":
    loop()
