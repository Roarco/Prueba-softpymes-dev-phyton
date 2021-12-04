# API Python Flask
API Test SoftPymes, cuenta con manejo de excepciones, manejo de base de datos MySQL
está desarrollada en lenguaje Python, con framework Flask y ORM SqlAlchemy.

## Tiempo de la prueba
La prueba esta estimada en un tiempo de 30 minutos y un tiempo máximo no superior a 1 hora.

## Requerimientos
Para ejecutar el proyecto, se requiere tener instalados:
- Python versiones 3 (superiores a la 3.6) 
- virtualenv 
- IDE pycharm (opcional, pero cualquier IDE te sirve, ejemplo: VSCODE)
- POSTMAN (Para realizar pruebas de los endpoint)
- Gestor de Base de Batos (MySQL)

## Instalación
Para la instalación de recursos, se debe tener en cuenta los siguientes pasos:

### Creación del Entorno
Para la creación del entorno virtual se deben ejecutar los siguientes comandos
en la raíz del proyecto:
```
python -m venv venv
```
> NOTA: el comando python dependen de la versión de python instalada en tu equipo,
> ejemplo: si tienes python 3.7.9 instalado el comando seria python3.7.9 -m venv venv
> ó python3 -m venv venv con cualquiera de las dos opciones te debe crear el entorno virtual

### Instalar Requerimientos

La aplicación ya tiene las librerías necesarias para el desarrollo de la prueba, solo
es ejecutar los siguientes comandos en la raíz del proyecto:

```
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

> NOTA: Es libre de instalar las librerías que desee para dar solución a la prueba, pero tenga en cuenta
> el tiempo limite de la prueba

### Importar la Base de Datos
Para importar la base de datos, hacer uso del script ```softpymes_test.sql``` que se encuentra en la raíz del proyecto

> **Nota:** dentro de la carpeta ```api``` existe un archivo llamado ```.env``` este archivo
> tiene la configuración para conectarse a la base de datos, modificarlo según las preferencias
> de sus equipos.

### Ejecutar API
Los comandos a continuación permitirán la ejecución de la API
```
cd api
python run.py
```

### Probar la API - POSTMAN
Entre los archivos, se deja un endpoint o servicio de test, para que validen el funcionamiento del API.
```
http://127.0.0.1:5000/api/v1/index
```
> NOTA: tener en cuenta que todas las rutas que usted cree, para poder consultarlas por medio de postman
> debe hacerlo agregándolas después de http://127.0.0.1:5000/api/v1/ <- aquí viene su ruta o endpoint o servicio

# Objetivo de la prueba

La prueba consiste en realizar un CRUD completo para el módulo de Example,
para lo cual se divide la prueba en los siguientes puntos:

1. Se require CONSULTAR todos los registros de la tabla de manera paginada
   y consultar por cualquier criterio de búsqueda
   (Tener en cuenta que se pide consultar por página, por N cantidad de registros
   y por cualquier criterio de búsqueda que usted desee).
2. Se require GUARDAR un registro en la tabla.
3. Se requiere ACTUALIZAR la información de un registro específico.
4. Se require ELIMINAR un registro específico.

> Nota: Tener en cuenta que las peticiones se hacen enviando y recibiendo objetos JSON

## Criterios de aceptación

Con el objetivo de validar el conocimiento y cumplimiento de los puntos mencionados anteriormente,
los criterios que se evaluarán son los siguientes:

1. Implementación de buenas prácticas
2. Validaciones de posibles errores, tanto de código como en el resultado de las consultas
3. La forma de responder una vez se consulten los endpoint o servicios que se crearán para consumir él API
4. Creatividad enfocada a la forma de solucionar cada uno de los puntos de la prueba, las respuestas del API

# Información de importante
Una vez terminada la prueba, debe crear un repositorio con su cuenta personal de git en (GitHub o GitLab o bitbucket) de manera público y,
enviar un correo con el link del repositorio que contiene la prueba, tener en cuenta que solo se aceptara el envio de la prueba, de la manera
mencionada anteriormente, para validar su conocimiento en consumo de APIs, se requiere que envien el json de la collection que genera POSTMAN,
importante tener en cuenta que este archivo debe ir en la raíz del proyecto que suba a su repositorio.

El correo debe tener los siguientes datos:

- Enviar la prueba al correo: lmelo@softpymes.com.co
- Asunto: Test SoftPymes - Backend Python
- Mensaje: En el mensaje agregar su nombre completo, además de sus conclusiones de la prueba, como se sintió, 
  que problemas se le presentaron y demás que desee contarnos.
  
> NOTA: En caso de tener una pregunta o requiera ayuda con un tema específico (no incluye solución de la prueba), 
> no dude en enviar un mensaje y este será respondido lo más pronto posible


