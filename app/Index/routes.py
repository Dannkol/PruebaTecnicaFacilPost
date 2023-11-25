from . import Index
from flask import render_template, redirect, url_for, request, jsonify
from ..config import DevelopmentConfig
import mysql.connector

@Index.route('/')
def index():
    return render_template('index.html')

# Función para conectar a la base de datos
def connect_to_database():
    from .. import app
    return mysql.connector.connect(
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST'],
        database=app.config['DB_NAME']
    )

@Index.route('/test_db_connection')
def test_db():  
    try:
        # Intentar establecer una conexión y realizar una operación simple en la base de datos
        connection = connect_to_database()
        cursor = connection.cursor() # El cursor se utiliza para ejecutar comandos SQL en la base de datos.
        cursor.execute("SELECT 1") # Ejecución de SQL
        result = cursor.fetchone() # Se utiliza el método fetchone() para recuperar el resultado de la consulta
        message = f"La conexión a la base de datos es exitosa. Resultado: {result}" # Template literal
    except Exception as e:
        message = f"Error de conexión a la base de datos: {str(e)}"
    finally:
        cursor.close() # El cursor se finaliza
        connection.close() # Se finaliza la conexión

    return jsonify({'message': message}) # respuesta en formato json