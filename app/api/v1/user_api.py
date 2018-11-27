"""
    user的视图函数
"""
from flask import jsonify, g

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.wyy_exception import SuccessException, AuthFailedException
from app.models.base_model import db
from app.models.user_model import UserModel

api = Redprint('user')


@api.route('/super_get_user/<uid>', methods=['POST'])
@auth.login_required
def super_get_user(uid):
    user = UserModel.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/get_user', methods=['POST'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = UserModel.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/delete_user', methods=['POST'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = UserModel.query.filter_by(id=uid).first_or_404()
        user.delete()
    return SuccessException()
