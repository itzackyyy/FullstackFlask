from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from livereload import Server as sv
from librerias import controlador_personajes as cp

app = Flask(__name__)

# ==============================
# CONFIGURACIÓN MONGO DB
# ==============================
# Puerto: 27017
app.config["MONGO_URI"] = "mongodb://localhost:27017/lorepediaDB"
mongo = PyMongo(app)

# ==============================
# ENDPOINTS API
# ==============================

@app.route('/')
def index():
    return jsonify({"estado": "API ONLINE", "mensaje": "Welcome to Lorepedia API"})

# Obtención de personajes
@app.route('/api/personajes', methods=['GET'])
def obtener_personajes():
    coleccion_pjs = mongo.db.personajes
    datos = []

    for personaje in coleccion_pjs.find():
        datos.append({
            'id': str(personaje['_id']), #Esto DEBERIA de convertir id a string
            'nombre': personaje.get('nombre'),
            'descripcion': personaje.get('descripcion')
        })

    return jsonify(datos)

# Guardado de personajes
@app.route('/api/guardarPjs', methods=['POST'])
def guardar_personaje():
    # JSON desde el cliente (POSTMAN O React)
    datos_entrada = request.json
    nombre = datos_entrada.get('nombre')
    descripcion = datos_entrada.get('descripcion')

    if nombre and descripcion:
        id_insertado = mongo.db.personajes.insert_one({
            'nombre': nombre,
            'descripcion': descripcion
        })

        return jsonify({
            'mensaje': 'Personaje guardado correctamente',
            'id': str(id_insertado.inserted_id)
        }), 201
    else:
        return jsonify({'error': 'Faltan datos'}), 400

@app.route('/editarPersonaje/<id_personaje', methods=['UPDATE'])
def editar_personaje(id_personaje):
    personaje_encontrado = cp.obtener_personaje_id(id_personaje)
    return jsonify({'mensaje': 'Personaje editado correctamente'}, personaje = personaje_encontrado)

@app.route('/actualizarPersonaje/<id_personaje>', methods=['PUT'])
def actualizar_personaje(id_personaje):
    id_personaje = request.form["id_personaje"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    cp.actualizar_personaje(id_personaje, nombre, descripcion)
    return jsonify({'mensaje': 'Personaje actualizado correctamente'})

# Eliminar personaje
@app.route('/api/eliminarPjs/<id>', methods=['DELETE'])
def eliminar_personaje(id):
    mongo.db.personajes.delete_one({'_id': ObjectId(id)})
    return jsonify({'mensaje': 'Personaje eliminado correctamente'}), 200

if __name__=='__main__':
    server = sv(app.wsgi_app)
    server.serve(port=5000, debug=True)