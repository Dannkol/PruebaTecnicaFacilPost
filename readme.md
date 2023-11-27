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
mysql -u [USUARIO] -p < db/script.sql
```

#### Ejecucion

Una vez realizados todos los pasos tienes que ejecutar el siguiente comendo desde la raiz del proyecto
```bash
python3 run.py
```

# Manual de uso

* VIDEO TUTORIAL : https://drive.google.com/file/d/1H7lsC_8PLpZc-sn56dWbtKOfAwFcLmAK/view?usp=sharing

# Cuestionario

## ¿Qué frameworks y librerías de Python ha utilizado en proyectos? ¿Cuáles recomendaría para desarrollo de AI y Apis Rest?

Utilece Flask 3.0.0 como framework principal, Python 3.10.12 y mysql  Ver 8.0.35-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))

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

### Recomendaciones para desarrollo de AI y APIs REST

Para el desarrollo de APIs REST, recomiendo utilizar Flask o Django. Ambos frameworks son fáciles de aprender y utilizar, y ofrecen una amplia gama de funciones para crear APIs RESTful seguras y escalables.

Para el desarrollo de AI, recomiendo utilizar TensorFlow o PyTorch. Ambas librerías ofrecen una amplia gama de algoritmos y funciones para tareas comunes de aprendizaje automático, y son utilizadas por investigadores y desarrolladores de todo el mundom, tambien podemos usar plataformas como Hugging Face, muy populares y competentes en NPL y ML, esto gracias su librearia de transformers, Hugging Face tambien nos ofrece una forma sencilla de ejecutar modelos preentrenados y un catalogo de estos mismo compartidos por la comunidad.

* [PyTorch](https://pytorch.org)
* [TensorFlow](https://www.tensorflow.org)
* [Hugging Face](https://huggingface.co/docs)

## ¿Cómo maneja las dependencias y entornos virtuales en Python? ¿Ha utilizado virtualenv, o similares?

Manejar dependencias y entornos virtuales en Python es esencial para un desarrollo eficaz. Utilizo el comando `python3 -m venv .venv` para crear un entorno virtual para cada proyecto. Esto me permite aislar las dependencias de cada proyecto, lo que facilita la resolución de problemas y la portabilidad.

También he utilizado virtualenv en el pasado como `Conda`.

## ¿Cómo realiza el control de versiones en sus proyectos Python? ¿Está familiarizado con Git y GitHub?

Siempre uso git y github para el control de versiones en mi proyecto, esto muy familiarizado con Git y GitHub, llevo màs de un año usandolo y siguiendo estandares como conventional commits o MIT

## ¿Qué aproximación utiliza para manejar excepciones y errores en Python? ¿Podría dar un ejemplo?

* Evitar errores en primer lugar. Esto se puede hacer escribiendo código claro y conciso, y usando las funciones y métodos adecuados.
* Manejar las excepciones que se producen. Para ello, utilizo bloques try-except para capturar las excepciones y tomar medidas para solucionarlas o informar de ellas.
* Registrar los errores que se producen. Esto puede ayudar a diagnosticar y solucionar los problemas.

```python
@Index.route('/', methods=['GET'])
def index():
    img_urls = []

    try:
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
```
El bloque except captura cualquier excepción que se produzca durante la ejecución del bloque try. Si se produce una excepción, se imprime el error en la consola y se agrega el mensaje 'error' a la lista de URL de imágenes.

El bloque finally se ejecuta siempre, independientemente de si se produce una excepción o no. En el bloque finally, se cierran el cursor y la conexión a la base de datos para liberar los recurso.

## ¿Cómo se implementa la programación orientada a objetos en Python? ¿Podría dar un ejemplo de clases y herencia?

La programación orientada a objetos (POO) es un paradigma de programación que organiza el código en torno a objetos. Los objetos son unidades de código que tienen datos y comportamientos asociados.

En Python, la POO se implementa mediante el uso de clases. Las clases son plantillas que definen los datos y comportamientos de un objeto.

Crear un clase Figura en python
```python
class Figura:
    def __init__(self, color):
        self.color = color

    def dibujar(self):
        print("Dibujando una figura de color {}.".format(self.color))
```
Creamos una clase hija o una clase que herede de la clase Figura
```python
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado
```
En este ejemplo, la clase Figura es la clase base. La clase Cuadrado hereda de la clase Figura.

La clase Cuadrado tiene un atributo adicional, lado, y un método adicional, calcular_area(). El método calcular_area() calcula el área del cuadrado.

```python
cuadrado = Cuadrado("azul", 10)

cuadrado.dibujar() 
# Imprime "Dibujando una figura de color azul."

print(cuadrado.calcular_area())
# Imprime 100
```

## ¿Cómo trabaja con bases de datos en Python? ¿Ha utilizado ORM como SQLAlchemy?

En este proyecto uso mysql-connector-python para trabajar con una base de datos mysql  Ver 8.0.35-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu)).

Enteriormente he usado ORM como sequelize y eloquent para bases de datos SQL en javascript y php correspondientemente y mongoose para MongoDB en javascript.

## ¿Cuál ha sido el proyecto Python más complejo que ha desarrollado?

Actualmente mis proyectos más complejos en python son script para el uso de LLM como llama2, normalmente python lo suelo usar para creacion de script para automatizar tareas o calculos.

## ¿Cómo analiza y mejora el performance de queries SQL generadas por el ORM de Python? ¿Conoce técnicas para optimizar consultas SQL?

No he usado ORM en Python pero si conozco tecnicas de optimizacion de consultas SQL como por ejemplo

* Limita la cantidad de datos recuperados:

    SELECT para recuperar solo las columnas necesarias.
    
    LIMIT para limitar la cantidad de filas devueltas.

* Optimiza las cláusulas WHERE
* Evita el uso excesivo de JOINs
* Evita las subconsultas innecesarias
* Utiliza almacenamiento en caché:

    Almacenar resultados de consultas frecuentes y evitar la necesidad de ejecutar la misma consulta repetidamente.

## ¿Cómo consume e integra API de terceros en aplicaciones Python? ¿Utiliza bibliotecas como Requests o aiohttp? ¿Puede describir el proceso?

En este caso no se usaron apis de terceros, pero este es un ejemplo de consumo de api con python3 usando Requests

```python
import requests

def obtener_informacion_pokemon(nombre_pokemon):
    url_api = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    
    # Realizar la solicitud GET a la API
    respuesta = requests.get(url_api)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta a formato JSON
        datos_pokemon = respuesta.json()

        # Imprimir información relevante
        print(f"Nombre: {datos_pokemon['name']}")
        print(f"ID: {datos_pokemon['id']}")
        print(f"Tipos: {', '.join(tipo['type']['name'] for tipo in datos_pokemon['types'])}")
        print(f"Altura: {datos_pokemon['height']}")
        print(f"Peso: {datos_pokemon['weight']}")
    else:
        print(f"Error al obtener la información. Código de respuesta: {respuesta.status_code}")

# Ejemplo de uso para el Pokemon 'Ditto'
nombre_pokemon_ejemplo = 'ditto'
obtener_informacion_pokemon(nombre_pokemon_ejemplo)
```
Resultado
```bash
Nombre: ditto
ID: 132
Tipos: normal
Altura: 3
Peso: 40
```

## Si encuentra un error difícil de resolver en Python, ¿cuál suele ser su enfoque para depurarlo y encontrar una solución?

* Primero reviso los logs para estudiar bien el error y tener algo para realizar un busqueda de la solucion en Internet.

* Realizo depuracion en el codigo por medio de print, esto me ayuda a ralizar un seguimiento e identificar en que parte se encuentra el error

* Busqueda en documentacion oficion, muchas veces se suele tener problemas con las dependencias y en la documentacion oficial o foros de la misma se suele encontrar la solucion facilmente

* Antes de realizar una busqueda avanzada, ya con la informacion recopilada redacto un prompt para que la IA como bard o chatGPT me de mas informacion o una posible solucion

* Busqueda avanzada en internet y preguntas en comunidad

## ¿Cuáles son los próximos temas o tecnologías de Python que tiene interés en aprender como desarrollador junior?

Me encuentro estudiando python para ciencia de datos e inteligencia artificial, esos dos son mis temas de interes en python

## ¿Si tuviera que explicar Python a un desarrollador que solo ha trabajado con lenguajes compilados, qué analogías usaría?

Se suele compara a python saber ingles, esto porque es un lenguaje facil de entender y aprender, si sabes ingles ya sabes mas del 80% del lenguaje esta es la analogia que usaria, tambien explicaria que apesar de ser amigable o sencillo es uno de los lenguajes mas usados y completos, con el puedes crear todo lo que te imagines