from flask import Blueprint


Index_create = Blueprint('Index_create', __name__, template_folder='templates', static_folder='static')

from . import routes