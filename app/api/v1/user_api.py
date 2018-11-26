"""
    user的视图函数
"""
from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user_model import UserModel

api = Redprint('user')


# @auth.login_required
@api.route('/get_user/<uid>')
def get_user(uid):
    user = UserModel.query.get_or_404(uid)
    print(user.email)
    return jsonify(user)
