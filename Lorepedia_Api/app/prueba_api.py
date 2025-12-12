import requests
import json

BASE_URL = "http://localhost:5000/api"

def probar_api():
    print("--- Probando guardado de personajes (POST) ---")
    nuevo_personaje = {
        "nombre": "Ejemplo",
        "descripcion": "Descripción del personaje de ejemplo"
    }
    response = requests.post(f"{BASE_URL}/guardarPjs", json=nuevo_personaje)

    if response.status_code == 201:
        print("El personaje se guardó correctamente.", response.json())
    else:
        print("Error al guardar el personaje.", response.json())

    print("--- Probando obtención de personajes (GET) ---")
    response = requests.get(f"{BASE_URL}/personajes")

    if response.status_code == 200:
        print("Personajes obtenidos correctamente.", response.json())
    else:
        print("Error al obtener personajes.", response.json())

if __name__ == "__main__":
    try:
        probar_api()
    except Exception as e:
        print(f"Error al probar la API: {e}")