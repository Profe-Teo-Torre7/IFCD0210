from flask import Flask, render_template,request
import utilidades as util

app = Flask(__name__)

PRODUCTOS = 'productos.json'


@app.route('/')
def index():
    datos = util.cargar_datos(PRODUCTOS)
    categ = datos["categorias"]
    prods = datos["productos"]

    id_producto = request.args.get("producto")

    return render_template('index.html', productos=prods, categorias = categ)