from flask import Flask , render_template , send_from_directory
import os
# Blueprints
from .Index import Index

# Modulos de configuracion
from .config import DevelopmentConfig

import mysql.connector


app = Flask(__name__, template_folder='Templates', static_folder='Templates/static')

# Registro de blueprints
app.register_blueprint(Index)


app.config.from_object(DevelopmentConfig)

# Configuración de rutas estaticas
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['ASSETS_FOLDER'] = 'assets'
app.config['ASSETS_STATIC_FOLDER'] = 'static'

# Manejo de errores
@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(error):
    return render_template('templates/404.html'), 404


@app.route('/assets/<path:filename>')
def assets_static(filename):
    return send_from_directory(app.config['ASSETS_FOLDER'], filename)