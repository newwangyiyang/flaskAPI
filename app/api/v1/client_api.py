"""
    客户端注册
"""
from flask import request, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.libs.wyy_exception import ClientTypeException
from app.models.user_model import UserModel
from app.validates.forms import ClientForm, UserEmailForm

api = Redprint('client')


def __create_client_by_email():
    form = UserEmailForm(data=request.json)

    if form.validate():
        UserModel.register_by_email(form.nickname.data, form.account.data, form.secret.data)


@api.route('/create_client', methods=['POST'])
def create_client():
    json_data = request.json
    form = ClientForm(data=json_data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __create_client_by_email
        }
        promise[form.type.data]()
    else:
        raise ClientTypeException
    return 'success'


