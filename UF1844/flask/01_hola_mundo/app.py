from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_world():
    return "Hola Mundo "


@app.route('/hola')
def hola():
    cadena = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Hola Usuario</h1>
            <h2>Bienvenido a mi sitio Flask</h2>
        </body>
        </html>
        """
    return cadena


@app.route('/prueba')
def prueba():
    return render_template('prueba.html')


if __name__ == '__main__':
    app.run(debug=True)
