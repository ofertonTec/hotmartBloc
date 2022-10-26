from conexion import *

def listarProductosBD(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT *FROM producto")
    data = cursor.fetchall()
    cursor.close()
    return data

