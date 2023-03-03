# Task Manager

## Link proyecto en servidor:
  - http://159.89.53.143

## Instalación:

#### Crear ambiente virtual
  - python -m venv env

#### Activar ambiente virtual:
  - .env\Scripts\activate

### Instalar requerimientos:
  - pip install -r requirements.txt
  
### Crear archivo llamado .env y agregar la siguiente informacion:
  - DATABASE_NAME= nombre de la base de datos
  - DATABASE_USER= usuario para la base de datos
  - DATABASE_PASSWORD= contraseña de el usuario ingresado
  
### Crear migraciones:
  - python manage.py migrate
 
### Ejecutar servidor:
  - python manage.py runserver

<p align="left">
<img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
</p>
