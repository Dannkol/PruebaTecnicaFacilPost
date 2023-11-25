from flask import Flask , render_template
# Blueprints
from .Index import Index

# Modulos de configuracion
from .config import DevelopmentConfig

import mysql.connector


app = Flask(__name__, template_folder='Templates', static_folder='Templates/static')

# Registro de blueprints
app.register_blueprint(Index)


app.config.from_object(DevelopmentConfig)

# Configuración de la carpeta de plantillas
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Manejo de errores
@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(error):
    return render_template('templates/404.html'), 404