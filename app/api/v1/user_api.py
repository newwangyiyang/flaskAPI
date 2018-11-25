"""
    user的视图函数
"""

from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get_user')
def get_user():
    return 'get_user'
