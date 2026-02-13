from flask import (Flask,
                    url_for, 
                    redirect,
                    session,
                    request,
                    flash, render_template)

from werkzeug.security import generate_password_hash, check_password_hash
import utilidades as util


app = Flask(__name__)
app.secret_key = "mi_clave_secreta"

USUARIOS = 'usuarios.json'


# Este es el decorador
def login_required(func):
    def envoltura(*args,**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return envoltura


@app.route('/')
def index():
    return redirect(url_for('registrar'))
    if 'user_id' in session:
        return redirect(url_for('principal'))
    return redirect(url_for('login'))

@app.route('/registro', methods=['GET','POST'])
def registrar():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if util.buscar_usuario(USUARIOS,username):
            flash(f"El usuario '{username}' ya existe")
            return redirect(url_for('registrar'))
    
        hashed_password = generate_password_hash(password)

        usuarios = util.cargar_datos(USUARIOS)
        user_id = len(usuarios) + 1

        usuarios.append(
            {
                "id": user_id,
                "username": username,
                "password": hashed_password
            }
        )

        util.guardar_datos(USUARIOS,usuarios)
        flash("Usuario creado correctamente")
        return redirect(url_for('login'))
    
    return render_template('registrar.html')

@app.route('/principal')
def principal():
    pass

@app.route('/login')
def login():
    pass

@app.route('/logout')
def logout():
    pass