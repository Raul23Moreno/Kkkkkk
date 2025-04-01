from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        try:
            db = mysql.connector.connect(
                host='db',
                user='ramorenoadmin',
                password='ramoreno23',
                database='usuarios'
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s", (nombre, contrasena))
            usuario = cursor.fetchone()
            db.close()

            if usuario:
                return f'Buenos dias, {nombre}!'
            else:
                return 'Nombre de usuario o contrasena incorrectos.'

        except mysql.connector.Error as err:
            return f'Error de base de datos: {err}'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
