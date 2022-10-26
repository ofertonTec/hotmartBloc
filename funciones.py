from flask import session
from conexion import *

def dataLoginSesion():
    inforLogin = {
        "dni"               :session['dni'],
        "tipoUser"             :session['tipoUser'],
        "nombre"                :session['nombre'],
        "apellido"              :session['apellido'],
        "email"                 :session['email'],
        "sexo"                  :session['sexo'],

    }
    return inforLogin

def dataPerfilUsuario():
    conexion_MySQL= conexionBD()
    cursor= conexion_MySQL.cursor(dictionary =True)
    idLogin=  session['dni']
    query = ("SELECT * FROM usuario  WHERE DNI='%s'", idLogin)
    cursor.execute(query)
    datoUsuario= cursor.fetchone()
    cursor.close()
    conexion_MySQL.close()
    return datoUsuario

#Convertir dataResult a list
def converToDictionary(data):
    usuarios=[]
    for row in data:
        usuario = {"dni":row[0],"tipo_usuario":row[1],"nombre":row[2],"apellido":row[3],"email":row[4],"password":row[5],"sexo":row[6]}
        usuarios.append(usuario)
    return usuarios
