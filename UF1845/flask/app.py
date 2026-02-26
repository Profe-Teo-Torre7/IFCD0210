from flask import Flask,render_template,request,redirect, url_for
import sqlite3

app = Flask(__name__)
BD = "productos.sqlite"


def get_conection():
    cnx = sqlite3.connect(BD)
    cnx.row_factory = sqlite3.Row  # Para usar los nombres de columnas
    return cnx

def init_bd():
    conn = get_conection()
    conn.execute('''
    create table if not exists producto(
            id integer primary key autoincrement,
            codigo text unique not null,
            nombre text not null,
            precio real not null,
            cantidad integer not null,
            fecha_caducidad text not null
            )
    '''
    )
    conn.commit()
    conn.close()

# creamos la bd si no existe
init_bd()




@app.route('/')
def index():
    conn = get_conection()
    productos = conn.execute("select * from producto").fetchall()
    conn.close
    return render_template('index.html', prods=productos)

#Editar producto
@app.route('/editar/<int:id>', methods=['POST','GET'])
def editar(id):
    conn = get_conection()
    producto = conn.execute('select * from producto where id = ?',
                            (id,)).fetchone()
    
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        fecha_caducidad = request.form['fecha_caducidad']

        conn.execute('''update producto set 
                    codigo=?, 
                    nombre=?, 
                    precio=?,
                    cantidad=?,
                    fecha_caducidad=?
                    where id=?
                    ''',
                    (codigo,nombre,precio,cantidad,fecha_caducidad,id)
                    )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('editar.html', prod=producto)

@app.post('/borrar/<int:id>')
def borrar(id):
    pass