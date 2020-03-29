from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, request, url_for
from .config import Config
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.debug = True
    db.init_app(app)


    from .auth import bp_auth
    app.register_blueprint(bp_auth, url_prfix="/")

    from .users import bp_users
    app.register_blueprint(bp_users, url_prfix='/users')
    #
    # from .testresult import bp_testresult
    # app.register_blueprint(bp_testresult, url_prfix='/testresult')

    return app
