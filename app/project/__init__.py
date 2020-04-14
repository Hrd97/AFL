from flask import Blueprint
bp_project = Blueprint('project', __name__)
from . import views