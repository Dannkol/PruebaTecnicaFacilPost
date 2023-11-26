from . import Index
import os
from flask import render_template, redirect, url_for, request, jsonify
import requests
from ..config import DevelopmentConfig
import mysql.connector

# Borrar producto seleccionado
@Index.route('/borrar/<int:producto_id>', methods=['GET', 'POST'])
def borrar_producto(producto_id):
    try:
        # Intenta establecer una conexión y borrar el producto según su ID
        connection = connect_to_database()
        cursor = connection.cursor() 
        cursor.execute(f"SELECT Asset FROM Productos WHERE Id = {producto_id};")
        asset_model_path = cursor.fetchone()[0] # optiene el path de la modelo a borrar
        cursor.execute(f"SELECT Img FROM Imagenes_de_Productos JOIN Imagenes ON Imagenes_de_Productos.Id_Img = Imagenes.Id WHERE Id_Productos = {producto_id};")
        asset_img_path = cursor.fetchone()[0]  # optiene el path del imagen a borrar
        cursor.execute(f"DELETE FROM Productos WHERE Id = {producto_id};")

        # Borra el modelo y la imagen
        if asset_model_path:
            model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' ,'assets',asset_model_path)
            os.remove(model_path)
        if asset_img_path:
            img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' ,'assets',asset_img_path)
            print("path:", os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' ,'assets',asset_img_path))
            os.remove(img_path)

        connection.commit()
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        connection.close()
    
    # Redirige de vuelta a la página principal después de borrar
    return redirect(url_for('Index.index'))

# Vista principal
@Index.route('/', methods=['GET'])
def index():
    img_urls = []

    try:
        # Intentar establecer una conexión y realizar una operación simple en la base de datos
        connection = connect_to_database()
        cursor = connection.cursor() 
        cursor.execute("SELECT Productos.Id AS id, Productos.Nombre AS NombreProducto, Productos.Precio, MIN(Imagenes.Img) AS RutaImagen FROM Productos JOIN Imagenes_de_Productos ON Productos.Id = Imagenes_de_Productos.Id_Productos JOIN Imagenes ON Imagenes_de_Productos.Id_Img = Imagenes.Id GROUP BY Productos.Id;") 
        results = cursor.fetchall() 
        for result in results:
            img_urls.append({
                'Id': result[0],
                'NombreProducto': result[1],
                'Precio': result[2],
                'RutaImagen': url_for('assets_static', filename=result[3])
            })
    except Exception as e:
        print(str(e))
        img_urls.append('error')
    finally:
        cursor.close() # El cursor se finaliza
        connection.close() # Se finaliza la conexión
    return render_template('index.html', img_url=img_urls)

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