from flask import Blueprint


Index_Modificar = Blueprint('Index_Modificar', __name__, template_folder='templates', static_folder='static', static_url_path='/Modificar')

from . import routes