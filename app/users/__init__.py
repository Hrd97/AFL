from flask import Blueprint
bp_users = Blueprint('users', __name__)
from . import views