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
| `Id` | `INT` | **Required**. Primary key auto incrementable |
| `Nombre` | `STRING` | **Required**. nombre del producto |
| `Precio` | `DOUBLE` | **Required**. Precio del producto |
| `Descripcion` | `LONGTEXT` | **Required**. Descripción del producto |
| `Ref` | `STRING` | **Opcional**. Referencia del producto |
| `Asset` | `STRING` | **Opcional**. Asset del producto |

#### Imagenes

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Id` | `INT` | **Required**. Primary key auto incrementable |
| `Img` | `LONGTEXT` | **Required**. Ruta de la imagen o base64 |

#### Categorias

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `INT` | **Required**. Primary key auto incrementable |
| `Nombre` | `STRING` | **Required**. Nombre de la categoria |

## Estructura de caperas

```bash
.
├── Doc
│   └── Img
│       └── Clase UML.jpeg
├── app
│   ├── Create
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates
│   │       └── crear_producto.html
│   ├── Detalles
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   └── main.css
│   │   └── templates
│   │       └── detalle_producto.html
│   ├── Index
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   ├── main.css
│   │   │   └── main.js
│   │   └── templates
│   │       └── index.html
│   ├── Modificar
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   └── main.css
│   │   └── templates
│   │       └── actualizar_producto.html
│   ├── Templates
│   │   └── templates
│   │       └── 404.html
│   ├── __init__.py
│   ├── assets
│   │   ├── img
│   │   │   ├── imagen1.jpg
│   │   │   ├── imagen2.jpg
│   │   │   └── imagen3.jpg
│   │   └── models
│   │       └── mesa_simple.glb
│   └── config
│       ├── __init__.py
│       └── development.py
├── db
│   └── script.sql
├── readme.md
├── requirements.txt
└── run.py
```

* asset : Guarda los archivos multimedia y recursos necesarios
* config : Configuraciones globales del sistema
* Index : Modulo principal de listar productos
* Create : Modulo de creacion de producto
* Modificar : Modulo de modificar producto
* Templates : Templates y archivos staticos para usar en casos particulares
* db : Scripts de la base de datos

# Criterios de evaluacion

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

# Ejecucion en local

## Python
* Python 3.10.12

### Dependencias

```bash
blinker==1.7.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
Flask==3.0.0
greenlet==3.0.1
idna==3.6
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
mysql-connector-python==8.2.0
protobuf==4.21.12
python-dotenv==1.0.0
requests==2.31.0
SQLAlchemy==2.0.23
typing_extensions==4.8.0
urllib3==2.1.0
Werkzeug==3.0.1
```

las puedes encontrar e instalar en [requirements.txt](./requirements.txt)

## Instalacion

`NOTA: Si usas windows tendras que instalar wsl(Windows Subsystem for Linux) su instalacion es facil por medio de la tienda de windows`

* [INSTALA WSL](https://www.microsoft.com/store/productId/9P9TQF7MRM4R?ocid=pdpshare)
* [INSTALA UBUNTU PARA WSL](https://www.microsoft.com/store/productId/9PN20MSR04DW?ocid=pdpshare)
* [DOCUMENTACION WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

### Comandos de instalacion

#### Clona el repositorio
```bash
git clone https://github.com/Dannkol/PruebaTecnicaFacilPost.git
```

#### Creacion del entorno virual
```bash
python3 -m venv .venv
```

#### Iniciamos el entorno virtual
```bash
. .venv/bin/activate
```
`NOTA: En caso de problemas instale el paquete virtualenv`

#### Instalacion de dependencias
```bash
pip install -r requirements.txt
```

#### Configuracion de la variables de entorno

Con el archivo [.env_example](./.env_example) crea un archivo .env y cambias las variables a tu necesidad

* DB_HOST : El host de la base de datos
* DB_USER : El usuario de la base de datos
* DB_PASSWORD : La contraseña de la base de datos
* DB_NAME : La nombre de la base de datos de la base de datos

#### Montar la base de datos

`NOTA: Version de MySQL : mysql  Ver 8.0.35-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))`

Con el archivo [db/script.sql](db/script.sql) puedes crear la base de datos, copy y pega en la terminal sql o trata de usar este comando  desde el directorio raiz del proyecto

```bash
mysql -u root -p < db/script.sql
```

#### Ejecucion

Una vez realizados todos los pasos tienes que ejecutar el siguiente comendo desde la raiz del proyecto
```bash
python3 run.py
```

# Manual de uso

* VIDEO TUTORIAL : https://drive.google.com/file/d/1H7lsC_8PLpZc-sn56dWbtKOfAwFcLmAK/view?usp=sharing
