"""
    参数验证模块
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user_model import UserModel


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), Length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, field):
        """
            对type进行自定义验证器
            :return:
        """
        try:
            client = ClientTypeEnum(field.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='请输入正确的邮箱地址')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[0-9a-zA-Z_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(), Length(min=2, max=22)])

    def validate_account(self, field):
        if UserModel.query.filter_by(email=field.data).first():
            raise ValidationError()
