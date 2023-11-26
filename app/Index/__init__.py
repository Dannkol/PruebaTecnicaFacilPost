from flask import Blueprint


Index = Blueprint('Index', __name__, template_folder='templates', static_folder='static', static_url_path='/Index')

from . import routes