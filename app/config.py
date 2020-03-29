class Config(object):
    # 这边进行自定义
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SECRET_KEY = '184172410'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dbgroup:DBgroup2019.@175.24.44.2/afl'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:darihan.@localhost/hsp'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    DEBUG = True
    #
    # @staticmethod
    # def init_app(app):
    #     pass

