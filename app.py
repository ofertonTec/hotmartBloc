from itertools import count
from flask import Flask, render_template,redirect,url_for, request,session

#INICIO: mis archivos adicionales .py creados
from conexion import *
from funciones import *
from productos import listarProductosBD

#Inicializando la aplicación
app=Flask(__name__)

#Definiendo la clave secreta para poder accesar al sistema
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

#INICIO: Referenciar la base de datos y la conexión
mysql= conexionBD(app)

#INICIO: Definiendo ruta por defecto
@app.errorhandler(404)
def not_found(error):
    return redirect('/')


#INICIO: renderizando a login.html
@app.route('/')
def mostrarLogin():
    return render_template('modulo_login/login.html' )

#INICIO: enviando la información del login
@app.route('/login', methods=['POST','GET'])
def ingresarSistema():
    usuario= request.form['usuario']
    password= request.form['password']
    #verificar si existe el email
    cursor=mysql.connection.cursor()
    sql=("select *from usuario where email='%s'" % usuario)
    cursor.execute(sql)
    data= cursor.fetchone()
    if data !=None:
        user = {"dni":data[0],"tipo_usuario":data[1],"nombre":data[2],"apellido":data[3],"email":data[4],"password":data[5],"sexo":data[6]}
        if request.method=='POST' and password == user['password'] and usuario==user['email']:
            print('ingresa al sistema')

            session['conectado']  =True
            session['dni']= user['dni']
            session['tipoUser'] =user['tipo_usuario']
            session['nombre'] =user['nombre']
            session['apellido'] =user['apellido']
            session['email'] =user['email']
            session['sexo'] =user['sexo']
            listaProductos= listarProductosBD(mysql)
            return render_template('dasboard/home.html', dataLogin= dataLoginSesion(),productos=listaProductos)

        else:
            return render_template('modulo_login/login.html')
        
    else:
        return render_template('modulo_login/login.html' )



#INICIO: Renderizando al archivo nuevo_usuario.html
@app.route('/registro')
def registrarUsuario():
    return render_template('modulo_login/nuevo_usuario.html')


#INICIO: Enviando los datos del formulario
@app.route('/NuevoUsuario', methods=['POST'])
def crearNuevoUsuario():
    dni= request.form['dni']
    tipoUsuario= 2
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    email =request.form['email']
    password= request.form['password']
    sexo= request.form['genero']

    cursor= mysql.connection.cursor()
    sql=("INSERT INTO usuario VALUES(%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(sql,(dni,tipoUsuario,nombre,apellido,email,password,sexo))
    mysql.connection.commit()
    
    print(f'query:{sql}')
    return render_template('modulo_login/login.html')





# Lista de productos
@app.route('/productos')
def mostrarProductos():
    if 'conectado' in session:
        data = listarProductosBD(mysql)
        return render_template('dasboard/home.html', productos=data, dataLogin= dataLoginSesion())
    else:
        return redirect('/')

    

@app.route('/bloc')
def iniciarBloc():
    return render_template('dasboard/bloc.html')


@app.route('/cerrarSesion')
def cerrarSesion():

    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    session.pop('dni', None)
    session.pop('email', None)
    return render_template('modulo_login/login.html')

if __name__== '__main__':
    app.run(debug=True)
