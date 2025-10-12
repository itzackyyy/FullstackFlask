from flask import Flask, render_template
from livereload import Server as sv
import psycopg2


app=Flask(__name__)

@app.route('/login')#endpoint login
def login():
    return render_template('lorepedia/iniciarSesion.html')

@app.route('/registrar')
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