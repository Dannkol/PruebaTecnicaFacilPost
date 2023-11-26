from . import Index_create
import os
from flask import render_template, redirect, url_for, request, jsonify
import requests
from ..config import DevelopmentConfig
import mysql.connector

# Función para conectar a la base de datos
def connect_to_database():
    from .. import app
    return mysql.connector.connect(
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST'],
        database=app.config['DB_NAME']
    )

@Index_create.route('/crear_producto', methods=['GET'])
def index():
    categorias = []

    try:
        # Intentar establecer una conexión y realizar una operación simple en la base de datos
        connection = connect_to_database()
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM Categorias;") 
        results = cursor.fetchall() 
        for result in results:
            categorias.append({
                'Id': result[0],
                'NombreCategoria': result[1]
            })
    except Exception as e:
        print(str(e))
        categorias.append('error')
    finally:
        cursor.close()
        connection.close()
    print(type(categorias), categorias)
    return render_template('crear_producto.html', categorias=categorias)