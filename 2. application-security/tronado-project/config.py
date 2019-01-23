# coding=utf-8

import os
BASE_DIRS = os.path.dirname(__file__)
import base64
import uuid
base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

#参数
options = {
    "port":"8000",
}


#配置
settings = {
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "templates"),
    "cookie_secret": "uuQzfZpaSbaKPK9AkA7WAVQsvUUwjU+IpcGGxPOl7Fk=",
    "xsrf_cookies": True,
    "login_url":"/login"
    # "debug": True
}