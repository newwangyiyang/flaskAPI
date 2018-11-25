"""
    自定义异常，继承HTTPException
"""
from app.libs.base_exception import BaseApiException


class ClientTypeException(BaseApiException):
    code = 400
    msg = '请求参数错误'
    status_code = 1