# Prueba tecnica python

# Investigacion

## [Blueprints](https://flask.palletsprojects.com/es/latest/blueprints/)

En el contexto de una aplicación Flask, la arquitectura de blueprints se refiere a la capacidad de organizar y estructurar tu aplicación en módulos más pequeños y reutilizables. Los blueprints permiten dividir una aplicación Flask grande en partes más manejables, lo que facilita la colaboración, el mantenimiento y la escalabilidad del código.

Un "blueprint" en Flask es esencialmente un conjunto de operaciones que pueden incluir rutas, controladores (funciones de vista), modelos y archivos estáticos. Al utilizar blueprints, puedes dividir tu aplicación en módulos lógicos y luego registrar esos módulos en la aplicación principal. Esto mejora la modularidad y facilita la comprensión del código

## Base de datos

![Descripción de la imagen](/Doc/Img/Clase%20UML.jpeg)

#### Productos

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `INT` | **Required**. Primary key auto incrementable |
| `nombre` | `STRING` | **Required**. nombre del producto |
| `Precio` | `DOUBLE` | **Required**. Precio del producto |
| `Descripcion` | `LONGTEXT` | **Required**. Descripción del producto |
| `Ref` | `STRING` | **Opcional**. Referencia del producto |
| `Asset` | `STRING` | **Opcional**. Asset del producto |

#### Imagenes

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `INT` | **Required**. Primary key auto incrementable |
| `Img` | `LONGTEXT` | **Required**. Ruta de la imagen o base64 |

#### Categorias

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `INT` | **Required**. Primary key auto incrementable |
| `Nombre` | `STRING` | **Required**. Nombre de la categoria |

## Estructura de caperas

```bash
.
├── app
│   ├── assets
│   ├── config
│   │   ├── development.py
│   │   └── __init__.py
│   ├── Index
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   ├── main.css
│   │   │   └── main.js
│   │   └── templates
│   │       └── index.html
│   ├── __init__.py
│   └── Templates
│       ├── static
│       └── templates
│           └── 404.html
├── readme.md
├── requirements.txt
└── run.py
```

* asset : Guarda los archivos multimedia y recursos necesarios
* config : Configuraciones globales del sistema

Dentro de app se encontraran los blueprints o modulos de la aplicacion divididos por los puntos evatualuativos de la prueba que son los siguiente

1. Página Principal:
    - Mostrar una tabla con los productos.
    - Mostrar botones para "Ver," "Modificar" y "Eliminar" cada producto en la tabla.
    - Incluir un botón para "Agregar nuevo producto."

2. Agregar Producto:
    - Al hacer clic en el botón "Agregar nuevo producto," mostrar un formulario con
    campos para ingresar información sobre un nuevo producto (nombre,
    descripción, precio, etc.).
    - Al enviar el formulario, el nuevo producto debe ser almacenado en la base de
    datos y visible en la página principal.

3. Ver Producto:
    - Al hacer clic en el botón "Ver" junto a un producto en la tabla, mostrar una
    página o modal con detalles del producto.

4. Modificar Producto:
    - Al hacer clic en el botón "Modificar" junto a un producto en la tabla, permitir al
    usuario editar la información del producto y guardar los cambios en la base
    de datos.

5. Eliminar Producto:
    - Al hacer clic en el botón "Eliminar" junto a un producto en la tabla, se elimina
    el producto de la base de datos