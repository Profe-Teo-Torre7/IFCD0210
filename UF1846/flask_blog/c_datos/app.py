from flask import Flask,request,jsonify
import mysql.connector
import config

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(host=config.HOST, 
                        user=config.USER,
                        password=config.PASSWORD,
                        database=config.DATABASE,
                        port=config.PORT)




def fetch_all(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query,params or ())
    result = cursor.fetchall()
    conn.close()
    return result

def fetch_one(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query,params or ())
    result = cursor.fetchone()
    conn.close()
    return result

def execute(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query,params or ())
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id


# Endpoints de usuarios

@app.route('/data/user/by-email')
def get_user_by_email():
    email = request.args.get('email')
    user = fetch_one("select * from usuarios where email = %s", (email,))
    return jsonify(user)


@app.route('/data/user', methods=['POST'])
def create_user():
    data = request.json
    user_id = execute(
        "insert into usuarios(nombre,email,pw_hash,rol,f_alta) values(%s,%s,%s,%s,%s)",
        (
        data['nombre'],
        data['email'],
        data['pw_hash'],
        data['rol'],
        data['f_alta'])
        )
    return jsonify({'id':user_id})

