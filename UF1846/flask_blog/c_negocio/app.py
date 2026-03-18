import requests
from flask import Flask,request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

RUTA_DATOS = 'http://localhost:5001/data'

# ----------------------------

def get_user_by_email(email):
    resp = requests.get(f"{RUTA_DATOS}/user/by-email",params={'email':email})
    return resp.json()

def create_user_db(user_data):
    resp = requests.post(f"{RUTA_DATOS}/user",json=user_data)
    return resp.json()

def get_posts_db():
    resp = requests.get(f"{RUTA_DATOS}/posts")
    return resp.json()

def get_post_db(post_id):
    resp = requests.get(f"{RUTA_DATOS}/post/{post_id}")
    return resp.json()

def create_post_db(data):
    resp = requests.post(f"{RUTA_DATOS}/post",json=data)
    return resp.json()

def update_post_db(post_id,data):
    resp = requests.put(f"{RUTA_DATOS}/post/{post_id}",json=data)
    return resp.json()

def delete_post_db(post_id):
    resp = requests.delete(f"{RUTA_DATOS}/post/{post_id}")

# -------------------------------------------

@app.route("/api/login",methods=['POST'])
def login():
    data = request.json

    user = get_user_by_email(data['email'])
    if not user:
        return jsonify({'error':'El usuario no existe.'}),401
    
    if not check_password_hash(user['pw_hash'],data['password']):
        return jsonify({'error':'Password incorrecta.'}),401
    
    return jsonify(
        {'mensaje': "Login correcto.",
        'user_id':user['id'],
        'rol': user['rol']}
    )

# ---------------------------------

@app.route('/api/posts')
def get_posts():
    posts = get_posts_db()
    publicados = []

    for p in posts:
        if p['estado'] == 'publicado':
            publicados.append(p)
    
    return jsonify(publicados)


