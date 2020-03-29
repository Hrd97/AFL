from flask import Blueprint
bp_testresult = Blueprint('testresult', __name__)
from . import views