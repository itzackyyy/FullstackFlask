from flask import Flask, render_template, redirect, request, Response, session, jsonify
from livereload import Server as sv
import pymysql as sqlxd
import os
from werkzeug.security import generate_password_hash
from flask_cors import CORS


# #Información de login hacia la base de datos.
# DB_CONFIG = {
#     'host': os.getenv('DB_HOST', '127.0.0.1'),
#     'user': os.getenv('DB_USER','lore_user'),
#     'password': os.getenv('DB_PASS','LoreDB12$'),
#     'database': os.getenv('DB_NAME','lorepedia_db'),
#     'cursorclass': sqlxd.cursors.DictCursor,
#     'charset': 'utf8mb4'
# }

#Conexión hacia la base de datos desde Flask hacia MySQL
# def db_con():
#     return sqlxd.connect(
#         host=DB_CONFIG['host'],
#         user=DB_CONFIG['user'],
#         password=DB_CONFIG['password'],
#         database=DB_CONFIG['database'],
#         cursorclass=DB_CONFIG['cursorclass'],
#         charset=DB_CONFIG['charset']
#     )



app=Flask(__name__)
CORS(app)

@app.route('/login')#endpoint login
def login():
    return render_template('lorepedia/iniciarSesion.html')

@app.route('/registrar')#endpoint para registrar
def registrar():
    return render_template('lorepedia/crearSesion.html')




@app.route('/') #endpoint home
def index():
    return render_template('lorepedia/index.html')

@app.route('/personajes') #endpoint personajes
def personajes():
    return render_template('lorepedia/Paginas/Personajes.html')


if __name__=='__main__':
    # Configura Livereload para Flask
    server = sv(app.wsgi_app)
    server.watch('**/*.html')
    server.watch('**/*.css')
    server.watch('**/*.js')
    server.serve(port=5000, debug=True)