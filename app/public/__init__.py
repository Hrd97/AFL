from flask import Blueprint
bp_testresult = Blueprint('publicproject', __name__)
from . import views