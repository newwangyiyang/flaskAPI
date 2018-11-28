"""
    用于配置普通项的配置文件
"""
import os

from flask_uploads import IMAGES

DEBUG = True

TOKEN_EXPIRATION = 30 * 24 * 3600

# 设置文件上传
UPLOADED_FILE_DEST = os.path.join(os.getcwd(),'static/upload/image')
UPLOADED_FILE_ALLOW = IMAGES