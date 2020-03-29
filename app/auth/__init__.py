from flask import Blueprint

bp_auth = Blueprint('auth', __name__)

from . import views
