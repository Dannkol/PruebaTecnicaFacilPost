from . import Index_Detalles
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

@Index_Detalles.route('/detalle_producto/<int:producto_id>', methods=['GET'])
def detalle_producto(producto_id):
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
        print(producto_result)
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
            print(categorias_result)
            categorias_producto = [categorias[0] for categorias in categorias_result]

            # Agrega la lista de rutas de imágenes al diccionario de detalles del producto
            detalle_producto['Categorias'] = categorias_producto

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

    # Renderiza la plantilla de detalle_producto.html con la información del producto
    return render_template('detalle_producto.html', data=detalle_producto)
