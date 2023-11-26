from . import Index_create
import os
import secrets
from flask import render_template, redirect, url_for, request, jsonify, current_app
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
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
    return render_template('crear_producto.html', categorias=categorias)

@Index_create.route('/agregar_producto', methods=['GET','POST'])
def agregar_producto():

    if request.method != 'POST':
        return redirect('/crear_producto')

    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    descripcion = request.form['descripcion']
    ref = request.form['ref']
    categorias = request.form.getlist('categorias[]')


    # Carpeta para guardar las imágenes
    img_folder = os.path.join(current_app.config['APP_FOLDER'], current_app.config['ASSETS_FOLDER'], 'img')
    os.makedirs(img_folder, exist_ok=True)

    # Carpeta para guardar los modelos 3D
    models_folder = os.path.join(current_app.config['APP_FOLDER'], current_app.config['ASSETS_FOLDER'], 'models')
    os.makedirs(models_folder, exist_ok=True)



    # Guardar imágenes
    imagenes = []
    for imagen in request.files.getlist('imagenes[]'):
        filename = secrets.token_hex(16) + secure_filename(imagen.filename)
        img_path = os.path.join(img_folder, filename)
        imagen.save(img_path)
        imagenes.append(filename)
    
    # Guardar modelos 3D
    asset = None
    if request.files.getlist('asset[]') and request.files.getlist('asset[]')[0].read().strip():
        # Verificar si hay archivos y el valor no está en blanco
        for modelo in request.files.getlist('asset[]'):
            filename = secrets.token_hex(16) + secure_filename(modelo.filename)
            model_path = os.path.join(models_folder, filename)
            modelo.save(model_path)
            print(model_path)
            asset = filename

    print(
        nombre,
        precio,
        descripcion,
        ref,
        asset,
        categorias,
        imagenes
    )

        # Conectar a la base de datos
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Insertar el nuevo producto en la tabla Productos
        if asset is None:
            cursor.execute(
                "INSERT INTO Productos (Nombre, Precio, Descripcion, Ref) VALUES (%s, %s, %s, %s)",
                (nombre, precio, descripcion, ref)
            )
        else:
            cursor.execute(
                "INSERT INTO Productos (Nombre, Precio, Descripcion, Ref, Asset) VALUES (%s, %s, %s, %s, %s)",
                (nombre, precio, descripcion, ref, asset)
            )

        product_id = cursor.lastrowid # Obtener el ID del producto insertado
        print(product_id)
        # Insertar las categorías en la tabla Categorias_de_Productos
        for categoria_id in categorias:
            cursor.execute(
                "INSERT INTO Categorias_de_Productos (Id_Categoria, Id_Productos) VALUES (%s, %s)",
                (categoria_id, product_id)
            )

        # Insertar las imágenes en la tabla Imagenes_de_Productos
        for img_filename in imagenes:
            img_path = "img/{}".format(img_filename)
            cursor.execute(
                "INSERT INTO Imagenes (Img) VALUES (%s)",
                (img_path,)
            )
            img_id = cursor.lastrowid
            cursor.execute(
                "INSERT INTO Imagenes_de_Productos (Id_Img, Id_Productos) VALUES (%s, %s)",
                (img_id, product_id)
            )

        # Commit para guardar los cambios en la base de datos
        connection.commit()

    except Exception as e:
        print(f"Error al insertar en la base de datos: {str(e)}")
        # Manejar el error como desees

    finally:
        # Cerrar la conexión
        cursor.close()
        connection.close()
    
    return redirect('/crear_producto')