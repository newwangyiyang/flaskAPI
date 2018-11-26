"""
    user的视图函数
"""

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user_model import UserModel

api = Redprint('user')


@api.route('/get_user/<uid>')
@auth.login_required
def get_user(uid):
    user = UserModel.query.get_or_404(uid)
    return ''
