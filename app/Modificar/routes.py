from . import Index_Modificar
import os
import secrets
from flask import render_template, redirect, url_for, request, jsonify, current_app
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import requests
from ..config import DevelopmentConfig
import mysql.connector

def connect_to_database():
    from .. import app
    return mysql.connector.connect(
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST'],
        database=app.config['DB_NAME']
    )

@Index_Modificar.route('/borrarimg/<string:path>/<int:producto_id>', methods=['GET', 'POST'])
def borrarimg(path,producto_id):
    print(path,producto_id)
    query = f"img/{path}"
    try :
        connection = connect_to_database()
        cursor = connection.cursor() 
        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' ,'assets','img',path)
        os.remove(img_path)
        cursor.execute("DELETE FROM Imagenes WHERE Img = %s;",(query,))
        connection.commit()
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        connection.close()
    return redirect( url_for('Index_Modificar.actualizar_producto', producto_id=producto_id))

@Index_Modificar.route('/borrarmodelo/<string:path>/<int:producto_id>', methods=['GET', 'POST'])
def borrarmodelo(path,producto_id):
    print(path,producto_id)
    try :
        connection = connect_to_database()
        cursor = connection.cursor() 
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' ,'assets','models',path)
        os.remove(model_path)
        cursor.execute("UPDATE Productos SET Asset = NULL WHERE Id = %s;",(producto_id,))
        connection.commit()
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        connection.close()
    return redirect( url_for('Index_Modificar.actualizar_producto', producto_id=producto_id))

@Index_Modificar.route('/actualizar_producto/<int:producto_id>', methods=['GET', 'POST'])
def actualizar_producto(producto_id):
    if request.method == 'GET':
        # Obtener los detalles del producto desde la base de datos
        try:
            # Intenta establecer una conexión y obtener los detalles del producto por su ID
            connection = connect_to_database()
            cursor = connection.cursor() 

            # Realiza la consulta para obtener los detalles del producto
            cursor.execute(
                "SELECT Productos.Id, Productos.Nombre, Productos.Precio, Productos.Descripcion, Productos.Ref, Productos.Asset "
                "FROM Productos "
                "WHERE Productos.Id = %s",
                (producto_id,)
            )
            producto_result = cursor.fetchone()
            if producto_result:
                # Si se encontró el producto, construye un diccionario con los detalles básicos
                detalle_producto = {
                    'Id': producto_result[0],
                    'Nombre': producto_result[1],
                    'Precio': producto_result[2],
                    'Descripcion': producto_result[3],
                    'Ref': producto_result[4],
                    'Asset': url_for('assets_static', filename=producto_result[5]) if producto_result[5] != None else None  
                }

                # Realiza la consulta para obtener todas las imágenes del producto
                cursor.execute(
                    "SELECT Imagenes.Img "
                    "FROM Imagenes_de_Productos "
                    "JOIN Imagenes ON Imagenes_de_Productos.Id_Img = Imagenes.Id "
                    "WHERE Imagenes_de_Productos.Id_Productos = %s",
                    (producto_id,)
                )
                imagenes_result = cursor.fetchall()

                # Construye una lista de rutas de imágenes asociadas al producto
                imagenes_producto = [url_for('assets_static', filename=img[0]) for img in imagenes_result]

                # Agrega la lista de rutas de imágenes al diccionario de detalles del producto
                detalle_producto['Imagenes'] = imagenes_producto

                # Realiza la consulta para obtener todas las Categorias del producto
                cursor.execute(
                    "SELECT Categorias.Nombre "
                    "FROM Categorias_de_Productos "
                    "JOIN Categorias ON Categorias_de_Productos.Id_Categoria = Categorias.id "
                    "WHERE Categorias_de_Productos.Id_Productos = %s",
                    (producto_id,)
                )
                categorias_result = cursor.fetchall()

                # Construye una lista de rutas de imágenes asociadas al producto
                categorias_producto = [categorias[0] for categorias in categorias_result]

                # Agrega la lista de rutas de imágenes al diccionario de detalles del producto
                detalle_producto['Categorias'] = categorias_producto

                cursor.execute("SELECT * FROM Categorias")
                categoriasall_result = cursor.fetchall()
                print([categorias for categorias in categoriasall_result])

                detalle_producto['CategoriasAll'] = [categorias for categorias in categoriasall_result]

            else:
                # Si no se encontró el producto, puedes manejar este caso según tus necesidades
                detalle_producto = None

        except Exception as e:
            print(str(e))
            detalle_producto = None

        finally:
            cursor.close()
            connection.close()

        print(detalle_producto)

        # Renderizar el formulario con los detalles del producto
        return render_template('actualizar_producto.html', producto=detalle_producto)

    elif request.method == 'POST':
        # Procesar el formulario de actualización

        # Obtener los nuevos datos del formulario
        nuevo_nombre = request.form['nombre']
        nuevo_precio = float(request.form['precio'])
        nueva_descripcion = request.form['descripcion']
        nueva_ref = request.form['ref']
        nuevas_categorias = request.form.getlist('categorias[]')

        # Carpeta para guardar las imágenes
        img_folder = os.path.join(current_app.config['APP_FOLDER'], current_app.config['ASSETS_FOLDER'], 'img')
        os.makedirs(img_folder, exist_ok=True)

        # Carpeta para guardar los modelos 3D
        models_folder = os.path.join(current_app.config['APP_FOLDER'], current_app.config['ASSETS_FOLDER'], 'models')
        os.makedirs(models_folder, exist_ok=True)

        print(request.files.getlist('imagenes[]')[0].filename)
        imagenes = []

        if 'imagenes[]' in request.files and request.files.getlist('imagenes[]')[0].filename:
            for imagen in request.files.getlist('imagenes[]'):
                filename = secrets.token_hex(16) + secure_filename(imagen.filename)
                img_path = os.path.join(img_folder, filename)
                imagen.save(img_path)
                imagenes.append(filename)

        # Guardar modelos 3D
        asset = None
        if 'asset' in request.files and request.files['asset']:
            modelo = request.files['asset']
            filename = secrets.token_hex(16) + secure_filename(modelo.filename)
            model_path = os.path.join(models_folder, filename)
            modelo.save(model_path)
            print(model_path)
            asset = filename

        print(
            nueva_descripcion,
            nueva_ref,
            nuevo_nombre,
            nuevo_precio,
            nuevas_categorias,
            imagenes,
            asset
        )
        # Actualizar la base de datos con los nuevos datos
        connection = connect_to_database()
        cursor = connection.cursor()

        try:
            # Actualizar el producto en la tabla Productos
            if asset is None:
                cursor.execute(
                    "UPDATE Productos SET Nombre = %s, Precio = %s, Descripcion = %s, Ref = %s WHERE Id = %s",
                    (nuevo_nombre, nuevo_precio, nueva_descripcion, nueva_ref, producto_id)
                )
            else:
                asset_path = "models/{}".format(asset)
                cursor.execute(
                    "UPDATE Productos SET Nombre = %s, Precio = %s, Descripcion = %s, Ref = %s, Asset = %s WHERE Id = %s",
                    (nuevo_nombre, nuevo_precio, nueva_descripcion, nueva_ref, asset_path, producto_id)
                )
            # Eliminar las categorías existentes del producto en la tabla Categorias_de_Productos
            cursor.execute("DELETE FROM Categorias_de_Productos WHERE Id_Productos = %s", (producto_id,))

            # Insertar las nuevas categorías en la tabla Categorias_de_Productos
            for categoria_id in nuevas_categorias:
                cursor.execute(
                    "INSERT INTO Categorias_de_Productos (Id_Categoria, Id_Productos) VALUES (%s, %s)",
                    (categoria_id, producto_id)
                )

            # Insertar las nuevas imágenes en la tabla Imagenes
            for img_filename in imagenes:
                img_path = "img/{}".format(img_filename)
                cursor.execute(
                    "INSERT INTO Imagenes (Img) VALUES (%s)",
                    (img_path,)
                )
                img_id = cursor.lastrowid

                # Insertar las nuevas imágenes en la tabla Imagenes_de_Productos
                cursor.execute(
                    "INSERT INTO Imagenes_de_Productos (Id_Img, Id_Productos) VALUES (%s, %s)",
                    (img_id, producto_id)
                )

            # Commit para guardar los cambios en la base de datos
            connection.commit()

        except Exception as e:
            print(str(e))
            detalle_producto = None

        finally:
            cursor.close()
            connection.close()
        # Redirigir a la página de detalles del producto actualizado
        return redirect( url_for('Index_Modificar.actualizar_producto', producto_id=producto_id))