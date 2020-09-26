# EGC

### 1. Descargar los datos

Ingresa a: https://www.kaggle.com/shayanfazeli/heartbeat y descarga los archivos .csv

Crea una carpeta llamada data y pega los archivos descargados dentro de ella

### 2. Preparando el entorno

- Instalar conda junto con sus librerias

`conda create --name <env> --file <this file>`

O sea:

**Linux:**

`conda create --name EGC --file requirements.txt`

### 3. Corriendo el proyecto

1. Exportar la variable 

`export FLASK_APP=main.py`

2. Te mueves dentro de la carpeta src

`cd src`

3. Correr flask

`flask run`

