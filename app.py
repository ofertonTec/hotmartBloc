from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

#INICIO: Referenciar la base de datos y la conexión
app.config['MYSQL_HOST']='us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER']='b3b7ac7bff1605'
app.config['MYSQL_PASSWORD']='27abbfa8'
app.config['MYSQL_DB']='heroku_300dd68f46f2687'
mysql= MySQL(app)
#FIN: Referenciar la base de datos y la conexión

@app.route('/')
def iniciar():
    cursor= mysql.connection.cursor()
    cursor.execute('SELECT *FROM producto')
    data=cursor.fetchall()
    cursor.close()
    print('data: {}'.format(data))
    return render_template('inicio.html', productos=data)

@app.route('/bloc')
def iniciarBloc():
    return render_template('/bloc.html')

if __name__== '__main__':
    app.run(debug=True)
