"""
    用户进行登录并获取Token
"""
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.libs.wyy_exception import AuthFailedException
from app.models.user_model import UserModel
from app.validates.forms import ClientForm, TokenForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

api = Redprint('token')


@api.route('/get_token', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: UserModel.verify_by_email
    }
    identity = promise[form.type.data](form.account.data, form.secret.data)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)
    return jsonify({'token': token.decode('ascii')}), 200


@api.route('/get_token_info')
def get_token_info():
    form = TokenForm().validate_for_api()
    token = form.token.data
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token, return_header=True) # 返回token的创建时间，及存在的有效时间
    except BadSignature:
        # 无效token
        raise AuthFailedException(msg='无效token')
    except SignatureExpired:
        # token已失效
        raise AuthFailedException(msg='token已失效')
    print(data)
    return ''


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
        scope关键字是用于权限管理
    :param uid:
    :param ac_type:
    :param scope:
    :param expiration:
    :return:
    """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })