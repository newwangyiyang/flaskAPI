"""
    book视图函数
"""

from app.libs.redprint import Redprint

# 实例化自定义红图
api = Redprint('book')


@api.route('/get_book')
def get_book():
    return 'get_book'
