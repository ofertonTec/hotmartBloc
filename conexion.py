from flask_mysqldb import MySQL

def conexionBD(app):
    app.config['MYSQL_HOST']= 'us-cdbr-east-06.cleardb.net'
    app.config['MYSQL_USER']='b3b7ac7bff1605'
    app.config['MYSQL_PASSWORD']='27abbfa8'
    app.config['MYSQL_DB']='heroku_300dd68f46f2687'
    return MySQL(app)

