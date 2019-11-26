def get_db_uri(dbinfo):
    # 获取值，值不存在给默认值
    BACKEND = dbinfo.get('BACKEND') or 'mysql'

    DRIVER = dbinfo.get('DRIVER') or 'pymysql'

    USERNAME = dbinfo.get('USERNAME') or 'root'

    PASSWORD = dbinfo.get('PASSWORD') or 'root'

    HOST = dbinfo.get('HOST') or '127.1.1.0'

    PORT = dbinfo.get('PORT') or '3306'

    DATABASE = dbinfo.get('DATABASE') or 'aronp'

    return "{}+{}://{}:{}@{}:{}/{}".format(BACKEND, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)


class Config:
    SECRET_KEY = 'Aaronuo'

    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 不同的环境有环境配置-----开发环境
class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'HOST': '127.1.1.0',
        'PROT': '3306',
        'DATABASE': 'aronp'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 不同的环境有环境配置-----测试环境
class TestingConfig(Config):
    DEBUG = True

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PROT': '3306',
        'DATABASE': 'aronp'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 不同的环境有环境配置-----演示环境
class StagingConfig(Config):
    DEBUG = True

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PROT': '3306',
        'DATABASE': 'data_data_Staging'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 不同的环境有环境配置-----演示环境
class ProductConfig(Config):
    DEBUG = True

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PROT': '3306',
        'DATABASE': 'data_data_Product'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
}
