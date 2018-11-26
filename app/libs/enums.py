"""
    定义常用的枚举
"""
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_PHONE = 101

    # 微信小程序
    USER_MINI = 200
    # 微信公众号
    USER_WX = 201