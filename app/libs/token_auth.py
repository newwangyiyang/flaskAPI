"""
    Token验证
"""
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.wyy_exception import AuthFailedException

auth = HTTPTokenAuth(scheme='WYY')

User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_token
def verify_token(token):
    user = verigy_auth_token(token)
    if not user:
        return False
    else:
        g.user = user
        return True



def verigy_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        # 无效token
        raise AuthFailedException(msg='无效token')
    except SignatureExpired:
        # token已失效
        raise AuthFailedException(msg='token已失效')
    uid = data['uid']
    ac_type = data['type']
    return User(uid, ac_type, '')