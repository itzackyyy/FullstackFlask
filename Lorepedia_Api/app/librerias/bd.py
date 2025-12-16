# importacion de librerias para soportar MongoDB Community Edition (en este caso xd).

from pymongo import MongoClient

def obtener_bd():
    cliente = MongoClient("mongodb://localhost:27017")
    return cliente['lorepediaDB']