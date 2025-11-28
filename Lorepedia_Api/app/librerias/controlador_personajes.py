from librerias import bd




def insertar_personaje(nombre, descripcion):
    conexion = bd.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO PERSONAJES (nombre, descripcion) values (%s, %s)",
                       (nombre, descripcion))
        conexion .commit()
        conexion.close()


def obtener_personaje():
    conexion = bd.obtener_conexion()
    personajes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM PERSONAJES")
        personajes = cursor.fetchall()
    conexion.close()
    return personajes

def eliminar_personaje(id_personaje):
    conexion = bd.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM PERSONAJES WHERE id_personaje = %s", (id_personaje,))
    conexion.commit()
    conexion.close()


def obtener_personaje_id(id_personaje):
    conexion = bd.obtener_conexion()
    personaje = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_personaje, nombre, descripcion FROM PERSONAJES WHERE id_personaje = %s ", (id_personaje,))
        personaje = cursor.fetchone()
    conexion.close()
    return personaje

def actualizar_personaje(nombre, descripcion, id_personaje):
    conexion = bd.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE PERSONAJES SET nombre = %s, descripcion = %s WHERE id_personaje = %s",
            (nombre, descripcion, id_personaje))
    conexion.commit()
    conexion.close()