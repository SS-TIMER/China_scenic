# 创建app     manage
from flask import Flask

from App.extensions import init_ext
from App.config import envs
from App.views import init_first_blue


def create_app():
    app = Flask(__name__)
    # 初始化设置  config

    app.config.from_object(envs.get("develop"))
    # 初始化蓝图  views   blue

    init_first_blue(app)
    # 初始化扩展  ext

    init_ext(app)
    return app
