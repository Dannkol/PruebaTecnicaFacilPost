from flask import Blueprint


Index_Detalles = Blueprint('Index_Detalles', __name__, template_folder='templates', static_folder='static', static_url_path='/Detalles')

from . import routes