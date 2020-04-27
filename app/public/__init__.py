from flask import Blueprint
bp_public = Blueprint('public', __name__)
from . import views