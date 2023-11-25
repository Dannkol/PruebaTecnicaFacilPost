from flask import Blueprint


Index = Blueprint('Index', __name__, template_folder='templates', static_folder='static')

from . import routes