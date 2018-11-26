"""
    用户进行登录并获取Token
"""
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user_model import UserModel
from app.validates.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
api = Redprint('token')


@api.route('/get_token', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: UserModel.verify_by_email
    }
    identity = promise[form.type.data](form.account.data, form.secret.data)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, None, expiration)
    return jsonify({'token': token.decode('ascii')}), 200


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value
    })