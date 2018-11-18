# coding:UTF-8
# by jyf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from ..models import User, Item


class ItemForm(FlaskForm):
    item_id = StringField(
        label="工程号",
        validators=[
            DataRequired("请输入工程号！")
        ],
        description="工程号",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程号!"
        }
    )
    name = StringField(
        label="工程名称",
        validators=[
            DataRequired("请输入工程名称！")
        ],
        description="工程名称",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程名称!"
        }
    )
    location = StringField(
        label="工程地址",
        validators=[
            DataRequired("请输入工程地址！")
        ],
        description="工程地址",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程地址!"
        }
    )

    manager = StringField(
        label="工程管理单位",
        validators=[
            DataRequired("请输入工程管理单位！")
        ],
        description="工程管理单位",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程管理单位!"
        }
    )

    time = StringField(
        label="工程时间",
        validators=[
            DataRequired("请输入工程时间！")
        ],
        description="工程时间",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程时间!",
            "id": "input_time"
        }
    )

    staff_name = StringField(
        label="工程负责人",
        validators=[
            DataRequired("请输入工程负责人！")
        ],
        description="工程负责人",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程负责人!"
        }
    )

    staff_rel = StringField(
        label="联系方式",
        validators=[
            DataRequired("请输入负责人联系方式！")
        ],
        description="联系方式",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入负责人联系方式!"
        }
    )

    bridge = FileField(
        label="桥梁简图",
        validators=[
            DataRequired("请上传桥梁简图!")
        ],
        description="封面",
    )

    submit = SubmitField(
        '提交',
        render_kw={
            "class": "b1 click_pop"
        }
    )


class ItemeditForm(FlaskForm):
    # item_id = StringField(
    #     label="工程号",
    #     validators=[
    #         DataRequired("请输入工程号！")
    #     ],
    #     description="工程号",
    #     render_kw={
    #         "class": "carNo_input",
    #         "placeholder": "请输入工程号!"
    #     }
    # )
    # sensor_id = StringField(
    #     label="传感器号",
    #     validators=[
    #         DataRequired("请输入传感器号！")
    #     ],
    #     description="传感器号",
    #     render_kw={
    #         "class": "carNo_input",
    #         "placeholder": "请输入传感器号!"
    #     }
    # )
    # sensor_type = StringField(
    #     label="传感器类型",
    #     validators=[
    #         DataRequired("请输入传感器类型！")
    #     ],
    #     description="传感器类型",
    #     render_kw={
    #         "class": "carNo_input",
    #         "placeholder": "请输入传感器类型!"
    #     }
    # )
    sensor_thre = StringField(
        label="传感器阈值",
        validators=[
            DataRequired("请输入传感器阈值！")
        ],
        description="传感器阈值",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入传感器阈值!"
        }
    )
    submit = SubmitField(
        '确定',
        render_kw={
            "class": "shzclick"
        }
    )


class SggleditForm(FlaskForm):
    remark = StringField(
        label="备注信息",
        validators=[
            DataRequired("请输入备注信息!")
        ],
        description="传感器阈值",
        render_kw={
            "class": "carNo_imput",
            "placeholder": "请输入备注信息!"
        }
    )

    start_time = StringField(
        label="通知时间",
        validators=[
            DataRequired("请输入通知时间！")
        ],
        description="通知时间",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入通知时间!",
            "id": "input_start_time"
        }
    )

    comp_time = StringField(
        label="工程完成时间",
        validators=[
            DataRequired("请输入工程完成时间！")
        ],
        description="工程完成时间",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程完成时间!",
            "id": "input_comp_time"
        }
    )

    # staff = StringField(
    #     label="施工人员",
    #     validators=[
    #         DataRequired("请输入施工人员!")
    #     ],
    #     description="施工人员",
    #     render_kw={
    #         "class": "carNo_imput",
    #         "placeholder": "请输入施工人员!"
    #     }
    # )

    submit = SubmitField(
        '确定',
        render_kw={
            "class": "shzclick"
        }
    )


class GcszForm(FlaskForm):
    staff_name = StringField(
        label="工程负责人",
        validators=[
            DataRequired("请输入工程负责人！")
        ],
        description="工程负责人",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程负责人!"
        }
    )

    staff_rel = StringField(
        label="联系方式",
        validators=[
            DataRequired("请输入负责人联系方式！")
        ],
        description="联系方式",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入负责人联系方式!"
        }
    )

    # url = FileField(
    #     label="文件",
    #     validators=[
    #         DataRequired("请上传解调仪和传感器!")
    #     ],
    #     description="文件",
    # )

    bridge = FileField(
        label="桥梁简图",
        validators=[
            DataRequired("请上传桥梁简图!")
        ],
        description="封面",
    )

    submit = SubmitField(
        '确定',
        render_kw={
            "class": "shzclick"
        }
    )


class StaffForm(FlaskForm):
    staff_name = StringField(
        label="工程负责人",
        validators=[
            DataRequired("请输入工程负责人！")
        ],
        description="工程负责人",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入工程负责人!"
        }
    )

    staff_rel = StringField(
        label="联系方式",
        validators=[
            DataRequired("请输入负责人联系方式！")
        ],
        description="联系方式",
        render_kw={
            "class": "carNo_input",
            "placeholder": "请输入负责人联系方式!"
        }
    )
    submit = SubmitField(
        '确定',
        render_kw={
            "class": "shzclick"
        }
    )
