from flask import Flask, render_template
from livereload import Server as sv
import psycopg2


app=Flask(__name__)



@app.route('/')
def login():

    return render_template('login.html')

@app.route('/home')
def index():
    return render_template('lorepedia/index.html')


if __name__=='__main__':
    app.run(debug=True, port=5000)



# para leer los archivos HTML, CSS Y JS 
# que esten dentro de /static y /templates :D
sv.watch('**/*.html')
sv.watch('**/*.css')
sv.watch('**/*.js')