"""
    book视图函数
"""
from flask import request, jsonify, current_app

from app.libs.redprint import Redprint

# 实例化自定义红图
from app.libs.token_auth import auth
from app.libs.wyy_exception import SuccessException
from app.models.book_model import BookModel
from app.models.user_model import UserModel
from app.validates.forms import BookForm

api = Redprint('book')


@api.route('/add_book', methods=['POST'])
@auth.login_required
def add_book():
    BookForm().validate_for_api()
    BookModel.add_book(request.json)
    return SuccessException()


@api.route('/all_book', methods=['POST'])
def all_book():
    books = BookModel.query.filter_by().all()
    return jsonify(books)
