import pymysql


def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='personajes_db') #nombre base de datos final (la de ahora es test)



#seccion de prueba de conexion
"""
if __name__ == "__main__":
    try:
        conexion = obtener_conexion()


        with conexion.cursor() as cursor:
            sql = "SELECT * FROM songs"

            cursor.execute(sql)

            resultado = cursor.fetchall()
            print(f"Resultados encontrados {resultado}")
            for fila in resultado:
                print(fila)
        conexion.close()
    except Exception as e:
        print(f"error xdxd:   {e}")
"""